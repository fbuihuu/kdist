%files -n %{name}-debuginfo -f debugfiles.list
%defattr (-, root, root)
%{debuginfodir}/lib/modules/%{uname_r}/vmlinux
