# Makefile ispell-gaeilge
# INSTALLATION=gaeilgemor
# INSTALLATION=gaeilgelit
INSTALLATION=gaeilge
ISPELLDIR=/usr/lib/ispell
ISPELLBIN=/usr/bin
INSTALL=/usr/bin/install
SHELL=/bin/sh
MAKE=/usr/bin/make
PERSONAL=aitiuil daoine eachtar gall giorr gno logainm miotas.txt romhanach stair.txt

#   Shouldn't have to change anything below here
RELEASE=4.4
RAWWORDS= gaeilge.raw
LITWORDS= gaeilge.lit
ALTWORDS= gaeilge.mor
AFFIXFILE= gaeilge.aff
ALTAFFIXFILE=gaeilgemor.aff
INSTALL_DATA=$(INSTALL) -m 444

SORT=/usr/bin/sort -u

hashtable: $(INSTALLATION).hash

all: gaeilge.hash gaeilgelit.hash gaeilgemor.hash

gaeilge.hash: $(RAWWORDS) $(AFFIXFILE) $(PERSONAL)
	$(SORT) $(RAWWORDS) $(PERSONAL) | LC_ALL=C grep -v "[^'a-zA-ZáéíóúÁÉÍÓÚ/-]" > gaeilge.focail
	$(ISPELLBIN)/buildhash gaeilge.focail $(AFFIXFILE) gaeilge.hash
#	rm -f gaeilge.focail

gaeilgelit.hash: $(RAWWORDS) $(LITWORDS) gaeilgelit.aff $(PERSONAL)
	$(SORT) $(RAWWORDS) $(LITWORDS) $(PERSONAL) | LC_ALL=C grep -v "[^'a-zA-ZáéíóúÁÉÍÓÚ/-]" > gaeilge.focail
	$(ISPELLBIN)/buildhash gaeilge.focail gaeilgelit.aff gaeilgelit.hash
	rm -f gaeilge.focail

gaeilgemor.hash: $(RAWWORDS) $(LITWORDS) $(ALTWORDS) $(ALTAFFIXFILE) $(PERSONAL)
	$(SORT) $(RAWWORDS) $(LITWORDS) $(ALTWORDS) $(PERSONAL) | LC_ALL=C grep -v "[^'a-zA-ZáéíóúÁÉÍÓÚ/-]" > gaeilge.focail
	$(ISPELLBIN)/buildhash gaeilge.focail $(ALTAFFIXFILE) gaeilgemor.hash
	rm -f gaeilge.focail

$(ALTAFFIXFILE): $(AFFIXFILE) gaeilgemor.diff
	patch -o gaeilgemor.aff gaeilge.aff < gaeilgemor.diff

personal: biobla $(PERSONAL)
	LC_ALL=ga_IE sort -u $(PERSONAL) > ./personal
	rm -f $(HOME)/.ispell_$(INSTALLATION)
	LC_ALL=ga_IE sort -u biobla > $(HOME)/.ispell_$(INSTALLATION)

gaeilgelit.aff: $(AFFIXFILE)
	cp $(AFFIXFILE) gaeilgelit.aff

install: $(INSTALLATION).hash $(INSTALLATION).aff
	$(INSTALL_DATA) $(INSTALLATION).hash $(ISPELLDIR)
	$(INSTALL_DATA) $(INSTALLATION).aff $(ISPELLDIR)

installall: gaeilge.hash gaeilgelit.hash gaeilgemor.hash gaeilgelit.aff
	$(INSTALL_DATA) gaeilge.hash $(ISPELLDIR)
	$(INSTALL_DATA) $(AFFIXFILE) $(ISPELLDIR)
	$(INSTALL_DATA) gaeilgelit.hash $(ISPELLDIR)
	$(INSTALL_DATA) gaeilgelit.aff $(ISPELLDIR)
	$(INSTALL_DATA) gaeilgemor.hash $(ISPELLDIR)
	$(INSTALL_DATA) $(ALTAFFIXFILE) $(ISPELLDIR)

clean:
	rm -f *.cnt *.stat *.bak *.tar *.tar.gz *.full gaeilge sounds.txt ga.cwl repl aspellrev.txt IG2.* EN.temp IG.missp IG.temp IG.temp2 personal accents.txt

distclean:
	$(MAKE) clean
	rm -f *.hash aspell.txt aspelllit.txt aspellalt.txt ga_IE.dic gaeilgelit.aff $(ALTAFFIXFILE) ga_IE.aff gaelu giorr

#############################################################################
