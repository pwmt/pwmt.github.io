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
The page padding defines the gap in pixels between each rendered page and can
not be changed during runtime.

* Value-type: Integer
* Default value: 1

### pages-per-row
Defines the number of pages that are rendered next to each other in a row.

* Value-type: Integer
* Default value: 1

### recolor-dark-color
Defines the color value that is used to represent dark colors in recoloring mode

* Value-type: String
* Default value: #FFFFFF

### recolor-light-color
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
found in its documentation.
