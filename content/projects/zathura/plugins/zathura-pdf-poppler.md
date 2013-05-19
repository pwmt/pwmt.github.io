---
title: zathura-pdf-poppler
description: PDF support
---

The *zathura-pdf-poppler* plugin adds PDF support to zathura by using the
[poppler](http://poppler.freedesktop.org) rendering engine.

## Dependencies
* [poppler](http://poppler.freedesktop.org/)

## Download

Version  Release Date  SHA-1 Checksum                             Download
-------- ------------  ------------------------------------------ --------------------------------------------------------
0.2.3    2013/05/12    `24655177e42164cc43863bd313d7633046ff7509` [Download](../download/zathura-pdf-poppler-0.2.3.tar.gz)
0.2.2    2013/01/20    `c2ee47d6cce019e600a553070684d150abb5cc8d` [Download](../download/zathura-pdf-poppler-0.2.2.tar.gz)
0.2.1    2012/08/30    `f0f770e57481f47cb2458a7f9b5fba97b574dd74` [Download](../download/zathura-pdf-poppler-0.2.1.tar.gz)
0.2.0    2012/06/09    `b4d9c97c2a0c7372cfbbbb0b3e54ef63af4eaf95` [Download](../download/zathura-pdf-poppler-0.2.0.tar.gz)
0.1.1    2012/03/09    `6a644127f272c0bbb1582334935a0206ead8e4b9` [Download](../download/zathura-pdf-poppler-0.1.1.tar.gz)
0.1.0    2012/02/21    `3631b4f608f2fc5a856953326e1f48f61f51c173` [Download](../download/zathura-pdf-poppler-0.1.0.tar.gz)

## Installation
It is recommended to install it from your prefered package manager. Otherwise
you can grab the latest version of the source code from our website and build it
by hand:

    $ tar xfv zathura-pdf-poppler-<version>.tar.gz
    $ cd zathura-pdf-poppler-<version>
    $ make
    $ make install

## Known supported distributions
* [Arch Linux](https://www.archlinux.org/packages/community/x86_64/zathura-pdf-poppler/)
* [Debian](http://packages.debian.org/en/sid/zathura)
* [Gentoo](http://packages.gentoo.org/package/app-text/zathura-pdf-poppler)
* [Ubuntu](https://launchpad.net/ubuntu/saucy/+package/zathura)

## Installation (Developer version)
For the installation of the *zathura-pdf-poppler* plugin follow the
instructions:

    $ git clone git://pwmt.org/zathura-pdf-poppler.git
    $ cd zathura-pdf-poppler
    $ git checkout --track -b develop origin/develop
    $ make
    $ make install

## Source code
If you are interested in the source code you can either
[browse](http://git.pwmt.org/?p=zathura-pdf-poppler.git) it online or clone the
repository:

    $ git clone git://pwmt.org/zathura-pdf-poppler.git
