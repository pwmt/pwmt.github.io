---
title: zathura
description: a document viewer
---

zathura is a highly customizable and functional document viewer. It provides a
minimalistic and space saving interface as well as an easy usage that mainly
focuses on keyboard interaction.

![zathura](img/zathura.png)

## Main features
zathura has a lot of different features where some of them are described in the
following paragraphs:

### Choose your supported file formats
You only want to view PDF documents? How about PostScript or DjVu? All together?
zathura now uses a [plugin](plugins) based system for supported document types
which makes it possible for you to choose which file formats you want your
version of zathura to support. This also makes it possible to use different
backends for the same document type: For instance we provide a plugin for PDF
documents using either the poppler or the mupdf library.

![Multiple file formats](img/fileformat.png)

### Mouse-free navigation
zathura makes it possible to completely view and navigate through different
documents without using a mouse. Functions to scroll or zoom are mapped to
certain keys as well as the possibility to follow or open links that are shown
in the document. By simply pressing the "f" key on your keyboard, zathura
highlights all links shown on the current screen. By typing one of the shown
numbers you can easily follow links to chapters or open them with your favourite
web browser. But of course... you still can use the mouse as well.

![Follow links](img/follow.png)

### Automatic document reloading
Whenever the file that you are currently looking at changes (e.g.: you are
working heavily on a LaTeX document and you compile it to view the changes),
zathura automatically detects that and reloads the document without any
hesitation.

![Automatic document reloading](img/latex.png)

### Quickmarks and bookmarks
Whenever you want to find a certain page of the document later on you can use
bookmarks which are saved by using the command ":bmark". You can easily move to
your saved bookmarks with the ":blist" command or delete them with ":bdelete".
Or you can simply use quickmarks. A quickmark is simply a page assigned to a
letter or number and can therefore saved or opened with only two key presses. To
create a new quickmark just type "m" followed by a letter or number. To view a
saved quickmark just use "'" and then the previously used letter or number.

![Save and open bookmarks](img/bookmarks.png)

## Other features

* Export images and attachments
* Open encrypted documents
* Print whole documents or just specific sites
* Search the document
* Show and browse the document index
* Display document information
* Optional [sqlite](http://sqlite.org) database backend
* Support for [tabbed](http://tools.suckless.org/tabbed)

## Source code
If you are interested in the source code you can either
[browse](http://git.pwmt.org) it online or clone the repository:

    $ git clone git://pwmt.org/zathura.git

In addition a doxygen documentation is [available](doxygen).
