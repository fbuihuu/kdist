cp arch/arm/boot/zImage %{buildroot}/boot/vmlinuz-%{uname_r}
cp arch/arm/boot/uImage %{buildroot}/boot/uImage-%{uname_r}
cp System.map %{buildroot}/boot/System.map-%{uname_r}
cp .config %{buildroot}/boot/config-%{uname_r}
