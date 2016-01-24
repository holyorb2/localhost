#!/usr/bin/env python3
from gi.repository import Gtk

class DialogAddSite():
  def __init__(self, parent):
    self.parent = parent

    builder = Gtk.Builder()
    builder.add_from_file("lib/dialog_add_site.glade")
    self.dialog = builder.get_object("dialog_add_site")
    builder.connect_signals(self)

    self.btn_add_site = builder.get_object('btn_add_site')
    self.btn_edit_site = builder.get_object('btn_edit_site')
    self.en_site_name = builder.get_object('en_site_name')
    self.cb_docker_db = builder.get_object('cb_docker_db')
    self.cb_docker_php = builder.get_object('cb_docker_php')

    list_db = Gtk.ListStore(int, str)
    list_php = Gtk.ListStore(int, str)
    list_db.append([0, "Select an Item:"])
    list_php.append([0, "Select an Item:"])
    i_db = 1
    i_php = 1
    for docker_name in self.parent.conf['dockers']:
      if self.parent.conf['dockers'][docker_name]['type'] == 'PHP':
        list_php.append([i_php, docker_name])
        i_php += 1
      elif self.parent.conf['dockers'][docker_name]['type'] == 'DB':
        list_db.append([i_db, docker_name])
        i_db += 1

    self.cb_docker_php.set_model(list_php)
    self.cell = Gtk.CellRendererText()
    self.cb_docker_php.pack_start(self.cell, True)
    self.cb_docker_php.add_attribute(self.cell, 'text', 1)
    self.cb_docker_php.set_active(0)

    self.cb_docker_db.set_model(list_db)
    self.cell = Gtk.CellRendererText()
    self.cb_docker_db.pack_start(self.cell, True)
    self.cb_docker_db.add_attribute(self.cell, 'text', 1)
    self.cb_docker_db.set_active(0)

    self.clear_add_dialog()


  def on_btn_cancel_clicked(self, button):
    self.clear_add_dialog()

  def on_btn_add_site_clicked(self, button):
    self.parent.add_site = {
      self.en_site_name.get_text().strip(): {
        'docker_db': self.cb_docker_db.get_model()[self.cb_docker_db.get_active()][1],
        'docker_php': self.cb_docker_php.get_model()[self.cb_docker_php.get_active()][1],
      }
    }
    self.clear_add_dialog()

  def on_btn_edit_site_clicked(self, button):
    pass

  def on_entry_changed(self, entry):
    self.dialog_button_status(self.dialog_validate())

  def on_cb_changed(self, widget):
    self.dialog_button_status(self.dialog_validate())

  def dialog_validate(self):
    if self.en_site_name.get_text().strip() == '':
      return False
    if self.cb_docker_db.get_active() == 0 or self.cb_docker_php.get_active() == 0:
      return False
    return True

  def dialog_button_status(self, status=False):
    self.btn_add_site.set_sensitive(status)
    self.btn_edit_site.set_sensitive(status)

  def clear_add_dialog(self):
    self.en_site_name.set_text('')
    self.dialog_button_status()
    self.cb_docker_php.set_active(0)
    self.cb_docker_db.set_active(0)
