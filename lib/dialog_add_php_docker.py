#!/usr/bin/env python3
from gi.repository import Gtk

class DialogAddPhpDocker():
  def __init__(self, parent):
    self.parent = parent

    builder = Gtk.Builder()
    builder.add_from_file("lib/dialog_add_php_docker.glade")
    self.dialog = builder.get_object("dialog_add_php_docker")
    builder.connect_signals(self)

    self.en_local_name = builder.get_object('en_local_name')
    self.en_docker_name = builder.get_object('en_docker_name')
    self.en_path_mount = builder.get_object('en_path_mount')
    self.clear_add_docker_dialog()

  def on_btn_cancel_clicked(self, button):
    self.clear_add_docker_dialog()


  def on_bnt_add_docker_clicked(self, button):
    self.parent.add_docker = {
      self.en_local_name.get_text(): {
        'type': 'PHP',
        'docker_name': self.en_docker_name.get_text(),
        'path_mount': self.en_path_mount.get_text(),
      }
    }
    self.clear_add_docker_dialog()

  def clear_add_docker_dialog(self):
    self.en_local_name.set_text('')
    self.en_docker_name.set_text('{server_name}')
    self.en_path_mount.set_text('{project}/www')

