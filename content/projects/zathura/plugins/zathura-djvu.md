---
title: zathura-djvu
description: Support for DjVu documents
---

The *zathura-djvu* plugin adds DjVu support to zathura by using the
[djvulibre](http://djvu.sourceforge.net/) library.

## Dependencies
* [djvulibre](http://djvu.sourceforge.net)

## Download

Version  Release Date  SHA-1 Checksum                             Download
-------- ------------  ------------------------------------------ -------------------------------------------------
0.1.1    2012/03/24    `843e210c615b3b24d49f163b061754d878e67592` [Download](../download/zathura-djvu-0.1.1.tar.gz)
0.1.0    2012/03/09    `a808cddd4fffead3d9c6958de4a1258fbbe40f7e` [Download](../download/zathura-djvu-0.1.0.tar.gz)

## Installation
There are no packages currently available.

## Installation (Developer version)
For the installation of the *zathura-djvu* plugin follow the
instructions:

    $ git clone git://pwmt.org/zathura-djvu.git
    $ cd zathura-djvu
    $ git checkout --track -b develop origin/develop
    $ make
    $ make install

## Source code
If you are interested in the source code you can either
[browse](http://git.pwmt.org/?p=zathura-djvu.git) it online or clone the
repository:

    $ git clone git://pwmt.org/zathura-djvu.git

## Changelog

### 0.1.1 (2012/03/24)
* Fix djvu_document_save_as
