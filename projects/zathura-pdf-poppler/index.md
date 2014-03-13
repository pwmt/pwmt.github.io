title: zathura-pdf-poppler
description: PDF support


The *zathura-pdf-poppler* plugin adds PDF support to zathura by using the
[poppler](http://poppler.freedesktop.org) rendering engine.

## Dependencies
* [poppler](http://poppler.freedesktop.org/)

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
* [Fedora](https://admin.fedoraproject.org/pkgdb/acls/name/zathura-pdf-poppler)
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
