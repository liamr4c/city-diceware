all: cities.txt cities.txt.xz
cities.txt: cities1000.txt
	./csv-to-list.py
cities.txt.xz: cities.txt
	xz -e -9 cities.txt -k 
cities1000.txt: cities1000.zip
	unzip cities1000.zip
cities1000.zip:
	wget http://download.geonames.org/export/dump/cities1000.zip
clean:
	rm cities1000.zip
	rm cities1000.txt
clean-all: clean
	rm cities.txt
	rm cities.txt.xz
.PHONY: clean clean-all all xz
