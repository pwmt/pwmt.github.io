---
title: Downloads
description: Get zathura
---

Version  Release Date  SHA-1 Checksum                             Download
-------- ------------  ------------------------------------------ ----------------------------------
0.2.7    2014/02/17    `2c82d9490f0675b7b4897e69b2b53a8c19924cb8` [Download](zathura-0.2.7.tar.gz)
0.2.6    2013/11/24    `d84878388969d523027a1661f49fd29638bd460b` [Download](zathura-0.2.6.tar.gz)
0.2.5    2013/11/08    `ce795ca03140778f442d796a9e807f283a69253a` [Download](zathura-0.2.5.tar.gz)
0.2.4    2013/08/15    `9a11aa7adab7ecdb311bdb477edaf06793552c61` [Download](zathura-0.2.4.tar.gz)
0.2.3    2013/05/12    `cc3cb49f3bc9e7f787773ac7c3db18ca2ff6dce3` [Download](zathura-0.2.3.tar.gz)
0.2.2    2013/01/20    `0aa88b31cf574cb70a1936c317a567a94f680896` [Download](zathura-0.2.2.tar.gz)
0.2.1    2012/08/30    `6d508f8c0e8a4d8e21b7bae815a83abae402e828` [Download](zathura-0.2.1.tar.gz)
0.2.0    2012/06/09    `41310cd103a99d54145b21bf11afa0fdfa740d81` [Download](zathura-0.2.0.tar.gz)
0.1.2    2012/03/24    `11508530f39500cb6863829678eeda3bff2527bc` [Download](zathura-0.1.2.tar.gz)
0.1.1    2012/03/09    `a39044d410e6c9208a795f8eebe9f72b433a54c5` [Download](zathura-0.1.1.tar.gz)
0.1.0    2012/02/21    `d3a6c3233833adb6c678f70e4758a589a4cde4d9` [Download](zathura-0.1.0.tar.gz)
0.0.8.5  2011/11/09    `8d65b964fc80f380cfee5ebe1a7fcbebf38cfbf7` [Download](zathura-0.0.8.5.tar.gz)
0.0.8.4  2011/07/12    `5c0f02181baa555ff2e7ed0f4c68ca2a2a2a5893` [Download](zathura-0.0.8.4.tar.gz)
0.0.8.3  2011/03/24    `8d998ad0defc8d6eabb3da28f6115ce26489d4f4` [Download](zathura-0.0.8.3.tar.gz)
0.0.8.2  2010/11/21    `1abf051341588ab1df30aaf57566b9d8d03f28f7` [Download](zathura-0.0.8.2.tar.gz)
0.0.8.1  2010/07/29    `dda094bcb4a105ce2c6af0d2b5674e924259e539` [Download](zathura-0.0.8.1.tar.gz)
0.0.8    2010/07/28    `573f392bd367d7860888d8b67ad31098eb7afd59` [Download](zathura-0.0.8.tar.gz)
0.0.7    2010/06/21    `89a5216f00b9d6b4581046e82de108081aa87bee` [Download](zathura-0.0.7.tar.gz)
0.0.6    2010/06/06    `fcc5ad94459c468ca942cfb2208453977b6f8369` [Download](zathura-0.0.6.tar.gz)
0.0.5    2010/05/25    `e3845e9d471234f6ad9fa507925531428b778819` [Download](zathura-0.0.5.tar.gz)
0.0.4    2010/05/18    `5eecf06f4ddee253dfad2a7b0a35fe5a26838940` [Download](zathura-0.0.4.tar.gz)
0.0.3    2010/04/11    `4789c92e8c176b56b7e362ae784ff1d421f7d196` [Download](zathura-0.0.3.tar.gz)
0.0.2    2010/02/15    `3a9f3ec99d0354647fdd6558a3135f831cb18162` [Download](zathura-0.0.2.tar.gz)
0.0.1    2009/09/18    `9ba020235b722010e12af3276dcf1c3d702c0410` [Download](zathura-0.0.1.tar.gz)

## Changelog
Here you can view the changes between the different versions:

### 0.2.7 (2014/02/17)
* Full SyncTex support
* D-Bus interface
* Simple vim plugin for SyncTex support
* Add shortcuts for ^C and Esc in all modes
* Use the actual mode in mode toggle calls
* Only copy selected text in normal and fullscreen mode
* Translate error messages
* Correctly safe print setting state
* Add --mode option
* Expose more properties via D-Bus
* Center pages
* Replace glib memory functions with try version
* Align highlighted rectangles correctly
* Implement G and gg for index mode
* Implement TOGGLE for sc_navigate_index
* Preserve horizontal position when scrolling to PAGE_TOP/BOTTOM
* Implement shortcuts for scrolling to page top/bottom
* Set position on document load only if no page was specified
* Bail out early if we get TOP or BOTTOM
* Replace fullscreen mode with presentation mode
* Remove GTK+2 support
* Update documentation
* Updated translations

### 0.2.6 (2013/11/24)
* Update documentation
* Resolve layout problems

### 0.2.5 (2013/11/08)
* Use GTK+3 by default
* Rewritten render logic
* Fixed page refresh in certain situations
* Make the X clipboard buffer
* Allow number in quickmarks
* Workaround for print quality issues
* Update documentation
* Updated translations

