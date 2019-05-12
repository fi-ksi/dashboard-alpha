SOURCES=$(patsubst notebooks/%.ipynb, build/%.html, $(wildcard notebooks/*.ipynb))

all: $(SOURCES)

build/%.html: notebooks/%.ipynb
	./export_monitoring_notebook $< $@

clean:
	rm -rf build/*

git-fetch:
	git fetch origin
	git reset --hard origin/master

kleobis-deploy: clean git-fetch all

.PHONY: all clean kleobis-deploy git-fetch
