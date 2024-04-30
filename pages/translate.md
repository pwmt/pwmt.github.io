title: Localization
description: Help us translating our projects

Both [zathura](/projects/zathura) and [girara](/projects/girara) support
translations as of version 0.1.1. Since we currently only provide German
translation files we need your help to get them translated into other languages.

## Transifex
[transifex](http://transifex.net) is an open source platform for localization
which offers users an easy-to-use interface to submit translations to various
projects hosted on a number of hosting platform types.

All of our projects are available on [transifex](http://transifex.net) and can
be translated smoothly online:

* [girara on transifex](https://www.transifex.net/projects/p/girara/)
* [zathura on transifex](https://www.transifex.net/projects/p/zathura/)

## Manually

If you don't want to signup on [transifex](http://transifex.net), there is
another possibility to help us: At first you have to check out the "develop"
branch of girara or zathura. For girara this is done like this:

    $ git clone https://github.com/pwmt/girara.git
    $ cd girara
    $ git checkout -b develop origin/develop

Then you should run the "update-po" make target to get an up-to-date version of
the PO template and update the existing translations:

    $ make update-po

Now you can have a look at the files in the "po" directory. If you want to
create a new translation, copy the pot file to "$name_of_the_locale.po" and
start working on it. If you want to update an existing translation file just
edit the file.

When you're done please send the file to the mailing list to
[zathura@lists.pwmt.org](mailto:zathura@lists.pwmt.org) for zathura and to
[girara@lists.pwmt.org](mailto:girara@lists.pwmt.org) for girara. You can also
create a bug in our [bug tracker](http://bt.pwmt.org).
