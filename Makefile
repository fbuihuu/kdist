VERSION := $(shell ./kdist --version | sed -e 's/kdist version v//')

RM	= rm -f
TAR	= tar
MAKE	= make
INSTALL = install

KDIST	= kdist

KDIST_SCRIPTS = \
	kdist-project kdist-project--init kdist-config kdist-config--apply \
	kdist-config--diff kdist-config--info kdist--lib kdist--lib-git

KDIST_LIBEXECS = $(KDIST_SCRIPTS)

prefix = /usr/local
bindir = $(prefix)/bin
libexecdir = $(prefix)/libexec/kdist


.PHONY: all install tarbz2-pkg

all:
	@echo "Nothing need to be built."
	@echo "Run 'make install' to complete installation."

install:
	$(INSTALL) -m755 -d $(DESTDIR)$(bindir)
	$(INSTALL) -m755 -d $(DESTDIR)$(libexecdir)
	$(RM) -r $(DESTDIR)$(libexecdir)/*
	$(INSTALL) $(KDIST) $(DESTDIR)$(bindir)
	$(INSTALL) $(KDIST_LIBEXECS) $(DESTDIR)$(libexecdir)
	sed -i  -e "s|^LIBEXECDIR=.*|LIBEXECDIR=$(libexecdir)|" \
		-e "s|^KDIST_VERSION=.*|KDIST_VERSION=v$(VERSION)|" \
		$(DESTDIR)$(bindir)/kdist

TARVERSION = $(VERSION:-dirty=)
TARNAME = $(KDIST)-$(TARVERSION)
tarbz2-pkg:
	@git archive --format=tar --prefix=$(TARNAME)/ HEAD^{tree} > $(TARNAME).tar
	@mkdir -p $(TARNAME)
	@mkdir -p $(TARNAME)/scripts
	@echo v$(TARVERSION) > $(TARNAME)/kdist-version
	@$(TAR) rf $(TARNAME).tar $(TARNAME)/kdist-version
	@$(RM) -r $(TARNAME)
	@bzip2 -9 -f $(TARNAME).tar
	@echo $(TARNAME).tar.bz2

clean:
	$(RM) -r $(TARNAME)
	$(RM) -r $(TARNAME).tar.*
