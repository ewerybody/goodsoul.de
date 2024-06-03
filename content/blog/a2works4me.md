+++
date = 2024-03-18
title = "a2 - works for me"
[taxonomies]
tags = ["code", "projects"]
+++
Almost **12 years ago** (!!!)* I made [the initial commit on GitHub for a2](https://github.com/ewerybody/a2/commit/71031e49299a2e1189a30405380581b02c28c5c9). The thing was always planned as "never finished, always in development" but sure you gotta get somewhere somewhen, right? So what's the holdup?

Well, I guess the biggest "problem" is that is just `works for me`™️.

It runs all day every day and helps me here and there countless times. I only really recognize it when it's not running or there is some edge-case I didn't have yet. OR: my favorite actually: When I get reports and or feature requests :) Like I do work at Crytek all the time basically. Just not on a2.

Still I have some things up my sleeve that I really want to do for a2 in the near future. Of course there is also [the issue tracker](https://github.com/ewerybody/a2/issues). But that's mostly specific technical things there and I want to gather my thoughts here about the bigger picture. Eventually all this needs to be reflected in the tracker.

So, if you don't even know what I'm talking about: THAT's also up the sleeve ... ehm on this list. Is it the most important thing? No idea. There are other pressing general issues it's just really really about time for the actual explanation of "**What is a2?**"! Doing it right away though would just feel a little off meanwhile. Since a couple years I'm doing Python code each and every day for the company and my standards shifted quite a lot. Of course there are loads of places in a2 that I now find uber ugly and would love to fix right away.

Alright. Out with it. Here the list and then some details:

- [ ] a2 core free from ui
- [ ] back on track with latest Qt for Python 6
- [ ] resolve the **What is a2?** issue
- [x] run on latest Autohotkey 2
- [ ] un-coupled user/dev element parts

# a2 core refactor

The current [`a2core`](https://github.com/ewerybody/a2/blob/master/ui/a2core.py) is already not using any UI code. That's good but it's also lacking some things that one needs the UI for!

Adding and changing elements of a module is entangled with ui-code. This must be something that the a2 core/backend is doing. After all I'd even like **hotkeys** handled by the core!

It's probably no wonder that I didn't envision it like that > 10 years ago but now I'd like to be able to have an a2 CLI that can basically do all this from the terminal and the UI is rather optional, displaying things nicely and calling into the core for changes. This core could even be based on yet another language really but for starters Python is just fine 🤞

# latest Qt for Python 6

The tool turned out with this kind of UI since I gathered XP with PySide professionally. I was already kinda fluent with it and Qt is still nice and up-to-date! So why aren't we on the edge as of now? Well, Qt for Python developed faster than I could pick up the pace. "Back in the days" I thought multiple inheritance was really smart. It isn't. Resolving it all with proper dependency injection is SO much nicer and rewarding! And it works better with Qt for Python. Currently I don't really know if it's actually like "working at all" without multi-inheritance but I also don't care. This crap needs to go AND it fixes the problems with latest Qt :) win-win!

# How to What is ...

Videos. I'd actually like to make shorts explaining aspects of a2. Might be something like the format of [Fireship on YouTube](https://www.youtube.com/@Fireship). There should really be some compact straight-to-the-point videos about:

* what is a2 (Ahk runtime, some examples, config with ui, make own modules)
* how to get a2 (download from GitHub, install, ignore windows warning, how to update)
* big video with all a2.modules and time stamps to jump into
* short about each of the a2.modules
* how to make mods
* how to develop a2 (fork, get python, get PySide6, setup vs code)

# latest Ahk 2

Not unlike the Python world Ahk is split into legacy and latest. Ahk 2 has been on the horizon for ages and I was always too lazy to go for it and give it a try. Meanwhile it was made the default and I actually managed to do some tests and ported some library stuff. But that's a tiny step yet and there is quite some chunk of work ahead! The big question is still if it would work at all the way we build the Ahk script files and start/restart the runtime but, well it's the future™ and it would be rather embarrassing to not attempt the move.

# un-coupling elements

The module building blocks need another overhaul.

Currently the developer Ui and code always loads when we just use them the default way. The hotkey element already has its own directory under a2elements. Let's do it that way for any element and have user and dev .py files underneath.

For once I still believe in separation of code and data. Most Ui is data anyway and if it can be handled with a dedicated tool, let's do it! But currently some default settings values of some of the module building blocks are only just set by the Ui. That's dirty and must come from a dedicated defaults JSON for each and every element.

# conclusion

So yeah. There you have it. That's another 5 years of work? ;D I don't know. I'm still not even sure about the order. Maybe we do Ahk 2 first?

\* seems like there's a pattern of [reminiscing about ancient stuff in my past life here](@/blog/goodsoul40.md).
