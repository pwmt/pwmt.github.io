---
title: Plugins
description: Which documents are supported?
---

## Plugins
Each file type that is supported by zathura is implemented by its own plugin.
This section should give an overview about the supported file types of zathura
and how to install them.

### PDF
For the support of PDF documents we are developing two plugins which differ on
the backend they are using. Notice that it is only possible to run one plugin
for one file type at the time:

#### zathura-pdf-poppler
The *zathura-pdf-poppler* plugin adds PDF support to zathura by using the
[poppler](http://poppler.freedesktop.org) rendering engine.

##### Dependencies
* [poppler](http://poppler.freedesktop.org/)

##### Installation (Developer version)
For the installation of the *zathura-pdf-poppler* plugin follow the
instructions:

    $ git clone git://pwmt.org/zathura-pdf-poppler.git
    $ cd zathura-pdf-poppler
    $ make
    $ make install

#### zathura-pdf-mupdf
The *zathura-pdf-mupdf* plugin adds PDF support to zathura by using the
[mupdf](http://mupdf.com/) rendering library. *mupdf* has to be built with
*-fPIC* before it can be linked successfully to our plugin. You have to use at
least version 0.8.165. If you are using the git version of *mupdf*, make sure
you checkout the *mupdf-git* branch in our plugin repository.

##### Dependencies
* [mupdf](<http://mupdf.com/)

##### Installation (Developer version)
For the installation of the *zathura-pdf-mupdf* plugin follow the
instructions:

    $ git clone git://pwmt.org/zathura-pdf-mupdf.git
    $ cd zathura-pdf-mupdf
    $ make
    $ make install

### DjVu
The *zathura-djvu* plugin adds DjVu support to zathura by using the
[djvulibre](http://djvu.sourceforge.net/) library.

#### Dependencies
* [djvulibre](http://djvu.sourceforge.net)

#### Installation (Developer version)
For the installation of the *zathura-djvu* plugin follow the
instructions:

    $ git clone git://pwmt.org/zathura-djvu.git
    $ cd zathura-djvu
    $ make
    $ make install

### PostScript
The *zathura-ps* plugin adds PostScript support to zathura by using the
[libspectre](http://libspectre.freedesktop.org/) library.

#### Dependencies
* [libspectre](http://libspectre.freedesktop.org/)

#### Installation (Developer version) 
For the installation of the *zathura-ps* plugin follow the
instructions:

    $ git clone git://pwmt.org/zathura-ps.git
    $ cd zathura-ps
    $ make
    $ make install
