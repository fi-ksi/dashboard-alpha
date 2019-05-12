TARGETS=$(patsubst notebooks/%.ipynb, build/%.html, $(wildcard notebooks/*.ipynb))

all: $(TARGETS)

build/%.html: notebooks/%.ipynb
	./export_monitoring_notebook $< $@

clean:
	rm -rf $(TARGETS)

.PHONY: all clean
