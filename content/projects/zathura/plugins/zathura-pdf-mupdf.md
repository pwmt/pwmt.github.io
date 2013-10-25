---
title: zathura-pdf-mupdf
description: PDF support
---

The *zathura-pdf-mupdf* plugin adds PDF support to zathura by using the
[mupdf](http://mupdf.com/) rendering library. *mupdf* has to be built with
*-fPIC* before it can be linked successfully to our plugin. For the latest
version you have to use at least mupdf >= 1.2. If you are using the git version
of *mupdf*, make sure you checkout the *mupdf-git* branch in our plugin
repository.

## Dependencies
* [mupdf](http://mupdf.com/)

## Download

Version  Release Date  SHA-1 Checksum                             Download
-------- ------------  ------------------------------------------ ------------------------------------------------------
0.2.5    2013/10/25    `168a3143ff10d07dc34080661da26b285a1f7d44` [Download](../download/zathura-pdf-mupdf-0.2.5.tar.gz)
0.2.4    2013/05/12    `1d7cb4fd3c07bb009d7d0b08b4bc12065c394ca6` [Download](../download/zathura-pdf-mupdf-0.2.4.tar.gz)
0.2.3    2013/03/18    `8bc711c68fbf53800b2897f5500e00a58b9663f3` [Download](../download/zathura-pdf-mupdf-0.2.3.tar.gz)
0.2.2    2013/01/20    `de565c7a184d3e887c8e02e41fd920fdd81f223f` [Download](../download/zathura-pdf-mupdf-0.2.2.tar.gz)
0.2.1    2012/08/30    `42d0bd2a3ab24b3c61e50faeaa2a25aab842371c` [Download](../download/zathura-pdf-mupdf-0.2.1.tar.gz)
0.2.0    2012/06/09    `299642b224b86494dc9f5f1572c89b185e9f11de` [Download](../download/zathura-pdf-mupdf-0.2.0.tar.gz)
0.1.0    2012/03/09    `9d13a298a73eba12c73ca6de608a3f32fd3d98d8` [Download](../download/zathura-pdf-mupdf-0.1.0.tar.gz)

## Installation
It is recommended to install it from your prefered package manager. Otherwise
you can grab the latest version of the source code from our website and build it
by hand:

    $ tar xfv zathura-pdf-mupdf-<version>.tar.gz
    $ cd zathura-pdf-mupdf-<version>
    $ make
    $ make install

## Known supported distributions
* [Arch Linux](https://www.archlinux.org/packages/community/x86_64/zathura-pdf-mupdf/)
* [Gentoo](http://packages.gentoo.org/package/app-text/zathura-pdf-mupdf)

## Installation (Developer version)
For the installation of the *zathura-pdf-mupdf* plugin follow the
instructions:

    $ git clone git://pwmt.org/zathura-pdf-mupdf.git
    $ cd zathura-pdf-mupdf
    $ git checkout --track -b develop origin/develop
    $ make
    $ make install

## Source code
If you are interested in the source code you can either
[browse](http://git.pwmt.org/?p=zathura-pdf-mupdf.git) it online or clone the
repository:

    $ git clone git://pwmt.org/zathura-pdf-mupdf.git
