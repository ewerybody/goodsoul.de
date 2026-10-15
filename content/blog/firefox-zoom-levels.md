+++
date = 2026-10-07
title = "Firefox Zoom Levels"
draft = true
[taxonomies]
tags = ["code", "snippet", "browser"]
+++

When you zoom in our out on Firefox the zoom levels are by default a discreet list of percentages: `20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 100%, 110%, 120%, 130%, 140%, 150%, 160%, 170%, 180%, 190%, 200%, 220%, 240%, 260%, 280%, 300%, 400%, 500%`

These are actually listed under `about:config` in an option called `toolkit.zoomManager.zoomValues`:
```
.2,.3,.4,.5,.6,.7,.8,.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.2,2.4,2.6,2.8,3,4,5'
```

Now I wanted a little finer zooming and was too lazy to hack it piece by piece so I looked at the percentages and found that it's 3 ranges that we could loop through:
```py
>>> d = ((20, 200, 10), (200, 300, 20), (300, 550, 100))
>>> print(','.join(f'{str(i/100).lstrip('0').rstrip('.0')}' for s in d  for i in range(*s)))
.2,.3,.4,.5,.6,.7,.8,.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.2,2.4,2.6,2.8,3,4,5
```

So when you do that with a little higher frequency like
```py
>>> d = ((20, 200, 5), (200, 300, 10), (300, 550, 50))
>>> print(','.join(f'{str(i/100).lstrip('0').rstrip('.0')}' for s in d  for i in range(*s)))
.2,.25,.3,.35,.4,.45,.5,.55,.6,.65,.7,.75,.8,.85,.9,.95,1,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75,1.8,1.85,1.9,1.95,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.5,4,4.5,5
```
