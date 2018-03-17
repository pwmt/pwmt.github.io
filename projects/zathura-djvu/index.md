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
    $ mkdir build
    $ meson build
    $ cd build
    $ ninja
    $ ninja install

## Known supported distributions
* [Arch Linux](https://www.archlinux.org/packages/community/x86_64/zathura-djvu/)
* [Debian](http://packages.debian.org/en/sid/zathura-djvu)
* [Fedora](https://admin.fedoraproject.org/pkgdb/acls/name/zathura-djvu)
* [Gentoo](http://packages.gentoo.org/package/app-text/zathura-djvu)
* [Ubuntu](https://launchpad.net/ubuntu/saucy/+package/zathura-djvu)

## Installation (Developer version)
For the installation of the *zathura-djvu* plugin follow the
instructions:

    $ git clone https://git.pwmt.org/pwmt/zathura-djvu.git
    $ cd zathura-djvu
    $ git checkout --track -b develop origin/develop
    $ mkdir build
    $ meson build
    $ cd build
    $ ninja
    $ ninja install
