.PHONY: all clean

all: guxplay

guxplay: 
	echo '#!/usr/bin/env python3' > guxplay
	cat guxplay.py >> guxplay
	chmod +x guxplay

clean:
	rm -f guxplay
