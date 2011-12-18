cp arch/x86/boot/bzImage %{buildroot}/boot/vmlinuz-%{uname_r}
cp System.map %{buildroot}/boot/System.map-%{uname_r}
cp .config %{buildroot}/boot/config-%{uname_r}
