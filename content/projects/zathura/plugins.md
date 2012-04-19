---
title: Plugins
description: Which document types are supported?
---

Each file type that is supported by zathura is implemented by its own plugin.
Each plugin page gives an overview about the supported file type of it and how
to install it. We are currently developing the following plugins:

* [zathura-pdf-poppler](zathura-pdf-poppler)
* [zathura-pdf-mupdf](zathura-pdf-mupdf)
* [zathura-djvu](zathura-djvu)
* [zathura-ps](zathura-ps)
* [zathura-cb](zathura-cb)

## Plugin functionality

The following table should give an overview about which functionality has been
already implemented in which plugin and which is still missing.

Function                pdf-poppler pdf-mupdf djvu  ps cb
--------                ----------- --------- ----- -- --
Render                  X           X         X     X  X
Search text             X           X         X     -  0
Document information    X           X         -     X  -
Document index          X           X         X     -  -
Select text             X           X         X     -  -
Attachments             X           -         -     -  -
Links                   X           X         -     -  -
Images                  X           -         -     -  -
Save                    X           -         X     X  -

## Development guide
We have written a short guide which explains how to write a new plugin for
zathura. You can find it [here](development).
