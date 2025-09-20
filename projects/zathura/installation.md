title: Installation
description: Get it up and running

## Dependencies
The core of zathura depends on two external libraries,
[girara](/projects/girara/), our simplistic user interface
library and [GTK+](https://www.gtk.org/), a cross-platform widget toolkit.
Depending on which filetypes should be supported you are going to need
additional libraries to build those file type plugins.

### Core dependencies
* [girara](/projects/girara/), our simplistic user interface library (>= 0.2.9)
* [GTK+](https://www.gtk.org/), a cross-platform widget toolkit (>= 3.22)

### Optional and build dependencies
* [sqlite3](https://www.sqlite.org/), a SQL database engine
* [intltool](https://launchpad.net/intltool), utility scripts for internationalization
* [check](https://check.sourceforge.net/), a unit testing framework for C
* libmagic from [file](https://www.darwinsys.com/file/), a file type guesser
* [docutils](https://docutils.sourceforge.net), documentation utilities

## Stable version
Since zathura packages are available in many distributions it is recommended to
install it from there with your prefered package manager. Otherwise you can grab
the latest version of the source code from our website and build it by hand:

    $ tar xfv zathura-<version>.tar.xz
    $ cd zathura-<version>
    $ mkdir build
    $ meson build
    $ cd build
    $ ninja
    $ ninja install

## Known supported distributions

* [Arch Linux](https://www.archlinux.org/packages/community/x86_64/zathura)
* [Debian](https://packages.debian.org/en/sid/zathura)
* [Fedora](https://pkgs.org/fedora-rawhide/fedora-i386/zathura-0.0.8.5.fc17.i686.rpm.html)
* [Gentoo](https://packages.gentoo.org/package/app-text/zathura)
* [Ubuntu](https://packages.ubuntu.com/precise/zathura)
* [openSUSE](https://software.opensuse.org/package/zathura)
* [OpenBSD](https://openports.se/textproc/zathura)
* [MacPorts](https://www.macports.org/ports.php?by=name&substr=zathura)
* [Source Mage](https://mirror.sobukus.de/files/sourcemage/codex/test/doc/zathura/)

## Developer version
If you are interested in testing the very latest versions with all its new
features, that we are working on, type in the following commands. At first you
have to install the latest version of girara:

    $ git clone https://github.com/pwmt/girara.git
    $ cd girara
    $ git checkout --track -b develop origin/develop
    $ mkdir build
    $ meson build
    $ cd build
    $ ninja
    $ ninja install

After the successful installation of the user interface library, grab the latest
version of zathura and install it:

    $ git clone https://github.com/pwmt/zathura.git
    $ cd zathura
    $ git checkout --track -b develop origin/develop
    $ mkdir build
    $ meson build
    $ cd build
    $ ninja
    $ ninja install

For the installation of a file type plugin check the [plugins](../plugins) section.
