title: Usage
description: 


## User scripts
jumanji supports user scripts from sites like
[userscripts.org](https://userscripts.org) which are used to modify and
customize the behaviour, functionality and look of certain websites. Those
scripts are loaded automatically when the according website has been opened.

To use those scripts you just have to download and save them into your
*~/.config/jumanji/scripts/* directory.

## Adblocking
jumanji supports [adblock plus](https://adblockplus.org) filter lists that can
be downloaded from the [subscriptions](https://adblockplus.org/en/subscriptions)
website of adblock plus.

To use a filter list you just have to download and save them into your
*~/.config/jumanji/adblock/* directory and jumanji will read and parse them
automatically on startup.

## Downloads
To download files with jumanji you can either use the internal download manager
(which has not been implemented by now) or define a custom command
(*download-command*) that is spawned whenever a file should be downloaded. In
addition you can define the default download directory (*download-dir*) in your
jumanjirc.::

    set download-dir ~/dl
    set download-command "wget %s -O %s"

The first place holder will be replaced by the url that should be downloaded.
The second is optional and will be replaced by a concatenation of the download
dir and the filename.

## Flash support (for GTK3 version)
It is possible to use flash with the gtk3 version by installing
*nspluginwrapper* and the *lib32-flashplugin* package. After running::

    $ nspluginwrapper -i /usr/lib32/mozilla/plugins/libflashplayer.so

flash support should be available.

## Hide scrollbars in GTK+-3.0
Since the 'show-scrollbars' option will not have any effect with GTK+-3.0 you
can add the following to your `~/.config/gtk-3.0/gtk.css` file:

    #jumanji GtkScrollbar {
      -GtkRange-slider-width: 0;
      -GtkRange-trough-border: 0;
    }
