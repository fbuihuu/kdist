%files -n %{name}
%defattr (-, root, root)
/boot/vmlinuz-%{uname_r}
/boot/System.map-%{uname_r}
/boot/config-%{uname_r}
/lib/modules/%{uname_r}
