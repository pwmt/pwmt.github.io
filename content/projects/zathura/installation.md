---
title: installation
description: a document viewer
---

## Installation

### Dependencies
The core of zathura depends on two external libraries,
[girara](http://pwmt.org/projects/girara/), our simplistic user interface
library and [GTK+](http://www.gtk.org/), a cross-platform widget toolkit.
Depending on which filetypes should be supported you are going to need
additional libraries to build those file type plugins.

#### Core dependencies
* [girara](http://pwmt.org/projects/girara/), our simplistic user interface library
* [GTK+](http://www.gtk.org/), a cross-platform widget toolkit

#### Additional dependencies
* [poppler](http://poppler.freedesktop.org/) for PDF support
* [mupdf]<http://mupdf.com/) for PDF support
* [djvulibre](http://djvu.sourceforge.net/) for DjVu support
* [libspectre](http://libspectre.freedesktop.org/) for PostScript support

### Stable version
Since zathura packages are available in many distributions it is recommended to
install it from their with your prefered package manager. Otherwise you can grab
the latest version of the source code from our website and build it by hand::

    $ tar xfv zathura-<version>.tar.gz
    $ cd zathura-<version>
    $ make
    $ make install

### Known supported distributions

* [Arch Linux](http://www.archlinux.org/packages/community/x86_64/zathura)
* [Debian](http://packages.debian.org/en/sid/zathura)
* [Fedora](http://pkgs.org/fedora-rawhide/fedora-i386/zathura-0.0.8.2-4.fc15.i686.rpm.html)
* [Gentoo](http://packages.gentoo.org/package/app-text/zathura)
* [Ubuntu](http://packages.ubuntu.com/maverick/zathura)
* [OpenBSD](http://openports.se/textproc/zathura)

### Developer version
If you are interested in testing the very latest versions with all its new
features, that we are working on, type in the following commands. At first you
have to install the latest version of girara::

    $ git clone git://pwmt.org/girara.git
    $ cd girara
    $ make
    $ make install

After the successful installation of the user interface library, grab the latest
version of zathura and install it::

    $ git clone git://pwmt.org/zathura.git
    $ cd zathura
    $ git checkout --track -b develop origin/develop
    $ make
    $ make install

For the installation of a file type plugin check the :doc:`plugins`
section.
