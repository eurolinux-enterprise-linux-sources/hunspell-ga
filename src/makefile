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
RELEASE=4.6
RAWWORDS= gaeilge.raw
LITWORDS= gaeilge.lit dinneenok.txt
ALTWORDS= gaeilge.mor
AFFIXFILE= gaeilge.aff
ALTAFFIXFILE=gaeilgemor.aff
INSTALL_DATA=$(INSTALL) -m 444

SORT=/usr/bin/sort -u

hashtable: $(INSTALLATION).hash

all: gaeilge.hash gaeilgelit.hash gaeilgemor.hash

# grep -v filters out Malmö, São, LC_ALL=C needed!
gaeilge.hash: $(RAWWORDS) $(AFFIXFILE) $(PERSONAL)
	LC_ALL=C $(SORT) $(RAWWORDS) $(PERSONAL) | LC_ALL=C grep -v "[^'a-zA-ZáéíóúÁÉÍÓÚ/-]" | iconv -f utf8 -t iso-8859-1 > gaeilge.focail
	iconv -f utf8 -t iso-8859-1 $(AFFIXFILE) > tempaff.txt
	$(ISPELLBIN)/buildhash gaeilge.focail tempaff.txt gaeilge.hash
	rm -f gaeilge.focail tempaff.txt

gaeilgelit.hash: $(RAWWORDS) $(LITWORDS) gaeilgelit.aff $(PERSONAL)
	LC_ALL=C $(SORT) $(RAWWORDS) $(LITWORDS) $(PERSONAL) | LC_ALL=C grep -v "[^'a-zA-ZáéíóúÁÉÍÓÚ/-]" | iconv -f utf8 -t iso-8859-1 > gaeilge.focail
	iconv -f utf8 -t iso-8859-1 gaeilgelit.aff > tempaff.txt
	$(ISPELLBIN)/buildhash gaeilge.focail tempaff.txt gaeilgelit.hash
	rm -f gaeilge.focail tempaff.txt

gaeilgemor.hash: $(RAWWORDS) $(LITWORDS) $(ALTWORDS) $(ALTAFFIXFILE) $(PERSONAL)
	LC_ALL=C $(SORT) $(RAWWORDS) $(LITWORDS) $(ALTWORDS) $(PERSONAL) | LC_ALL=C grep -v "[^'a-zA-ZáéíóúÁÉÍÓÚ/-]" | iconv -f utf8 -t iso-8859-1 > gaeilge.focail
	iconv -f utf8 -t iso-8859-1 $(ALTAFFIXFILE) > tempaff.txt
	$(ISPELLBIN)/buildhash gaeilge.focail tempaff.txt gaeilgemor.hash
	rm -f gaeilge.focail tempaff.txt

$(ALTAFFIXFILE): $(AFFIXFILE) gaeilgemor.diff
	patch -o gaeilgemor.aff gaeilge.aff < gaeilgemor.diff

# "personal" file used in gramadoir-ga "lexfromdb", that's all
personal: biobla $(PERSONAL)
	sort -u $(PERSONAL) > ./personal
	rm -f $(HOME)/.ispell_$(INSTALLATION)
	LC_ALL=C sort -u biobla | iconv -f utf8 -t iso-8859-1 > $(HOME)/.ispell_$(INSTALLATION)

gaeilgelit.aff: $(AFFIXFILE)
	cp $(AFFIXFILE) gaeilgelit.aff

install: $(INSTALLATION).hash $(INSTALLATION).aff
	$(INSTALL_DATA) $(INSTALLATION).hash $(ISPELLDIR)
	iconv -f utf8 -t iso-8859-1 $(INSTALLATION).aff > tempaff.txt
	$(INSTALL_DATA) tempaff.txt $(ISPELLDIR)/$(INSTALLATION).aff
	rm -f tempaff.txt

installall: gaeilge.hash gaeilgelit.hash gaeilgemor.hash gaeilgelit.aff
	$(INSTALL_DATA) gaeilge.hash $(ISPELLDIR)
	iconv -f utf8 -t iso-8859-1 $(AFFIXFILE) > tempaff.txt
	$(INSTALL_DATA) tempaff.txt $(ISPELLDIR)/$(AFFIXFILE)
	$(INSTALL_DATA) gaeilgelit.hash $(ISPELLDIR)
	iconv -f utf8 -t iso-8859-1 gaeilgelit.aff > tempaff.txt
	$(INSTALL_DATA) tempaff.txt $(ISPELLDIR)/gaeilgelit.aff
	$(INSTALL_DATA) gaeilgemor.hash $(ISPELLDIR)
	iconv -f utf8 -t iso-8859-1 $(ALTAFFIXFILE) > tempaff.txt
	$(INSTALL_DATA) tempaff.txt $(ISPELLDIR)/$(ALTAFFIXFILE)
	rm -f tempaff.txt

clean:
	rm -f *.cnt *.stat *.bak *.tar *.tar.gz *.zip *.tar.bz2 gaeilge sounds.txt repl aspellrev.txt IG2.* EN.temp IG.missp IG.temp IG.temp2 personal accents.txt ga-IE-dictionary.xpi focloiri-gaeilge-*.oxt mimetype SentenceExceptList.xml WordExceptList.xml DocumentList.xml acor_ga-IE.dat validalts.txt

# not giorr, romhanach, etc.  see veryclean
distclean:
	$(MAKE) clean
	rm -f *.hash aspell.txt aspelllit.txt aspellalt.txt ga_IE.dic gaeilgelit.aff $(ALTAFFIXFILE) ga_IE.aff gaelu

#############################################################################
