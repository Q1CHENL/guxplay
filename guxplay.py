import gi
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

# global uxplay process
uxplay = None
icon_path_on = "/usr/share/icons/hicolor/48x48/apps/guxplay-on.png"
icon_path_off = "/usr/share/icons/hicolor/48x48/apps/guxplay-off.png"

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
            uxplay = subprocess.Popen(['uxplay', '-vsync', 'no'])
            indicator.set_icon_full(icon_path_on, "Icon Description")
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
        indicator.set_icon_full(icon_path_off, "Icon Description")


indicator = appindicator.Indicator.new(
    "guxplay",
    icon_path_on,
    appindicator.IndicatorCategory.APPLICATION_STATUS)
indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
indicator.set_menu(menu())
gtk.main()
