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
0.2.3    2013/05/12    `6a69c495a3afd94c407d5127d5a133d15d2b40b6` [Download](../download/zathura-djvu-0.2.3.tar.gz)
0.2.2    2013/01/20    `825489e94cd8f882c38cc4820f9d76d4a1825c73` [Download](../download/zathura-djvu-0.2.2.tar.gz)
0.2.1    2012/08/30    `a690bd9b0e7c60107b29b70f808d1246277853de` [Download](../download/zathura-djvu-0.2.1.tar.gz)
0.2.0    2012/06/09    `03f257c29fb03f7609300e227ce7d95dba0fa4af` [Download](../download/zathura-djvu-0.2.0.tar.gz)
0.1.1    2012/03/24    `843e210c615b3b24d49f163b061754d878e67592` [Download](../download/zathura-djvu-0.1.1.tar.gz)
0.1.0    2012/03/09    `a808cddd4fffead3d9c6958de4a1258fbbe40f7e` [Download](../download/zathura-djvu-0.1.0.tar.gz)

## Installation
It is recommended to install it from your prefered package manager. Otherwise
you can grab the latest version of the source code from our website and build it
by hand:

    $ tar xfv zathura-djvu-<version>.tar.gz
    $ cd zathura-djvu-<version>
    $ make
    $ make install

## Known supported distributions
* [Arch Linux](https://www.archlinux.org/packages/community/x86_64/zathura-djvu/)
* [Debian](http://packages.debian.org/en/sid/zathura-djvu)
* [Fedora](https://admin.fedoraproject.org/pkgdb/acls/name/zathura-djvu)
* [Gentoo](http://packages.gentoo.org/package/app-text/zathura-djvu)
* [Ubuntu](https://launchpad.net/ubuntu/saucy/+package/zathura-djvu)

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
