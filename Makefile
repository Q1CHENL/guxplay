.PHONY: all clean

all: guxplay

guxplay: 
	echo '#!/usr/bin/env python3' > guxplay
	cat guxplay.py >> guxplay
	chmod +x guxplay

install:
	echo '#!/usr/bin/env python3' > guxplay
	cat guxplay.py >> guxplay
	chmod +x guxplay
	sudo install -Dm755 guxplay /usr/local/bin/guxplay
	sudo cp assets/icon-on.png /usr/share/icons/hicolor/48x48/apps/guxplay-on.png
	sudo cp assets/icon-off.png /usr/share/icons/hicolor/48x48/apps/guxplay-off.png
	sudo gtk-update-icon-cache /usr/share/icons/hicolor

uninstall:
	sudo rm /usr/local/bin/guxplay
	sudo rm /usr/share/icons/hicolor/48x48/apps/guxplay-on.png
	sudo rm /usr/share/icons/hicolor/48x48/apps/guxplay-off.png

clean:
	rm -f guxplay
