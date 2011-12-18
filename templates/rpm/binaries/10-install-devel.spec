mkdir -p %{buildroot}%{kdevel_path}
cp .config %{buildroot}%{kdevel_path}

%if %no_source
cd source
%endif

for list in %{_sourcedir}/%{uname_r}{,-%asmarch}-develfiles.list; do
	tar -cf - --files-from=$list | tar -xf - -C %{buildroot}%{kdevel_path}
done

%if %no_source
cd -
%endif

make -C %{buildroot}%{kdevel_path} modules_prepare
