title: Installation
description: How to install girara on your system

## Dependencies
libgirara depends on [GTK+ 3](https://www.gtk.org/), a cross-platform widget
toolkit.

### Core dependencies

* [GTK+](https://www.gtk.org/), a cross-platform widget toolkit

## Stable version
Since girara packages are available in many distributions it is recommended to
install it from there with your prefered package manager. Otherwise you can grab
the latest version of the source code from our website and build it by hand:

    $ tar xfv girara-<version>.tar.xz
    $ cd girara-<version>
    $ mkdir build
    $ meson build
    $ cd build
    $ ninja
    $ ninja install

## Known supported distributions

* [Arch Linux](https://www.archlinux.org/packages/community/x86_64/girara)
* [Debian](https://packages.debian.org/en/source/unstable/girara)
* [OpenSUSE](https://software.opensuse.org/package/girara)
* [Gentoo](https://packages.gentoo.org/package/dev-libs/girara)
* [MacPorts](https://www.macports.org/ports.php?by=name&substr=girara)

## Developer version
If you are interested to use the current version of libgirara you need to pull
the source from our git repository and build it by hand:

    $ git clone https://github.com/pwmt/girara.git
    $ cd girara
    $ git checkout --track -b develop origin/develop
    $ mkdir build
    $ meson build
    $ cd build
    $ ninja
    $ ninja install
