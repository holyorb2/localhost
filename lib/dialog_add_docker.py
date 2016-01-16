#!/usr/bin/env python3
from gi.repository import Gtk

class DialogAddDocker():
  def __init__(self, parent):
    self.parent = parent

    builder = Gtk.Builder()
    builder.add_from_file("lib/dialog_add_docker.glade")
    self.dialog = builder.get_object("dialog_add_docker")
    builder.connect_signals(self)

    self.en_local_name = builder.get_object('en_local_name')
    self.en_docker_db_name = builder.get_object('en_docker_db_name')
    self.en_db_mount = builder.get_object('en_db_mount')
    self.en_db_user = builder.get_object('en_db_user')
    self.en_db_base = builder.get_object('en_db_base')
    self.en_db_pass = builder.get_object('en_db_pass')
    self.en_docker_php_name = builder.get_object('en_docker_php_name')
    self.en_php_mount = builder.get_object('en_php_mount')
    self.clear_add_docker_dialog()

  def on_btn_cancel_clicked(self, button):
    self.clear_add_docker_dialog()

  def on_bnt_add_docker_clicked(self, button):
    # if len(self.conf['dockers']) == 0 or self.en_local_name.get_text() not in self.conf['dockers']:
    #   self.conf['dockers'][self.en_local_name.get_text()] = {
    #     'repo_name': self.en_repo_name.get_text(),
    #     'addon_param': self.en_addon_param.get_text(),
    #     'mount_path': self.en_mount_path.get_text()
    #   }
    #   with open(self.conf_path + '/docker.yml', 'w') as f_conf:
    #     f_conf.write(yaml.dump(self.conf, default_flow_style=False))
    self.clear_add_docker_dialog()

  def clear_add_docker_dialog(self):
    self.en_local_name.set_text('')
    self.en_docker_db_name.set_text('{project}-db')
    self.en_db_mount.set_text('{project}/mysql')
    self.en_db_user.set_text('{project}')
    self.en_db_base.set_text('{project}')
    self.en_db_pass.set_text('{project}')
    self.en_docker_php_name.set_text('{project}-php')
    self.en_php_mount.set_text('{project}/www')

