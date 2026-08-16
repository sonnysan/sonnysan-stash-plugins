### 🚧 Merge Duplicate Tag Aliases (Development in progress ....)

A Stash plugin that helps clean up tag aliases by finding tags in your library that are aliases of a primary tag on **StashDB** or another configured primary Stash source.

Instead of manually searching for alternate tag names and replacing them one by one, this plugin helps identify those relationships and merge the aliases into the canonical tag.

## ✨ What It Does

The plugin:

* 🔍 Scans your existing Stash tags
* 🌐 Checks StashDB and configured primary Stash sources for tag aliases
* 🎯 Identifies the primary/canonical tag for each alias
* 🔗 Groups aliases that refer to the same primary tag
* 🔄 Lets you merge alias tags into the primary tag
* 🧹 Helps remove redundant tags from your library
* 🏷️ Makes your local tags more consistent with your metadata source

## 💡 Example

Imagine your Stash library contains several tags:

```text
60 FPS
60 Frames
60FPS
60p
High Frame Rate
```

The primary metadata source may define **60 FPS** as the canonical tag and recognize the others as aliases.

The plugin can identify the relationship:

```text
60 Frames       ──┐
60FPS           ──┤
60p             ──┼──► 60 FPS ⭐
High Frame Rate ──┘    Primary Tag
```

You can then merge the aliases into **60 FPS**.

After the merge, instead of maintaining several versions of the same tag, your library uses the canonical tag:

```text
60 FPS
```

### 🔄 Why This Helps

Over time, tags can become inconsistent because of:

* Manual tagging
* Different metadata sources
* Changes in preferred tag names
* Importing metadata from external sources
* Different names being used for the same concept

The plugin uses the alias information provided by your metadata source to help bring those tags back together.

## 🌐 Metadata Sources

The plugin can use:

* **StashDB**
* **Primary Stash sources configured in Stash**

This allows the plugin to work with the metadata sources already used by your Stash installation.

## 🚀 Installation

Install the plugin through a Stash plugin repository or install it manually using the plugin files.

For general information about Stash plugins, see the [Stash plugin documentation](https://docs.stashapp.cc/plugins/).

### 📦 Plugin Repository

If installing from the accompanying plugin repository, add its `index.yml` as a custom plugin source in:

**Settings → Plugins → Available Plugins → Add Source**

## ⚙️ Usage

After installation:

1. Open the plugin from Stash.
2. Scan your tags for known aliases.
3. Review the aliases and their corresponding primary tags.
4. Select the tags you want to consolidate.
5. Merge the aliases into their primary tags.
6. Review your tags after the operation.

> 💡 **Tip:** Review the proposed merges before applying them, particularly when working with a large existing library.

## ⚠️ Important

Merging tags changes your existing Stash metadata.

It is recommended to have a current backup of your Stash database before performing large-scale tag cleanup.

## 🐛 Issues & Feedback

If you encounter a problem or find an incorrect alias relationship, please open an issue with:

* 🖥️ Your Stash version
* 🔢 Plugin version
* ⚠️ Error messages, if applicable
* 🏷️ The affected tag(s)
* 🔁 Steps to reproduce the issue

Suggestions and feature requests are also welcome.

## 👨‍💻 Author

Developed by **[sonnysan](https://github.com/sonnysan)**.

## ⚖️ Disclaimer

This is an independent community plugin and is not affiliated with, endorsed by, or officially supported by the Stash project or StashDB.

## 📄 License

See the `LICENSE` file included with this plugin.
