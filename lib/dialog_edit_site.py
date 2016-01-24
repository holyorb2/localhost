#!/usr/bin/env python3
from gi.repository import Gtk

class DialogEditSite():
  def __init__(self, parent):
    self.parent = parent

    builder = Gtk.Builder()
    builder.add_from_file("lib/dialog_edit_site.glade")
    self.dialog = builder.get_object("dialog_edit_site")
    builder.connect_signals(self)

    self.en_site_name = builder.get_object('en_site_name')
    self.en_php_name = builder.get_object('en_php_name')
    self.en_php_image = builder.get_object('en_php_image')
    self.en_php_mount = builder.get_object('en_php_mount')
    self.en_db_name = builder.get_object('en_db_name')
    self.en_db_image = builder.get_object('en_db_image')
    self.en_db_mount = builder.get_object('en_db_mount')
    self.en_db_user = builder.get_object('en_db_user')
    self.en_db_base = builder.get_object('en_db_base')
    self.en_db_pass = builder.get_object('en_db_pass')
    self.sw_site_status = builder.get_object('sw_site_status')
    self.btn_edit_site = builder.get_object('btn_edit_site')

    self.clear_dialog()

  def on_entry_changed(self, entry):
    self.dialog_button_status(self.dialog_validate())

  def on_cb_changed(self, widget):
    self.dialog_button_status(self.dialog_validate())

  def on_btn_cancel_clicked(self, button):
    self.clear_dialog()

  def on_btn_edit_site_clicked(self, button):
    self.clear_dialog()

  def dialog_validate(self):
    return False

  def clear_dialog(self):
    if len(self.parent.add_site):
      site_name = self.parent.add_site.keys()[0]
      docker_php = self.parent.add_site[site_name]['docker_php']
      docker_db = self.parent.add_site[site_name]['docker_db']

      self.en_site_name.set_text(site_name)
      self.en_php_name.set_text(docker_php)
      self.en_php_image.set_text(self.parent.conf['dockers'][docker_php]['docker_name'])
      self.en_php_mount.set_text(self.parent.conf['dockers'][docker_php]['path_mount'])
      self.en_db_name.set_text(docker_db)
      self.en_db_image.set_text(self.parent.conf['dockers'][docker_db]['docker_name'])
      self.en_db_mount.set_text(self.parent.conf['dockers'][docker_db]['path_mount'])
      self.en_db_user.set_text(self.parent.conf['dockers'][docker_db]['db_user'])
      self.en_db_base.set_text(self.parent.conf['dockers'][docker_db]['db_base'])
      self.en_db_pass.set_text(self.parent.conf['dockers'][docker_db]['db_db_pass'])
      #self.sw_site_status  #FIXME
