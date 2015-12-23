#!/usr/bin/env python3
from gi.repository import Gtk
import os

class MyWindow(Gtk.Window):

  def __init__(self):
    Gtk.Window.__init__(self, title="Simple Notebook Example")
    self.set_border_width(4)

    self.notebook = Gtk.Notebook()
    self.add(self.notebook)

    # Status (Main) tab
    self.p_list = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    self.p_list.set_border_width(10)
    l_status = Gtk.Label('Config / Add new')
    l_status.set_halign(Gtk.Align.START)
    self.p_list.pack_start(l_status, False, False, 0)
    self.notebook.append_page(self.p_list, Gtk.Label('Status'))

    # Proccess tab
    self.p_list = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    self.p_list.set_border_width(10)
    p = os.popen('docker ps -a')
    line = True
    s_ps = ''
    while line:
      line = p.readline()
      s_ps = s_ps + line
    l_proccess = Gtk.Label(s_ps)
    l_proccess.set_halign(Gtk.Align.START)
    self.p_list.pack_start(l_proccess, False, False, 0)
    self.notebook.append_page(self.p_list, Gtk.Label('Proccess'))

    # Images tab
    self.p_images = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    self.p_images.set_border_width(10)
    p = os.popen('docker images')
    line = True
    images = ''
    while line:
      line = p.readline()
      images = images + line
    l_images = Gtk.Label(images)
    l_images.set_halign(Gtk.Align.START)
    self.p_images.pack_start(l_images, False, True, 0)
    self.notebook.append_page(self.p_images, Gtk.Label('Images'))

    # About tab
    self.p_about = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    self.p_about.set_border_width(10)
    p = os.popen('docker version')
    line = True
    version = ''
    while line:
      line = p.readline()
      version = version + line
    l_version = Gtk.Label(version)
    l_version.set_halign(Gtk.Align.START)
    self.p_about.pack_start(l_version, False, False, 0)
    self.notebook.append_page(self.p_about, Gtk.Label('About'))

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
