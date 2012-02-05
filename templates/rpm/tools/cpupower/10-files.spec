%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/cpupower
%{_bindir}/centrino-decode
%{_bindir}/powernow-k8-decode
%if %{with doc}
%{_mandir}/man[1-8]/cpupower*
%endif
