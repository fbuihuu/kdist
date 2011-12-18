VERSION := $(shell ./kdist --version | sed -e 's/kdist version v//')

RM	= rm -f
TAR	= tar
MAKE	= make
INSTALL = install

KDIST	= kdist

KDIST_LIBEXECS = $(wildcard kdist-*)

prefix = /usr/local
bindir = $(prefix)/bin
sharedir = $(prefix)/share/kdist
libexecdir = $(prefix)/libexec/kdist
template_dir = $(sharedir)/templates

export DESTDIR INSTALL RM TAR prefix template_dir


.PHONY: all install tarbz2-pkg

all:
	@echo "Nothing need to be built."
	@echo "Run 'make install' to complete installation."

install:
	$(INSTALL) -m755 -d $(DESTDIR)$(bindir)
	$(INSTALL) -m755 -d $(DESTDIR)$(libexecdir)
	$(INSTALL) $(KDIST) $(DESTDIR)$(bindir)
	$(INSTALL) $(KDIST_LIBEXECS) $(DESTDIR)$(libexecdir)
	$(MAKE) -C templates install
	sed -i  -e "s|^LIBEXECDIR=.*|LIBEXECDIR=$(libexecdir)|" \
		-e "s|^TEMPLATEDIR=.*|TEMPLATEDIR=$(template_dir)|" \
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
