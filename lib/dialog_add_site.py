#!/usr/bin/env python3
from gi.repository import Gtk

class DialogAddSite():
  def __init__(self, parent):
    self.parent = parent

    builder = Gtk.Builder()
    builder.add_from_file("lib/dialog_add_site.glade")
    self.dialog = builder.get_object("dialog_add_site")
    builder.connect_signals(self)

    self.clear_add_dialog()

  def on_btn_cancel_clicked(self, button):
    self.clear_add_dialog()

  def on_btn_add_site_clicked(self, button):
    self.clear_add_dialog()

  def clear_add_dialog(self):
    pass
    #self.bnt_add_site.set_sensitive(False)
