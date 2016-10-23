SVGs=$(wildcard *.svg)
PDFs=$(SVGs:.svg=.pdf)

images : $(PDFs) $(PNGs)

%.pdf : %.svg
	inkscape -z --export-pdf=$@ $<
