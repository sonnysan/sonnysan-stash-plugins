# 🧩 Stash Plugins

A collection of plugins for [Stash](https://github.com/stashapp/stash), developed and maintained by [sonnysan](https://github.com/sonnysan).

The plugins focus on improving **metadata management, organization, and consistency** within Stash libraries.

## 📦 Plugins

### 🔗 Merge Duplicate Tag Aliases

**Merge Duplicate Tag Aliases** helps keep your Stash tags consistent with the tags defined by StashDB and other primary metadata sources.

The plugin checks existing tags for known alias relationships. When multiple tags are recognized as aliases of a primary tag, the plugin identifies the canonical tag and allows the aliases to be merged into it.

This is useful for cleaning up an existing library where different tag names represent the same concept.

### 💡 Example

Suppose your library contains several tags referring to the same concept:

```text
60 FPS
60 Frames
60FPS
60p
High Frame Rate
```

Your metadata source may define **60 FPS** as the primary tag, with the others recognized as aliases:

```text
60 Frames       ──┐
60FPS           ──┤
60p             ──┼──► 60 FPS
High Frame Rate ──┤      ⭐ Primary
                 ──┘
```

The plugin detects these relationships and lets you merge the alias tags into the primary **60 FPS** tag.

After the merge, your library contains the canonical tag:

```text
🏷️ 60 FPS
```

This makes it easier to maintain consistent tags and match your local library with the terminology used by StashDB or another primary metadata source.

### ✨ Features

* 🔍 Detect tags that have known aliases
* 🌐 Check alias relationships from StashDB
* 🔗 Use other configured primary Stash sources
* 🎯 Identify the corresponding primary tag
* 🧩 Handle multiple aliases for a single tag
* 🔄 Merge alias tags into the primary tag
* 🧹 Reduce duplicate and inconsistent tags
* 📚 Keep local tagging aligned with external metadata sources

## 🚀 Installation

The repository can be added to Stash as a custom plugin source.

1. ⚙️ Open **Settings → Plugins**
2. 📋 Open **Available Plugins**
3. ➕ Select **Add Source**
4. 🔗 Enter this repository's `index.yml` URL
5. 💾 Save the source
6. 📦 Install the plugin from the available plugins list

For more information, see the [Stash plugin documentation](https://docs.stashapp.cc/plugins/).

## 🔗 Plugin Source

```text
https://sonnysan.github.io/<repository-name>/index.yml
```

Replace `<repository-name>` with the name of this repository.

## 👨‍💻 About

These plugins are developed and maintained by **sonnysan**.

🐙 [GitHub](https://github.com/sonnysan)

Issues, suggestions, and improvements are welcome.

## 🤝 Contributing

When reporting an issue, please include:

* 🏷️ Plugin version
* 🖥️ Stash version
* ⚠️ Relevant error messages
* 🔁 Steps needed to reproduce the problem

## ⚠️ Disclaimer

These are independent community plugins and are **not affiliated with or officially supported by the Stash project**.

## 📄 License

See the repository's `LICENSE` file for licensing information.
