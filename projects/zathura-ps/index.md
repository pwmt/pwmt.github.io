title: zathura-ps
description: PostScript support


The *zathura-ps* plugin adds PostScript support to zathura by using the
[libspectre](http://libspectre.freedesktop.org/) library.

## Dependencies
* [libspectre](http://libspectre.freedesktop.org/)

## Installation
It is recommended to install it from your prefered package manager. Otherwise
you can grab the latest version of the source code from our website and build it
by hand:

    $ tar xfv zathura-ps-<version>.tar.gz
    $ cd zathura-ps-<version>
    $ make
    $ make install

## Known supported distributions
* [Arch Linux](https://www.archlinux.org/packages/community/x86_64/zathura-ps/)
* [Debian](http://packages.debian.org/en/sid/zathura-ps)
* [Fedora](https://admin.fedoraproject.org/pkgdb/acls/name/zathura-ps)
* [Gentoo](http://packages.gentoo.org/package/app-text/zathura-ps)
* [Ubuntu](https://launchpad.net/ubuntu/saucy/+package/zathura-ps)

## Installation (Developer version)
For the installation of the *zathura-ps* plugin follow the
instructions:

    $ git clone git://pwmt.org/zathura-ps.git
    $ cd zathura-ps
    $ git checkout --track -b develop origin/develop
    $ make
    $ make install

## Source code
If you are interested in the source code you can either
[browse](http://git.pwmt.org/?p=zathura-ps.git) it online or clone the
repository:

    $ git clone git://pwmt.org/zathura-ps.git
