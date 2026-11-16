+++
date = 2026-10-29
title = "🍏🐛 mac thoughts"
draft = false
[taxonomies]
tags = ["bla", "computer", "list"]
+++

So, the team I'm now working with had me picking a new company device. As it was kindly suggested, I didn't have any solid XP with it, and thought that'd complete my "collection" of the 3 OSs I accepted the recommendation and chose a MacBook. (Maybe... I now wish they'd have [framework ones](https://frame.work/de/en/laptop13)!)
I'm quite new to working on a mac. Sure, I did a couple things here and there but working all day on one I did not yet.
But I'm open to the experience! So let's dig into it! :)

### Keyboard/Typing
* There is a system built-in text replacements thing in the keyboard options!! 😃
  The accent tool (hold long for accents) doesn't work there 🤦
  It cannot deal with upper/lower cases 🤦
* Emoji panel seems nice! It's always put at the place where you actually type! 👍:
  * But sometimes the cursor keys don't let you move through the findings? I don't see the pattern yet but the UX is not quite there yet.
  * **FIXED meanwhile**: When you search "apple" it shows you: 'headphones', 'computer mouse' (which is shown as a white upright rectangle that could be anything, so there is no features that make it a computer mouse 🤦 different story tho), 'watch', 'technologist', 'woman technologist', 'man technologist', 'cocktail glass' end of list. no "apple"! 🤦
  There ARE "red apple" and "green apple" among these emojis! But they're not shown.
* There are already Shortcuts set up to convert text to simplified/traditional Chinese! `Ctrl+Option+Shift+Command+C` 🤯
* Home/End keys do nothing on connected keyboard. When set to cmd+left/right they might even interfere with browsing back/forward!!?!?!
  Because it's set to be "smart" about the context: It's only home/end behavior when in a text box otherwise it's browse back/forward 🤦
* Mangling word jump left/right + selection is UTTERLY difficult
* App Shortcuts don't work!? You set it up in Keyboard > Keyboard Shortcuts... > App Shortcuts and then it does absolutely nothing.
  Oh! It's menu-name based!!! 🤦 You type the EXACT menu name and then it does the thing. I'm baffled.
  So that neat Finder feature "Select things, RMB, group into new folder" cannot be put to one of these shortcuts with arbitrary numbers of selected items be cause the number of items is in the menu name and that changes ... 🤦

### Window Management/Display
* I really like the cycle-current-app-windows shortcut `Cmd+\``!
  Doesn't work with fullscreen windows though. They're just left out of the loop 🤦
* There are a lot of window-modal-dialogs and editors. When you want to move the dialog you need to move from the title of the **dimmed out** background window! 🤦
* When going into sleep there's often a loud sound peak crack coming from connected monitor. Sounds really bad :/ 🙅
* Sound volume on a connected monitor cannot be set!!?? 🤦
* When you have an app on full-screen and want to switch apps it slides to the side somehow 🤦 bitte was?
  You can set "Reduce Motion" under `Accessibility > Display`. But ONLY if you explicitly search for it! It's not visible under Display directly! 🤦
* OK when "Reduce Motion" is set it's not yet instant. It now fades and you see the Desktop briefly fading. No option to turn fade time off or to 0??
* Fullscreen apps cannot have floating windows in front of them 🤦
* Scaling can **not** be set per monitor setup. So on my big screen everything would be tiny, so I scale things up. Now when I'm on the laptop only I have to scale it all back down individually!!! 🤦
  * There is "Accessibility > Text Size" but it's not clear what it affects. Clearly the item texts in Finder are immediately scaled but not all and some things differently? 🤔
  * On the "Built-in Display" it shows a couple previews from "Larger Text" to "More Space" but there is a resolution shown underneath. Ehmm why would I want to change the resolution when I'm looking for **scaling**? Like 100%, 125%, 150% ...
* Monitor is turned off randomly. Have to wait a moment, it comes back on and I need **log in** again 😵‍💫
* Display brightness: (one time occurrence so far!) Automatic adjustment veeery slowly turns display black right before me in bright environment 😦


