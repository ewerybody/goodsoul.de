+++
date = 2023-12-29
title = "goodsoul blog 4.0"
[taxonomies]
tags = ["blog", "bla", "web"]
+++

Yes, this is already the 4th installment of this website. And it's been 23 years since it all started! 😮
Emojis were not a thing already and like them almost any fancy looks had to be hacked together with gifs. Darn, even transparency was a problem and dedicated hacks for certain browsers (well, Internet Explorer mostly) were pretty common.

After all this time I am not even a web-geek! I know .. ehmm, better I can teach myself what I need to know for the problem in front of me in the moment and forget about it asap. So this here is my little experience with it :]

### a **little** timeline

1. `2001-2006` • hand crafted HTML frame jungle as a 'DJ friends calendar page' with "blog" notes.\
2. `2007-2008` • [Movable Type](https://movabletype.org) php blog thing.
3. `2008-2023` • [Wordpress](https://wordpress.org) with tailored design (which broke somewhen, ).
4. `2024-...` • Staticly generated from md-files with [Zola](https://getzola.org).

### Why **now** Zola?

🤷 I don't know. First off, there was no way it would have been anything else than **static**. I have some experience with [Hugo](https://gohugo.io) now. It's alright. I don't love the documentation. But guess [I'm not alone there](https://news.ycombinator.com/item?id=30527884).

After spending some time with it now: [the Zola-Docs](https://getzola.org/documentation/content/section/) aren't uber great either. For once I think the VS Code tooling for HUGO came a long way and Zola might be behind. I mean if the IDE helps you with most of the things you might not need to look up website-documentation at all!

For more there is [Tera](https://keats.github.io/tera/) ... eh whut now?! 🧐 Well, Zola is built upon it. And **you need to know that**! Otherwise you end up scratching your head why there is no info in the Zola docs about simple things such as [for loops](https://keats.github.io/tera/docs/#for)

### Blog TODO:
- [x] main page with last few articles
- [x] article list with dates on home page and all posts list
- [x] tags
- [x] mobile not properly working well, on mobile! (according <meta> was missing)
- [x] bold slab font broken on mobile safari? (not used font variable name thoroughly)
- [x] all links work relatively
- [ ] code style
    - [x] snippet
    - [ ] block syntax highlighting
- [ ] article layout
    - [x] title on top
    - [x] background box
    - [x] meta on top right
    - [x] link to github repo
    - [x] title ~~md~~ html-stylable
- [ ] have `page.title` in head-title (not only `config.title`)
- [ ] cookies
  - [ ] floater
  - [ ] recipie page
- [x] Center stuff properly
    - [x] article
    - [x] nav
    - [x] mobile view
- [x] external links with icons
- [x] what to put in the footer
    - [x] build with Zola - date ?
- [x] have it upload to FTP via [uptpy](https://github.com/ewerybody/uptpy)


### some resources used

* [Realtime Colors](https://realtimecolors.com/blog-post?colors=c7c7c7-0c0b14-3560ed-0d0f35-05ff93&fonts=Zilla%20Slab-Noto%20Sans) - colors and font picking. I like these videos from [Juxtopposed on YouTube](https://youtube.com/@juxtopposed). Apparently they do more than just smartshitting and meme bombing social-media-videos. They have actually real good working things!
* [Aligning items in a flex container - developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Aligning_Items_in_a_Flex_Container) [and](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_box_alignment) - Good old Mozilla docs! This stuff is developing way too quick for me to stay on top.
* [Hermit Zola](https://github.com/VersBinarii/hermit_zola) & [archie-zola](https://github.com/XXXMrG/archie-zola) - for looking into zola code about the tags
* [Wolfgang's blog notthebe.ee](https://notthebe.ee) [code](https://github.com/notthebee/notthebe.ee) - for simplicity and more Zola examples
* [Ryan Dahl's blog](https://tinyclouds.org), [Andy Sloane aka a1k0n](https://www.a1k0n.net) and [Floh's Brain Dump](https://floooh.github.io) for their ultra simplicity
* [Fireship.io](https://fireship.io), [Pixelfed](https://pixelfed.org) and [fediverse](https://jointhefediverse.net/?lang=en-us) for some style/look and feel

### old site links

Don't know if I really want to publish? Maybe screenshots?
* [1.0](https://goodsoul.de/_private/_old_site/main.html) HTML 1.0
* [2.0](https://goodsoul.de/goodsoul/archives.html) movable type archive
* [3.0](https://goodsoul.de/wp) last wordpress
* [4.0](https://goodsoul.de) current
