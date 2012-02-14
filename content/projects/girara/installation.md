## Installation

### Dependencies
libgirara depends on [GTK+](http://www.gtk.org/), a cross-platform widget
toolkit. It can be build for gtk2 as well as for gtk3.

* [GTK+](http://www.gtk.org/), a cross-platform widget toolkit

### Stable version
No official version of libgirara has been released yet.

### Developer version
If you are interested to use the current version of libgirara you need to pull
the source from our git repository and build it by hand:

    $ git clone git://pwmt.org/girara.git
    $ make
    $ make install

libgirara is build for gtk2 by default. If you want to build it for gtk3 just
pass the GIRARA_GTK_VERSION argument to make:

    $ make GIRARA_GTK_VERSION=3 install