### Finder
* One can setup per folder actions with Apple script!! kinda Nice 👍
* Actually neat Finder feature "Select things, RMB, group into new folder" 👍
* Save dialog:
  * **no autocomplete** when typing the file name in the Finder dialog 🫤
  * you cannot paste a path in there 🤦 because paths are so last millennium ...
* No way of having a full path on TOP of the file browser. No you can have it on the bottom ☝️🤓
* Double-clicking the title bar on a Finder window does NOT maximize it. It shrinks it to the minimal size. 🤦 Making it nice and compact!! It's a feature!!!
* These .dmg-"Installers" [apparently](https://unsung.aresluna.org/as-a-windows-user-its-a-very-surreal-way-to-install-a-program/) are customized Finders  🤯

### Mouse
* **Mouse-Wheel events** are handled completely different. You cannot simply intercept a wheel event with Karabiner and use it with something 🤦
  So by default already there is no ModifierKey+Wheel to turn sizes or Volume up/down.
* Trackpad & Mouse **"Natural scrolling"** cannot be set individually!! 🤦
  Whenever I re-connect my USB-hub I need to goto Settings > Trackpad and toggle "Natural scrolling" to have the mouse wheel act normal 🤦
* No **Double-tap-drag**? I have to **press** the trackpad when I want to drag something? I've got good muscle memory for double-tap-drag from Linux and Windows. You tap twice, hold down on the second tap and can move things. Easy. It feels WAY more lightweight and controllable than clicking through.\
  Seems I just found it! Or did I? Clearly there is nothing under "Trackpad" in the "Point&Click" tab but "Accessibility > Pointer Control" has a "Trackpad Options..." dialog (Of course there is no link between the 2 places). It has a switch for "Use trackpad for dragging" .. ehh DUH!!?! This doesn't affect click-through-dragging with the trackpad of course 🤦 Another combo shows "Without Drag Lock", "With Drag Lock", "Three Finger Drag". The first seems like it would be the thing I'm looking for but things are STILL glued to the pointer after release! AH the first 2 differ by a timeout:
  * **Without Drag Lock**: "Glued to pointer for way too long" and
  * **With Drag Lock**: "Glued to pointer forever"
  Gotcha! 🤦

  The "Three Finger Drag". I'll try that now. It actually feels kinda nice in collab with [ComfortResize](https://github.com/ewerybody/ComfortResize) but it collides with 3-Finger volume control that I have on all the other devices! Darn.
* Laggy or stuck mouse: **Maybe FIXED?** Pretty often when I come back to the mac the (external) mouse takes a moment up to several seconds to respond.
  Apparently this is a know issue 🤦 \ Oooof I just opened up the lid to try the trackpad for a change because I thought that's probably ONLY the evil non-apple mouse here and internal shit will be shiny as always.
  Well, that COMPLETELY got it go bananas. Maybe 10 seconds NO cursor movement at all then some "wait a moment I'm busy popup", then 1 jump every second...
* Click-Drag feels terrible!? **Maybe FIXED?** It's not a lot but maybe not even half a second lag? Eeeuuuhh

## after all ...

I don't mean to hate on the Mac or it's users. I'm quite happy for the machine! It's mostly doing a great job, build quality is as expected top notch, battery lasts for ages, sound is awesome, the keyboard (although I only use it when not home) is absolutely nice...

I'm quite biased tho and some of the prejudgments I had are not completely wiped. The taste is still there that they put most of the energy to keep you within the ecosystem and as soon as you go a little outside, like plugging a non-Apple monitor: shame on you! **You** were **asking** for problems! ;]

Thanks for reading this far! If you have objections, additions or thoughts on this let me know and I'll amend the article accordingly. Also tell me know If you want to stay anonymous or want to be linked.

Eventually for private computing at least I'm looking forward to not rely on any of the proprietary OSs anymore. Expect a roast on "closing the windows" soon :)
