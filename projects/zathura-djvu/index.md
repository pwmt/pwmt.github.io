title: zathura-djvu
description: Support for DjVu documents


The *zathura-djvu* plugin adds DjVu support to zathura by using the
[djvulibre](http://djvu.sourceforge.net/) library.

## Dependencies
* [djvulibre](http://djvu.sourceforge.net)

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
