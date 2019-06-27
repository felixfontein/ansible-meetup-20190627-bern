ALL = \
    beamer.pdf
#    print.pdf

all: intermediate $(ALL)

intermediate:
	mkdir -p intermediate

clean:
	rm -f $(ALL)
	rm -rf intermediate

# Presentation
beamer.pdf: source/beamer.tex
	rubber -m pdftex -W all -I source --into intermediate $<
	cp intermediate/beamer.pdf .

#print.pdf: beamer.pdf Makefile
#	qpdf $< --pages $< 1,2,9,10,16,22,34,36,40,44,45,47,50,51,53,57,58,59,61,62,64,69,73,77,82,86,90,112,120,121,123,129 -- $@
