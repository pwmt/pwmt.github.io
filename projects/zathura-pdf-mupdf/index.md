title: zathura-pdf-mupdf
description: PDF support


The *zathura-pdf-mupdf* plugin adds PDF support to zathura by using the
[mupdf](https://mupdf.com/) rendering library. *mupdf* has to be built with
*-fPIC* before it can be linked successfully to our plugin. For the latest
version you have to use at least mupdf >= 1.16. If you are using the git version
of *mupdf*, make sure you checkout the *mupdf-git* branch in our plugin
repository.

## Dependencies
* [mupdf](https://mupdf.com/)

## Installation
It is recommended to install it from your prefered package manager. Otherwise
you can grab the latest version of the source code from our website and build it
by hand:

    $ tar xfv zathura-pdf-mupdf-<version>.tar.xz
    $ cd zathura-pdf-mupdf-<version>
    $ mkdir build
    $ meson build
    $ cd build
    $ ninja
    $ ninja install

## Known supported distributions
* [Arch Linux](https://www.archlinux.org/packages/community/x86_64/zathura-pdf-mupdf/)
* [Gentoo](https://packages.gentoo.org/package/app-text/zathura-pdf-mupdf)

## Installation (Developer version)
For the installation of the *zathura-pdf-mupdf* plugin follow the
instructions:

    $ git clone https://github.com/pwmt/zathura-pdf-mupdf.git
    $ cd zathura-pdf-mupdf
    $ git checkout --track -b develop origin/develop
    $ mkdir build
    $ meson build
    $ cd build
    $ ninja
    $ ninja install
