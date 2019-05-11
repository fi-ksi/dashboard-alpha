SOURCES=$(patsubst notebooks/%.ipynb, build/%.html, $(wildcard notebooks/*.ipynb))

all: $(SOURCES)

build/%.html: notebooks/%.ipynb
	./export_monitoring_notebook $< $@

clean:
	rm -rf build/*

.PHONY: all clean
