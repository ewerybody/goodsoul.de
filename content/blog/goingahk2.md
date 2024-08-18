+++
date = 2024-08-18
title = "Going Autohotkey 2"
[taxonomies]
tags = ["code", "projects"]
+++
Whow! **Exactly** 5 months ago [I wrote about the next big things on my a2 project](@/blog/a2works4me.md). One of these 5 things was switching its scripting language Autohotkey to the now officially supported version 2, deprecating the old 1.1 version that a2 scripts were based on so far.

Well, I kind of suggested doing this of the 5 right away and yeah, that's what this post is about :]

So I jumped into it, swapped the Autohotkey.exe to the new version, tried to run it and fixed it piece by piece until it no longer complained. There are now `ahk2` branches for [a2](https://github.com/ewerybody/a2/tree/ahk2), [a2.modules](https://github.com/ewerybody/a2.modules/tree/ahk2) and [a2.modlab](https://github.com/a2script/a2.modlab/tree/ahk2) amounting 145 commits (code submissions) ahead of their main branches as of now.

That bulk of work was actually quite fun! I didn't have such a surge of productivity on the project for long! It was rather dull work but it felt super rewarding. Heaps of low hanging fruit harvest! Quickly I knew about what makes it tick now and how things need to be done now and I gotta say: This is a different beast than Python 2/3 conversion! (Which is another topic on it's own. Just so much: We're maintaining a whole big ass library running on Python 2 and 3 all time at the company and it's totally doable!) As for Autohotkey though, no can do! I guess there might be very simple Autohotkey scripts that can run both on 1.1 and 2.0 but generally the changes are rather substantial and I'm sure we'll see why.

tbd: I'll go through some of the commits and list the most offenders.

* default arguments **need** the walrus operator :=
* `byref` is now `*` and much more explicit
* ...