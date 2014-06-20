title: Example code
description: Blurp


~~~ {.c}
#include <stdio.h>
#include <stdlib.h>

#include <girara/girara.h>

void setting_cb(girara_session_t* session, const char* name,
    girara_setting_type_t type, void* value, void* data)
{
  fprintf(stderr, "Setting '%s' has been changed\n", name);
}

int main(int argc, char *argv[])
{
  gtk_init(&argc, &argv);

  /* create girara session */
  girara_session_t* session = girara_session_create();

  if (session == NULL) {
    return -1;
  }

  if (girara_session_init(session, NULL) == false) {
    girara_session_destroy(session);
    return -1;
  }

  /* enable tabs */
  girara_tabs_enable(session);

  /* create tabs */
  for (unsigned int i = 0; i < 5; i++) {
    /* create widget that should be display in the tab */
    GtkWidget* tab = gtk_text_view_new();
    if (tab == NULL) {
      continue;
    }

    /* add and insert tab */
    gchar* text = g_strdup_printf("Tab %d", i + 1);
    girara_tab_new(session, text, tab, false, NULL);
    g_free(text);
  }

  /* add some settings */
  int test_val_int = 0;
  girara_setting_add(session, "test-val-int", &test_val_int, INT, FALSE, NULL,
      setting_cb, NULL);
  test_val_int = 42;
  girara_setting_set(session, "test-val-int", &test_val_int);

  /* add a statusbar entry */
  girara_statusbar_item_t* item =
    girara_statusbar_item_add(session, TRUE, TRUE, TRUE, NULL);

  if (item != NULL) {
    girara_statusbar_item_set_text(session, item, "girara-left");
  }

  /* parse configuration file */
  girara_config_parse(session, "~/.config/girara/config");

  /* read settings */
  int tmp_val_int = 0;
  if (girara_setting_get(session, "window-width", &tmp_val_int) == true) {
    fprintf(stderr, "Window width: %d\n", tmp_val_int);
  } else {
    fprintf(stderr, "Window width: (not set)\n");
  }


  /* start gtk main loop */
  gtk_main();

  /* clean up */
  girara_session_destroy(session);

  return 0;
}
~~~
