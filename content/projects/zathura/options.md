---
title: Options
description: Description of all possible options
---

## General settings
This section describes settings concerning the behaviour of zathura

### adjust-open
Defines which auto adjustment mode should be used if a document is loaded.
Possible options are "best-fit" and "width".

* Value-type: String
* Default value: best-fit

### advance-pages-per-row
Defines if the number of pages per row should be honored when advancing a page.

* Value-type: Boolean
* Default value: false


### highlight-color
Defines the color that is used for highlighting parts of the document (e.g.:
show search results)

* Value-type: String
* Default value: #9FBC00

### highlight-active-color
Defines the color that is used to show the current selected highlighted element
(e.g: current search result)

* Value-type: String
* Default value: #00BC00

### highlight-transparency
Defines the opacity of a highlighted element

* Value-type: Float
* Default value: 0.5

### page-padding
The page padding defines the gap in pixels between each rendered page.

* Value-type: Integer
* Default value: 1

### page-store-threshold
Pages that are not visible get unloaded after some time. Every page that has not
been visible for page-store-treshold seconds will be unloaded.

* Value-type: Integer
* Default value: 30

### page-store-interval
Defines the amount of seconds between the check to unload invisible pages.

* Value-type: Integer
* Default value: 30

### pages-per-row
Defines the number of pages that are rendered next to each other in a row.

* Value-type: Integer
* Default value: 1

### recolor
En/Disables recoloring

* Value-type: Boolean
* Default value: false

### recolor-darkcolor
Defines the color value that is used to represent dark colors in recoloring mode

* Value-type: String
* Default value: #FFFFFF

### recolor-lightcolor
Defines the color value that is used to represent light colors in recoloring mode

* Value-type: String
* Default value: #000000

### render-loading
Defines if the "Loading..." text should be displayed if a page is rendered.

* Value-type: Boolean
* Default value: true

### scroll-step
Defines the step size of scrolling by calling the scroll command once

* Value-type: Float
* Default value: 40

### scroll-wrap
Defines if the last/first page should be wrapped

* Value-type: Boolean
* Default value: false

### zoom-max
Defines the maximum percentage that the zoom level can be

* Value-type: Integer
* Default value: 1000

### zoom-min
Defines the minimum percentage that the zoom level can be

* Value-type: Integer
* Default value: 10

### zoom-step
Defines the amount of percent that is zoomed in or out on each comand.

* Value-type: Integer
* Default value: 10

## Girara settings
Most of the options affecting the appearance of zathura are derived from the
options that are offered by our user interface library called girara and can be
found in its [documentation](/projects/girara/options). Those values can also be
set via the *zathurarc* file.
