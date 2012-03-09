---
title: Downloads
description: Get zathura 
---

Version  Release Date  SHA-1 Checksum                             Download 
-------- ------------  ------------------------------------------ ----------------------------------
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
