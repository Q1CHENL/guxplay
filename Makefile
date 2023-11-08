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
	sudo cp icon.png /usr/share/icons/hicolor/48x48/apps/guxplay-icon.png
	sudo gtk-update-icon-cache /usr/share/icons/hicolor

uninstall:
	sudo rm /usr/local/bin/guxplay
	sudo rm /usr/share/icons/hicolor/48x48/apps/guxplay-icon.png

clean:
	rm -f guxplay
