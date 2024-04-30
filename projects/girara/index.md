title: girara
description: user interface library

girara is a library that implements a user interface that focuses on simplicity
and minimalism. Currently based on [GTK+](http://www.gtk.org/), a cross-platform
widget toolkit, it provides an interface that focuses on three main components:
A so-called view widget that represents the actual application (e.g. a website
(browser), an image (image viewer) or the document (document viewer)), an input
bar that is used to execute commands of the application and the status bar which
provides the user with current information. girara was designed to replace and
enhance the user interface that is used by zathura and jumanji and other
features that those applications share.

## Wide range of features

* Map certain key bindings to specific functions
* Usage of so-called bufferd commands that allows the user to map whole words
  like *foo* and *bar* to functions
* Respond to mouse events like clicking/releasing of certain buttons, scrolling
  and even mouse movement
* Execute parameterizable commands that can be easily extended with a completion
  function for arguments
* A statusbar that displays up to date information of the application and that
  can handle mouse events
* A complete settings management which allows the storage of certain variables
  that can be configured by built-in commands
* Reasonable default values and functions
* Parsing and evaluation of configuration files
* Useful data structures and utility functions
* Possibility to use tabs
* Support for either GTK2 or GTK3 applications

## Source code

If you are interested in the source code you can either
[browse](http://github.com) it online or clone the repository:

    $ git clone https://github.com/pwmt/girara.git

In addition, a doxygen documentation can be built from the source.
