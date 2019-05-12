TARGETS=$(patsubst notebooks/%.ipynb, build/%.html, $(wildcard notebooks/*.ipynb))

all: $(TARGETS)

build/%.html: notebooks/%.ipynb
	ksi-py3-venv/bin/python3 export_monitoring_notebook $< $@

clean:
	rm -rf $(TARGETS)

.PHONY: all clean