### 0.2.4 (2013/08/15)
* Resolve memory leak
* Report missing plugin or unsupported file types
* More vim-like search behaviour
* Introduced show-{h,v}-scrollbar settings
* Enhancement of the jumplist mechanism
* Use jumplists with marks
* More vim-like jump behaviour
* Improved bisect
* Update page number on mouse scroll
* Introduced window-title-page option
* Updated translations

### 0.2.3 (2013/05/17)
* LRU caching algorithm
* Bisect functionality
* Allow negative offsets
* Option --page to open at the specified page
* Scale vertical/horizontal scrolling in respect to the buffer
* Add statusbar-basename option
* Implement colors for 'Loading...'-text
* Don't render same page multiple times
* Use libmagic if available
* Some other bug fixes and updated translations

### 0.2.2 (2013/01/20)
* Implemented jumplist (^o, ^i)
* Update current page when following links
* Scroll horizontally with shift and mouse wheel
* Page aware scrolling
* Synctex forward synchronisation
* Update shortcuts
* Some other bug fixes and updated translations

### 0.2.1 (2012/08/30)
* Syntex backwards synchronisation
* Fix request-page-setup
* Fix window adustment
* Better GTK3 integration
* Added first-page-colum setting
* Added recolor-keephue setting
* Updated translations

### 0.2.0 (2012/06/09)
* New languages
* Better print support
* Improve document links
* Render last-viewed pages with a higher priority
* Export images and attachments
* Open multiple documents
* Plugin manager
* Several memory leaks and small bugs

### 0.1.2 (2012/03/24)
* Add 'open-first-page' setting
* Free invisible pages after specific time
* Set log level via command line
* Update GTK3 support
* Completion for :write command
* Simplified plugin loading
* Allow counter-clockwise rotation
* Changeable page-padding
* Introduced girara version check
* Detect sqlite automatically
* Update window title

### 0.1.1 (2012/03/09)
* Macro to register plugins
* Fix issues with the display of the current page number
* Ability to scroll to the full left or full right border
* Reimplement the render thread with GThreadPool
* Use the correct color to highlight results
* Support to use both database backends
* Additional notifications on errors
* Option to hide hidden directories
* Do not overwrite existing files with :write
* Fix flicker in text selection
* Resolved several memory leaks
* Updated Makefile

### 0.1.0 (2012/02/21)
* Complete rewrite of zathura
* Uses the [girara](/projects/girara) interface library
* [Plugin system](/projects/zathura/plugins) for different document types
* Better [configuration](/projects/zathura/configuration)
* Quickmarks
* and much more

### 0.0.8.5 (2011/11/09)
* Ignoring MOD5 which is used on some keyboards
* Fix scroll_wrap (#52)
* Don’t invert y coordinates (#42)
* Certain memory leaks and other small issues

### 0.0.8.4 (2011/07/12)
* Fixed bookmark handling
* Support :digits
* Save zoom level per file
* Fix backwards searching
* Fix blinking while switching pages
* Fix input issues in fullscreen mode
* Fixed several memory leaks

### 0.0.8.3 (2011/03/24)
* Updated text searching
* Support for poppler >= 0.15
* Fixed print command with multiple arguments
* Fixed GOptionEntries
* Updated Makefile
* Fixed several memory leaks
* Fixed segmentation faults

### 0.0.8.2 (2010/11/21)
* Wrap around scrolling
* Display scroll percentage in statusbar
* More familiar zoom key bindings
* Support reading files from stdin
* Open command with appended current file path
* Following XDG specification
* Colored window and view port
* File reloading fix
* Fixed several memory leaks
* Updated man page
* Updated Makefile

### 0.0.8.1 (2010/07/29)
* Fixed critical usability bug

### 0.0.8 (2010/07/28)
* Improved and fixed completion
* Optional parameters for the print command
* Escape filenames
* Resolved some memory leaks
* Global configuration file
* Specify configuration directory
* Configureable modes
* Smooth scrolling
* Extended statusbar string manipulation
* function
* Strip executable
* Updated manpage

### 0.0.7 (2010/06/21)
* Change window title to filename
* Fixation of the URI command
* Updated the behaviour of sc_scroll
* Half/Full-page scrolling
* Check document health in sc_reload
* tabbed support
* Define look with the set function
* Implemented map function
* zathurarc file
* Prevent buffer overflow in realpath
* Strip executeable
* Key evaluation when buffer is not empty
* Manpage update

### 0.0.6 (2010/06/06)
* Use GFileMonitor instead of inotify
* Added document reload shortcut
* Fixed toggle index
* Fixed print command
* Manpage update

### 0.0.5 (2010/05/25)
* Fullscreen mode
* Correct search result highlighting
* Document password dialog
* Several fixes

### 0.0.4 (2010/05/18)
* Mouse support (Scroll, Mark and copy text to clipboard)
* Keyboard navigation in the index view
* Different goto modes
* Auto adjustment when opening a document
* Escape filenames
* Several fixes

### 0.0.3 (2010/04/11)
* Reload modified document automatically
* Recolor the page instead of inverting the colors
* Working search function
* Show and hide document information
* Follow internal links or open URI in a predefined browser
* Save the document
* Several fixes

### 0.0.2 (2010/02/15)
* Complete new, re-written interface
* Multiple printer support
* Command history
* Show document index
* Centered view
* Add, save and open bookmarks
* Marker support
* Highlight search results
* Buffered commands
* set Function
* Revert video function
* Command completion
