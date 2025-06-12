+++
date = 2024-02-26
title = "uptpy - Compact Python FTP Uploader"
[taxonomies]
tags = ["code", "blog", "py", "web", "projects"]
+++
Finally I made this public! `uptpy` now has it's own GitHub project:

> [github.com/ewerybody/uptpy](https://github.com/ewerybody/uptpy)

# ok but why?
So, I built a [HUGO](https://gohugo.io) site for friends and had them host the code on GitHub. They could make changes on the `.md` files, commit and Voilà: The page was updated ... soon ... ish. Initially I set up some Github Action that used a suggested FTP project. The action was building with HUGO, checking out the FTP project from github, have it compile itself somehow and use it to push the public contents. All in all this took about 2 minutes!!
Well, having some XP with Python, FTP, manifest files and hashes I hacked something together. Couldn't be too hard, could it? I added a first draft to the site code, wired it up in Github actions. Slashing down the (usual) update time to about 10 seconds!

# ok but how?

Looking into the GitHub Actions logs with the first standard FTP-uploader script it spent most of the time:
* checking out the tool from github
* compiling it somehow
* uploading **everything** each time

So, needing to checkout the project anyway and having access to Python on the Actions instance already: that slashed down the first 2 points!
Of course: You'd need to add the python script to your project. (I should look into making it use `pip` and or checking out via GitHub Actions in the future.) and the script needs to be happy with built-in Python stuff. (That I'm not really having a problem with :) I really like vanilla stuff.)

Then: When the uploads happen through this very uploader all the time, we can know **what** was uploaded last time and check against the locally build files without scanning remotely. `uptpy` now downloads the remote manifest first, builds a local manifest and check against it sieving out anything that's already up-to-date and enabling deletions!! (well, only of files that once have been uploaded with `uptpy`, otherwise they're left in peace)

# ok but now?

I listed already some [issues](https://github.com/ewerybody/uptpy/issues). There is a fun one that I'm suspecting is either due to my ISPs FTP space or actually a Python issue: Remote file listing encoding! You can provide a type of encoding when creating the connection with the Python FTP module. There are a couple supported modes and one helps with emojis in filenames and the other with something else strange. Thing is:
if you'd have a filename with BOTH: no file listing whatsoever! 🤯

