---
title: Installation
description: How to install girara on your system
---

## Dependencies
libgirara depends on [GTK+](http://www.gtk.org/), a cross-platform widget
toolkit. It can be build for gtk2 as well as for gtk3.

### Core dependencies
* [GTK+](http://www.gtk.org/), a cross-platform widget toolkit

### Optional and build dependencies
* [intltool](https://launchpad.net/intltool), utility scripts for internationalization
* [check](http://check.sourceforge.net/), a unit testing framework for C

## Stable version
Since girara packages are available in many distributions it is recommended to
install it from there with your prefered package manager. Otherwise you can grab
the latest version of the source code from our website and build it by hand:

    $ tar xfv girara-<version>.tar.gz
    $ cd girara-<version>
    $ make
    $ make install

## Known supported distributions

* [Arch Linux](http://www.archlinux.org/packages/community/x86_64/girara)
* [Debian](http://packages.debian.org/en/source/experimental/girara)
* [Gentoo](http://packages.gentoo.org/package/dev-libs/girara)

## Developer version
If you are interested to use the current version of libgirara you need to pull
the source from our git repository and build it by hand:

    $ git clone git://pwmt.org/girara.git
    $ make
    $ make install
