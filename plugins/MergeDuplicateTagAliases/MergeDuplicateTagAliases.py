import sys
import json
import math
import time
from stashapi.stashapp import StashInterface
import stashapi.log as log

FRAGMENT = json.loads(sys.stdin.read())
TAG_MAP = {}

# Initialize connection to Stash
stash = StashInterface(FRAGMENT["server_connection"])

def fetch_all_tags_missing_stash_db_id(endpoint):
    log.info("Fetching all tags missing Stash DB ID....")
    tag_filter = {
        "stash_id_endpoint": {
            "endpoint": endpoint,
            "stash_id": "",
            "modifier": "IS_NULL"
        }
    }
    
    all_tags = []
    page = 1
    per_page = 100

    while True:
        filter_opts = {
            "page": page,
            "per_page": per_page,
            "sort": "scenes_count",
            "direction": "DESC"
        }
        tags = stash.find_tags(f=tag_filter, filter=filter_opts)
        if not tags:
            break
        
        all_tags.extend(tags)
        
        if len(tags) < per_page:
            break
            
        page += 1

    return all_tags


def fetch_all_tags():
    log.info("Fetching all tags into lookup map....")
    page = 1
    per_page = 100

    while True:
        filter_opts = {
            "page": page,
            "per_page": per_page,
            "sort": "scenes_count",
            "direction": "DESC"
        }
        tags = stash.find_tags(filter=filter_opts)
        if not tags:
            break

        for tag in tags:
            TAG_MAP[tag["name"]] = tag

        if len(tags) < per_page:
            break

        page += 1


def search_tag(tag_name):
    query = """
    query ScrapeSingleTag($source: ScraperSourceInput!, $input: ScrapeSingleTagInput!) {
      scrapeSingleTag(source: $source, input: $input) {
        stored_id
        name
        description
        alias_list
        parent {
          stored_id
          name
          description
        }
        remote_site_id
      }
    }
    """
    variables = {
        "source": {"stash_box_endpoint": "https://stashdb.org/graphql"},
        "input": {"query": tag_name.strip()}
    }

    res_data = stash.call_GQL(query, variables)
    scraped = res_data.get("scrapeSingleTag", [])
    matches = [t for t in scraped if t.get("name", "").strip().lower() == tag_name.strip().lower()]
    return matches[0] if matches else None


def merge_tag(source_tags, dest_tag):
    source_ids = [tag["id"] for tag in source_tags]
    dest_id = dest_tag["id"]

    try:
        result = stash.merge_tags(source_ids=source_ids, destination_id=dest_id)
        if result:
            return f"Tag {dest_id}: Success | Result: {json.dumps(result)}"
        return f"Tag {dest_id}: Failed | Result: {json.dumps(result)}"
    except Exception as e:
        return f"Tag {dest_id}: Exception | {e}"


def process_tag(tag, dry_run):
    log.info(f"Processing Tag: {tag['name']}")
    scrapped_tag = search_tag(tag["name"])
    
    if not scrapped_tag:
        log.info(f"{tag['name']}: Unable to scrape. No match found of same name.")
        return

    alias = scrapped_tag.get("alias_list")
    if not alias:
        log.info(f"{tag['name']}: No alias found.")
        return

    log.info(f"{tag['name']} : Alias ==>>  {alias}")

    alias_tag_result = [TAG_MAP.get(a_name) for a_name in alias]
    existing_alias = [r for r in alias_tag_result if r is not None]

    if not existing_alias:
        log.info("No existing alias tag found. Skipping merge.")
        return

    existing_names = [t["name"] for t in existing_alias]
    log.info(f"{tag['name']} : Existing Alias ==>>  {existing_names}")

    if dry_run:
        log.info(f"Dry run: {existing_names} >> will be merged into >> {tag['name']}")
    else:
        result = merge_tag(existing_alias, tag)
        log.info(f"Merge Result: {result}")

def merge_duplicate_aliases(dry_run, endpoint):
    log.info("Running dev-code from local machine!!!!!!!")
    
    if dry_run:
        log.info("DRY RUN MODE ENABLED. No changes will be saved to Stash.")
    else:
        log.info("LIVE MODE ENABLED. Changes will be written to the database.")

    all_tags = fetch_all_tags_missing_stash_db_id(endpoint)
    total_tags = len(all_tags)

    log.info(f"Starting scan of {total_tags} tags")

    for index, tag in enumerate(all_tags, start=1):
        log.info(f"Processing tag {index}/{total_tags}")
        process_tag(tag, dry_run)
        log.info("---------------------------------------")
        log.progress(index/total_tags)

    log.info("Merge Duplicate Tag Aliases task finished!")

    
def main():
    # Parse configuration payload provided by Stash via stdin
    try:
        input_data = json.loads(sys.stdin.read())
    except Exception:
        input_data = {}

    # Extract the user setting. Fallback to True for safety if missing.
    plugin_settings = input_data.get("server_connection", {}).get("PluginConfig", {})
    dry_run = plugin_settings.get("dry_run", True)
    endpoint = plugin_settings.get("stash_src", "https://stashdb.org/graphql")
    
    # Verify task argument from the YML configuration
    if len(sys.argv) > 1 and sys.argv[1] == "merge_tags":
        merge_duplicate_aliases(dry_run, endpoint)
    else:
        log.error(f"Invalid execution argument received: {sys.argv}")

if __name__ == "__main__":
    main()
