title: Configuration
description: Customize jumanji


The customization of jumanji is be managed via a configuration file called
*jumanjirc*. By default jumanji will evaluate the following files:

* */etc/jumanjirc*
* *$XDG_CONFIG_HOME/jumanji/jumanjirc*

The *jumanjirc* file is a simple plain text file that can be populated with
various commands to change the behaviour and the look of jumanji which we are
going to describe in the following subsections. Each line (besides empty lines
and comments (which start with a prepended *\#*) is evaluated on its own, so it
is not possible to write multiple commands in one single line.

## set - Changing options
In addition to the build-in *:set* command jumanji offers more options to be
changed and makes those changes permanent. To overwrite an option you just have
to add a line structured like the following

    set <option> <new value>

The *option* field has to be replaced with the name of the option that should be
changed and the *new value* field has to be replaced with the new value the
option should get. The type of the value can be one of the following:

* INT - An integer number
* FLOAT - A floating point number
* STRING - A character string
* BOOL - A boolean value ("true" for true, "false" for false)

In addition we advice you to check the options to get a more detailed view of
the options that can be changed and which values they should be set to.

The following example should give some deeper insight of how the *set* command
can be used

    set option1 5
    set option2 2.0
    set option3 hello
    set option4 hello\ world
    set option5 "hello world"

## map - Mapping a shortcut
It is possible to map or remap new key bindings to shortcut functions which
allows a high level of customization. The *:map* command can also be used in
the *jumanjirc* file to make those changes permanent:

    map [mode] <binding> <shortcut function> <argument>

### Mode
The *map* command expects several arguments where only the *binding* as well as
the *shortcut-function* argument is required. Since jumanji uses several modes
it is possible to map bindings only for a specific mode by passing the *mode*
argument which can take one of the following values:

* normal (default)
* visual
* insert
* index

The brackets around the value are mandatory.

#### Single key binding
The (possible) second argument defines the used key binding that should be
mapped to the shortcut function and is structured like the following. On the one
hand it is possible to just assign single letters, numbers or signs to it:

    map a shortcut_function
    map b shortcut_function
    map c shortcut_function
    map 1 shortcut_function
    map 2 shortcut_function
    map 3 shortcut_function
    map ! shortcut_function
    map ? shortcut_function

#### Using modifiers
It is also possible to use modifiers like the *Control* or *Alt* button on the
keyboard. It is possible to use the following modifiers:

* A - *Alt*
* C - *Control*
* S - *Shift*

Now it is required to define the *binding* with the following structure:

    map <A-a> shortcut_function
    map <C-a> shortcut_function

#### Special keys
jumanji allows it also to assign keys like the space bar or the tab button which
also have to be written in between angle brackets. The following special keys
are currently available:

Identifier  Description
-  --
BackSpace   *Back space*
CapsLock    *Caps lock*
Esc         *Escape*
Down        *Arrow down*
Up          *Arrow up*
Left        *Arrow left*
Right       *A7row right*
F1          *F1*
F2          *F2*
F3          *F3*
F4          *F4*
F5          *F5*
F6          *F6*
F7          *F7*
F8          *F8*
F9          *F9*
F10         *F10*
F11         *F11*
F12         *F12*
PageDown    *Page Down*
PageUp      *Page Up*
Return      *Return*
Space       *Space*
Super       *Windows button*
Tab         *Tab*

Of course it is possible to combine those special keys with a modifier. The
usage of those keys should be explained by the following examples:

    map <Space> shortcut_function
    map <C-Space> shortcut_function

#### Mouse buttons
It is also possible to map mouse buttons to shortcuts by using the following
special keys:

Identifier  Description
-  -
Button1     *Mouse button 1*
Button2     *Mouse button 2*
Button3     *Mouse button 3*
Button4     *Mouse button 4*
Button5     *Mouse button 5*

They can also be combined with modifiers:

    map <Button1> shortcut_function
    map <C-Button1> shortcut_function

#### Buffer commands
If a mapping does not match one of the previous definition but is still a valid
mapping it will be mapped as a buffer command:

    map abc quit
    map test quit

#### Shortcut functions
The following shortcut functions can be mapped:

Function           Description
--  
focus_inputbar     *Focus inputbar*
goto_homepage      *Goto homepage*
goto_parent_dir    *Goto parent dir of current URL*
navigate_history   *Navigate through the history*
put                *Open URL from clipboard*
quit               *Quit jumanji*
reload             *Reload current page*
restore            *Restore closed tab(s)*
scroll             *Scroll*
show_source        *Show source code of current site*
yank               *Copy current URL to clipboard*
zoom               *Zoom*

#### Pass arguments
Some shortcut function require or have optional arguments which influence the
behaviour of them. Those can be passed as the last argument:

    map <C-i> zoom in
    map <C-o> zoom out

Possible arguments are:

* bottom
* default
* down
* full-down
* full-up
* half-down
* half-up
* in
* left
* next
* out
* previous
* right
* specific
* top
* up
* best-fit
* width

### unmap - Removing a shortcut
In addition to mapping or remaping custom key bindings it is possible to remove
existing ones by using the *:unmap* command. The command is used in the
following way (the explanation of the parameters is described in the *map*
section of this document

    unmap [mode] <binding>
