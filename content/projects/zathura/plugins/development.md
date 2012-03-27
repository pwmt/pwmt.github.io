---
title: Plugin development
description: Write your own plugin
---

This guide should give a short introduction in the way zathura's plugin system
works and how you can write your own plugin and let zathura use it.

## Introduction

### Plugin system
zathura's plugin system is quite simple. At startup zathura searches through a
specified directory for shared objects and tries to load them as plugins. Each
plugin has to register itself by a name, its version, a special function as well
as its supported mimetypes to zathura. After the registration of the plugin
zathura will automatically use it to open files with the previous defined
mimetypes. That's it.

### A plugin
Each plugin has to implement a basic set of functionality so that it can be used
in a meaningful way with zathura. For instance it would not make any sense if
the plugin was not able to render any page at all. On the contrary the export of
images out of the document might not be considered as that important.

We have predefined a certain set of functionality that a plugin can have and
that can be used by zathura if it has been implemented by the plugin. When a
plugin is loaded, zathura calls a certain function that the plugin __must
implemented__ in order to work correctly. This function gets a data structure
which has to be filled with function pointers by the plugin, which are then used
by the main application.

## Example - A minimalistic PDF plugin
In this section we are going to develop a simplified version of the
[zathura-pdf-poppler](../zathura-pdf-poppler) plugin. For the sake of simplicity
we are not discussing the build process of the plugin because we would recommend
you to adapt our Makefiles from existing plugins. In addition we avoid most of
the error handling that should be implemented.

### Register the plugin
As previously described each plugin has to register itself to zathura so that it
can be used properly. Therefore we have introduced a macro called
*PLUGIN_REGISTER* which expects several parameters:

* Plugin name *The name of the plugin*
* Major version *The plugins major version*
* Minor version *The plugins minor version*
* Revision *The plugins revision*
* Open function *The open function*
* Mimetypes *A character array of supported mime types*

In our case we are going to register our plugin "my plugin" with its version
1.0.1, the register function *register_function* and the list of supported
mimetypes.

~~~ {.c}
PLUGIN_REGISTER(
  "my plugin",
  0, 1, 0,
  register_functions,
  PLUGIN_MIMETYPES({
    "application/pdf"
  })
)
~~~

This macro will automatically generate among others a function called *plugin_register* which is
used to register the plugin to zathura when it has been loaded.

### Register the plugin functions
In our macro we have defined that the function *register_functions* is used to
install our functions which will implement a certain functionality in the
struct:

~~~ {.c}
void
register_functions(zathura_document_functions_t* functions)
{
  functions->document_open     = pdf_document_open;
  functions->document_free     = pdf_document_free;
  functions->page_init         = pdf_page_init;
  functions->page_clear        = pdf_page_clear;
  functions->page_render_cairo = pdf_page_render_cairo;
}
~~~

We are now going to give a short overview about the used functions in the above
code snippet. For a complete documentation you should checkout the documentation
of [zathura_document_functions_t](../../doxygen). A document instance consists
out of a *zathura_document_t* document object that contains information about
the document itself and a defined number of *zathura_page_t* page objects. There
are several functions defined for those two types and they have to be
implemented by the plugin. For our simple plugin which will only be capable of
rendering a page we will need one function that is capable of opening the PDF
document and setting up all necessary objects for further usage and one function
which will clean up all the allocated objects afterwards. In addition we need
two of those functions for page objects as well and one function that will
actually implement the rendering process.

### Open and closing a document
The first thing we have to do when opening a document is to initialize all
necessary objects and values that we are going to need for the future use of the
plugin. Therefore we have to implement our *pdf_document_open* function:

~~~ {.c}
zathura_error_t
pdf_document_open(zathura_document_t* document)
{
  /* get path and password */
  char* path     = zathura_document_get_path(document);
  char* password = zathura_document_get_password(document);

  /* create poppler document */
  char* uri = g_filename_to_uri(path, NULL, NULL);
  PopplerDocument* poppler_document = poppler_document_new_from_file, uri, password, NULL);
  g_free(uri);

  if (poppler_document == NULL) {
    return ZATHURA_ERROR_UNKNOWN;
  }

  /* save poppler document for further usage */
  zathura_document_set_data(document, poppler_document);

  /* get number of pages */
  unsigned int number_of_pages = poppler_document_get_n_pages(poppler_document);
  zathura_document_set_number_of_pages(document, number_of_pages);

  return ZATHURA_ERROR_OK;
}
~~~

To open the document we retrieve the *path* and the optional *password* of the
document to create an instance of *PopplerDocument* which represents a document
in the poppler library. If this fails for any reason (e.g.: the path does not
exist, the user provided the incorrect password) we tell zathura that this
function failed for an unknown reason. If we are lucky we continue and save the
created *poppler_document* object in the custom data field of the document so
that we can access it later on. After that we determine the number of pages that
the document contains so that zathura can initialize every single page.

Since we have allocated the *poppler_document* object we have to make sure that
its resources will be freed when it is no longer needed. This happens in our
*pdf_document_free* function:

~~~ {.c}
zathura_error_t
pdf_document_free(zathura_document_t* document)
{
  if (document == NULL) {
    return ZATHURA_ERROR_INVALID_ARGUMENTS;
  }

  PopplerDocument* poppler_document = zathura_document_get_data(document);
  if (poppler_document != NULL) {
    g_object_unref(poppler_document);
  }

  return ZATHURA_ERROR_OK;
}
~~~
