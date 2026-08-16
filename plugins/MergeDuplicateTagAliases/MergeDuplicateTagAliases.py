import sys
import json
from stashapi.stashapp import StashInterface
import stashapi.log as log

FRAGMENT = json.loads(sys.stdin.read())
MODE = FRAGMENT["args"]["mode"]

# Initialize connection to Stash
stash = StashInterface(FRAGMENT["server_connection"])

def merge_duplicate_aliases(dry_run):
    if dry_run:
        log.info("DRY RUN MODE ENABLED. No changes will be saved to Stash.")
    else:
        log.info("LIVE MODE ENABLED. Changes will be written to the database.")
    
    try:
        tags = stash.find_tags(fragment="id name aliases")
        log.info(f"Successfully scanned {len(tags)} tags.")
        
        # Example safety logic:
        # if dry_run:
        #     log.info(f"[Dry Run] Would merge Tag A into Tag B")
        # else:
        #     stash.merge_tags(source_ids, destination_id)
            
    except Exception as e:
        log.error(f"An error occurred during execution: {str(e)}")
        return

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

    # Verify task argument from the YML configuration
    if len(sys.argv) > 1 and sys.argv[1] == "merge_tags":
        merge_duplicate_aliases(dry_run)
    else:
        log.error(f"Invalid execution argument received: {sys.argv}")

if __name__ == "__main__":
    main()
