title: Installation
description: Get it up and running

## Dependencies
The core of zathura depends on two external libraries,
[girara](/projects/girara/), our simplistic user interface
library and [GTK+](https://www.gtk.org/), a cross-platform widget toolkit.
Depending on which filetypes should be supported you are going to need
additional libraries to build those file type plugins.

### Core dependencies
* [girara](/projects/girara/) (>= 2026.01.30)
* [GTK+](https://www.gtk.org/) (>= 4.12)
* [sqlite3](https://www.sqlite.org/)
* libmagic from [file](https://www.darwinsys.com/file/)j
* [json-glib](https://gitlab.gnome.org/GNOME/json-glib)
* [libxxhash](https://xxhash.com/)

### Optional and build dependencies
* [libsynctex](https://launchpad.net/intltool) for SyncTeX support
* [libseccomp](https://docutils.sourceforge.net) for sandbox support
* [librvsg-bin](https://gitlab.gnome.org/GNOME/librsvg) for PNG icons
* [Sphinx](https://www.sphinx-doc.org/) for manpages

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
* [Fedora](https://src.fedoraproject.org/rpms/zathura)
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
