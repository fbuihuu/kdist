TAR	?= tar
INSTALL ?= install

prefix ?= /usr/local
sharedir ?= $(prefix)/share/kdist
template_dir ?= $(sharedir)/templates

install:
	$(INSTALL) -m755 -d $(DESTDIR)$(template_dir)
	$(TAR) cf - hooks | $(TAR) -C $(DESTDIR)$(template_dir) -xf -
	$(TAR) cf - mandriva | $(TAR) -C $(DESTDIR)$(template_dir) -xf -
