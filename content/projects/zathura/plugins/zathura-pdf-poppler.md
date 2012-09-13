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
0.2.1    2012/08/30    `f0f770e57481f47cb2458a7f9b5fba97b574dd74` [Download](../download/zathura-pdf-poppler-0.2.1.tar.gz)
0.2.0    2012/06/09    `b4d9c97c2a0c7372cfbbbb0b3e54ef63af4eaf95` [Download](../download/zathura-pdf-poppler-0.2.0.tar.gz)
0.1.1    2012/03/09    `6a644127f272c0bbb1582334935a0206ead8e4b9` [Download](../download/zathura-pdf-poppler-0.1.1.tar.gz)
0.1.0    2012/02/21    `3631b4f608f2fc5a856953326e1f48f61f51c173` [Download](../download/zathura-pdf-poppler-0.1.0.tar.gz)

## Installation
There are no packages currently available.

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

## Changelog

### 0.1.1 (2012/03/09)
* Return error if document could not be saved
* Use correct free function
* Update Makefile
* Use PLUGIN_REGISTER macro to register plugin
* Check the minim required version of zathura
