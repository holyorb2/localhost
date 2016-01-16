#!/usr/bin/env python3
from gi.repository import Gtk
import os, time, yaml
import os.path

from lib.dialog_add_docker import DialogAddDocker


class DockerHost:
  conf_path = 'tmp'  #FIXME add preferences
  conf = {
    'dockers': {}
  }
  d_tabs = {
    #'Status': '',
    'Proccess': 'ps -a',
    'Images': 'images',
    'Info': 'version'
  }

  def __init__(self):
    if os.path.isfile(self.conf_path + '/docker.yml'):
      with open(self.conf_path + '/docker.yml', 'r') as f_conf:
        self.conf = yaml.load(f_conf)
    #else:
    #FIXME create directory, check permitions, create file

    self.builder = Gtk.Builder()
    self.builder.add_from_file('lib/window.glade')
    self.builder.connect_signals(self)

    self.window = self.builder.get_object('window_main')
    self.about_dialog = self.builder.get_object('dialog_about')

    self.en_local_name = self.builder.get_object('en_local_name')
    self.en_repo_name = self.builder.get_object('en_repo_name')
    self.en_addon_param = self.builder.get_object('en_addon_param')
    self.en_mount_path = self.builder.get_object('en_mount_path')

    self.lab_status = self.builder.get_object('lab_status')
    self.box_status = self.builder.get_object('box_status')

    self.statusbar = self.builder.get_object('status_bar')
    self.context_id = self.statusbar.get_context_id('status')

    self.notebook = self.builder.get_object('notebook1')
    self.on_notebook1_switch_page(self.notebook, '', 0)

    self.window.show()

    #FIXME self.add_site_dialog = self.builder.get_object('dialog_add_site')
    self.add_docker_dialog = DialogAddDocker(self)


  def on_window_main_destroy(self, object, data=None):
    #FIXME quit with cancel
    Gtk.main_quit()

  def on_gtk_quit_activate(self, menuitem, data=None):
    #FIXME "quit from menu"
    Gtk.main_quit()

  def on_gtk_about_activate(self, menuitem, data=None):
    self.response = self.about_dialog.run()
    self.about_dialog.hide()

  def on_gtk_add_docker_activate(self, menuitem, data=None):
    self.response = self.add_docker_dialog.dialog.run()
    self.add_docker_dialog.dialog.hide()

  def on_gtk_add_site_activate(self, menuitem, data=None):
    #FIXME
    self.response = self.add_site_dialog.run()
    self.add_site_dialog.hide()

  def on_notebook1_switch_page(self,  notebook, page, page_num, data=None):
    tab_content = notebook.get_nth_page(page_num)
    name_label = notebook.get_tab_label(tab_content).get_label()

    if name_label in self.d_tabs:
      tab_content.set_halign(Gtk.Align.START)
      tab_content.set_text(self.get_docker_command(self.d_tabs[name_label]))
    elif name_label == 'Status':
      count_dockers = len(self.conf['dockers'])
      self.lab_status.set_halign(Gtk.Align.START)
      self.lab_status.set_text('Count of dockers - {0}'.format(count_dockers))

      children = self.box_status.get_children()
      for child in children:
        child.destroy()
      if count_dockers:
        box_row = Gtk.Box(spacing=6)
        self.box_status.pack_start(box_row, False, False, 0)

        label = Gtk.Label()
        label.set_text('Docker 1')
        label.set_justify(Gtk.Justification.LEFT)
        box_row.pack_start(label, True, True, 0)

        switch = Gtk.Switch()
        box_row.pack_end(switch, False, False, 0)

        button = Gtk.Button.new_with_label('Edit')
        #button.connect("clicked", self.on_click_me_clicked)
        box_row.pack_end(button, True, True, 0)

    self.statusbar.push(0, "Refreshed - {0}".format(time.ctime()))

  def get_docker_command(self, command):
    output = ''
    p = os.popen('docker ' + command)
    line = True
    while line:
      line = p.readline()
      output = output + line
    return output


if __name__ == "__main__":
  main = DockerHost()
  Gtk.main()
