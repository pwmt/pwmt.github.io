---
title: Installation
description:  
---

## Dependencies
jumanji depends on several external libraries, 
[girara](http://pwmt.org/projects/girara), our simplistic user interface library and
[GTK+](http://www.gtk.org/), a cross-platform widget toolkit and
[webkitgtk](http://webkitgtk.org/), the web rendering engine for GTK+.

* [girara](http://pwmt.org/projects/girara/), our simplistic user interface library
* [GTK+](http://www.gtk.org/), a cross-platform widget toolkit
* [webkitgtk](http://webkitgtk.org/), a web rendering engine for GTK+
* [libsoup](http://live.gnome.org/libsoup/), a http client/server library

## Stable version
No official version of jumanji has been released yet.

## Developer version
If you are interested to use the current version of jumanji you need to pull
the source from our git repository and build it by hand::

    $ git clone git://pwmt.org/jumanji.git
    $ make
    $ make install

## Developer version (based on girara)
If you are interested in testing the very latest versions with all its new
features, that we are working on, type in the following commands. At first you
have to install the latest version of girara::

    $ git clone git://pwmt.org/girara.git
    $ cd girara
    $ make GIRARA_GTK_VERSION=3
    $ make GIRARA_GTK_VERSION=3 install

Right now it is also possible to use the GTK2 version of girara with the jumanji
code. If you want to use that you have to update the *config.mk* file
accordingly.

After the successful installation of the user interface library, grab the latest
version of jumanji and install it::

    $ git clone git://pwmt.org/jumanji.git
    $ cd jumanji
    $ git checkout --track -b develop origin/develop
    $ make
    $ make install
