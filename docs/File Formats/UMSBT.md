---
date created: 2023-08-23 12:09
date updated: 2023-08-23 12:28
---

## Introduction:

UMSBT files are a proprietary format used primarily in Nintendo games. Standing for "Unified Message String Bundle Table," UMSBT files serve as containers for MSBT files, which in turn store in-game text data. This bundling ensures that multiple language variants of text data can be stored and accessed efficiently within a single game.

## Structure and Components:

1. Bundled MSBT Files: The primary content of a UMSBT file is a collection of MSBT files. Each MSBT file corresponds to a specific language or regional variant, containing text strings relevant to that localization.
2. Headers: UMSBT files begin with a header section providing metadata about the bundled content, such as the number of contained MSBT files, their respective languages, and other structural details.
3. Indexes: Typically, UMSBT files will feature an indexing system that allows the game engine to rapidly access specific strings or languages, streamlining the process of rendering text based on player settings or system locale.
4. Language Metadata: Information about the included languages, like language codes or regional identifiers, might be embedded to facilitate quick identification and switching.
