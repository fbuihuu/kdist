%files -n %{name}
%defattr (-, root, root)
/boot
%dir /lib/modules
/lib/modules/%{uname_r}
