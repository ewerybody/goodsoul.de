+++
date = 2026-10-29
title = "computer things"
draft = false
[taxonomies]
tags = ["bla", "computers"]
+++

I ... I should probably look into [nix](https://nixos.org/). But I was stopping myself here already. We're not there yet! Darn, I still have a windows machine 💩
However: I just want to remember some setup things that I constantly re-lookup and now I'll have a spot to put these! Yay!

- [Firefox](https://getfirefox.com)
  - [x] New Tab next to current: set `browser.tabs.insertAfterCurrent` to `true`
  - [x] Make F11 automatically hide the toolbar `browser.fullscreen.autohide` to `true`
  - [ ] Install [Sideberry](https://addons.mozilla.org/en-US/firefox/addon/sidebery/)? 🤔

- [VS Codium](https://vscodium.com/)
  - [ ] How to platform agnostic things in `.vscode/launch.json`?\
        [Hhatatatatata](https://youtube.com/shorts/DtdlPiYPln0)! Do you **really** want that?!
        If it's about the os path difference to the Python interpreter in `.venv`?\
        You can also use `${command:python.interpreterPath}`! That one must have been set anyway.\
        Not? Ok: Here you go: [There are `linux`, `osx` and `windows` sections that can be configured!](https://code.visualstudio.com/docs/debugtest/debugging-configuration#_platform-specific-properties)
- ... more to come :)



Sure, eventually this all should go into some nix-config on a git repo? That'd be pretty cool. Well not today my friend. Not today. :]
