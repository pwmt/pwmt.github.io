title: Configuration
description: Customize jumanji


## General settings
This section describes settings concerning the behaviour of jumanji

### auto-set-proxy
Defines if the proxy should be set while initializing jumanji

* Value-type: Boolean
* Default value: True

### close-window-with-last-tab
Defines if the jumanji window should be closed when the last tab has been closed

* Value-type: Boolean
* Default value: True

### download-command
The default download command that gets executed whenever a file should be
downloaded

* Value-type: String
* Default value: -

### download-dir
The default download directory

* Value-type: String
* Default value: ~/dl

### homepage
The page padding defines the home page that is loaded by default

* Value-type: String
* Default value: http://pwmt.org

### scroll-step
Defines the amount of pixels that are scrolled on each step:

* Value-type: Integer
* Default value: 40

### zoom-step
Defines the amount of percent that is zoomed in or out on each comand.

* Value-type: Integer
* Default value: 10

## Girara settings
Most of the options affecting the appearance of zathura are derived from the
options that are offered by our user interface library called girara and can be
found in its [documentation](/projects/girara/options). Those values can also be
set via the *zathurarc* file.
