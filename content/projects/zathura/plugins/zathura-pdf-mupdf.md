---
title: zathura-pdf-mupdf
description: PDF support
---

The *zathura-pdf-mupdf* plugin adds PDF support to zathura by using the
[mupdf](http://mupdf.com/) rendering library. *mupdf* has to be built with
*-fPIC* before it can be linked successfully to our plugin. You have to use at
least version 0.8.165. If you are using the git version of *mupdf*, make sure
you checkout the *mupdf-git* branch in our plugin repository.

## Dependencies
* [mupdf](http://mupdf.com/)

## Download

Version  Release Date  SHA-1 Checksum                             Download
-------- ------------  ------------------------------------------ ------------------------------------------------------
0.1.0    2012/03/09    `9d13a298a73eba12c73ca6de608a3f32fd3d98d8` [Download](../download/zathura-pdf-mupdf-0.1.0.tar.gz)

## Installation
There are no packages currently available.

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
