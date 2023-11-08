import os
import gi
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

# global uxplay process
uxplay = None

def main():
    indicator = appindicator.Indicator.new(
        "guxplay",
        "/usr/share/icons/hicolor/48x48/apps/guxplay-icon.png",
        appindicator.IndicatorCategory.APPLICATION_STATUS)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(menu())

    gtk.main()

def menu():
    menu = gtk.Menu()
    on = gtk.CheckMenuItem(label='On')
    off = gtk.CheckMenuItem(label='Off')
    quit = gtk.MenuItem(label='Quit')
    
    off.connect('activate', uxplay_off, on)
    on.connect('activate', uxplay_on, off)
    quit.connect('activate', exit)
    on.set_active(True)
    uxplay_on(on, off)
    
    menu.append(on)
    menu.append(off)
    menu.append(quit)

    menu.show_all()
    return menu

# messy logic but works LMAO
def uxplay_on(source, off):
    global uxplay
    if source.get_active():
        if uxplay is None:
            uxplay = subprocess.Popen(['uxplay'])
            if off.get_active():
                off.set_active(False)
    else:
        if uxplay is not None:
            source.set_active(True)
            
        

def uxplay_off(source, on):
    global uxplay
    if source.get_active():
        stop()
        if on.get_active():
            on.set_active(False)
    else:
        if uxplay is None:
            source.set_active(True)
    
# exit the app
def exit(source):
    stop()
    gtk.main_quit()

# stop the process uxplay    
def stop():
    global uxplay
    if uxplay: 
        uxplay.terminate()
        uxplay = None
    


if __name__ == "__main__":
    main()
