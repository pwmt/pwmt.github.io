title: zathura-cb
description: Comic book support


The *zathura-cb* plugin adds comic book support to zathura.

## Dependencies

* [libarchive](http://www.libarchive.org/)


## Installation
It is recommended to install it from your prefered package manager. Otherwise
you can grab the latest version of the source code from our website and build it
by hand:

    $ tar xfv zathura-cb-<version>.tar.gz
    $ cd zathura-cb-<version>
    $ mkdir build
    $ meson build
    $ cd build
    $ ninja
    $ ninja install

## Known supported distributions
* [Arch Linux](https://aur.archlinux.org/packages/zathura-cb/)
* [Debian](http://packages.debian.org/en/sid/zathura-cb)
* [Gentoo](http://packages.gentoo.org/package/app-text/zathura-cb)

## Installation (Developer version)
For the installation of the *zathura-cb* plugin follow the
instructions:

    $ git clone https://git.pwmt.org/pwmt/zathura-cb.git
    $ cd zathura-cb
    $ git checkout --track -b develop origin/develop
    $ mkdir build
    $ meson build
    $ cd build
    $ ninja
    $ ninja install
