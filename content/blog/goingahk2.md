+++
date = 2024-08-18
title = "Going Autohotkey 2"
[taxonomies]
tags = ["code", "projects"]
+++
Whow! **Exactly** 5 months ago [I wrote about the next big things on my a2 project](@/blog/a2works4me.md). One of these 5 things was switching its scripting language Autohotkey to the now officially supported version 2, deprecating the old 1.1 version that a2 scripts were based on so far.

Well, I kind of suggested doing this of the 5 right away and yeah, that's what this post is about :]

So I jumped into it. Here is an issue to track the whole thing: [#266](https://github.com/ewerybody/a2/issues/266). To resolve the first things I swapped the Autohotkey.exe to the new version, tried to run it and fixed it piece by piece until it no longer complained. There are now `ahk2` branches for [a2](https://github.com/ewerybody/a2/tree/ahk2), [a2.modules](https://github.com/ewerybody/a2.modules/tree/ahk2) and [a2.modlab](https://github.com/a2script/a2.modlab/tree/ahk2) amounting 145 commits (code submissions) ahead of their main branches as of now.

That bulk of work was actually quite fun! I didn't have such a surge of productivity on the project for long! It was rather dull work but it felt super rewarding. Heaps of low hanging fruit harvest! Quickly I knew about what makes it tick now and how things need to be done now and I gotta say: This is a different beast than Python 2/3 conversion! (Which is another topic on it's own. Just so much: We're maintaining a whole big ass library running on Python 2 and 3 all time at the company and it's totally doable!) As for Autohotkey though, no can do! I guess there might be very simple Autohotkey scripts that can run both on 1.1 and 2.0 but generally the changes are rather substantial and I'm sure we'll see why.

tbd: I'll go through some of the commits and list the most offenders that I encountered myself. The actual documentation "[*Changes from v1.1 to v2.0*](https://www.autohotkey.com/docs/v2/v2-changes.htm)" is (according to [WordCount](https://github.com/ewerybody/a2.modules/tree/master/texTools#wordcount---tooltip-with-selected-text-information-wino)) 24318 words, 141258 characters and 1803 lines long!! (I didn't read it all. Only what I needed) and here is the stuff that I stumbled over while working on it:

* The comma after `CommandName,` is gone. For these there needs to be a space now between the first argument. But ALL can also be written like functions!
* assignments as well as default arguments **need** the walrus operator `:=`
  before it could be **both**!
* `byref` is now `&` and much more explicit
  so you cannot pass a string when a reference is expected. I mean yeah, duh! But that was possible before!!!
* Strings are always in quotes and mix of `'` and `"` are valid! To write a single literal `"` now it's `'"'` and ... (I kid you not) no longer `""""`. You don't need percentage notation `%varname%` for concatenation.
* `my_array.Length` is now a property and can no longer be called
* ...

### mopping up

So that being mostly done (I really dunno what other v1/2 code problems lurk there) I need to wrap it into a new package that the user eventually can consume. Me being my prime user, I already discovered lots of problems with startup, legacy settings in the database and custom scripts. I fixed it all in place for myself but yet not in a programmatic way. So that left me trampling on the spot for a while. But I think I have a plan for how to move forward:

Let's fix the install scripts in a way that it can do a fresh install. Like for a "new user". Leaving legacy stuff behind for a moment I think that's a nice thing to focus on. When that's covered we can get on with the fixes needed for an actual update!
