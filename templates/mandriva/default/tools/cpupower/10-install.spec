%install
%{cpupower_make} install-lib install-tools
%if %{with doc}
%{cpupower_make} install-man
%endif
