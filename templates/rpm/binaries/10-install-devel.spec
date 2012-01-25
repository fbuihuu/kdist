mkdir -p %{buildroot}%{kdevel_path}

%if %no_source
cd source
%endif

for list in %{_sourcedir}/%{uname_r}{,-%asmarch}-develfiles.list; do
	tar -cf - --files-from=$list | tar -xf - -C %{buildroot}%{kdevel_path}
done

%if %no_source
cd -
%endif

list=%{_sourcedir}/%{uname_r}-output-develfiles.list
tar -cf - --files-from=$list | tar -xf - -C %{buildroot}%{kdevel_path}

# localversion exists when generating a released srpm package, in that
# case import it in the devel directory.
test -f localversion && cp localversion %{buildroot}%{kdevel_path}

make -C %{buildroot}%{kdevel_path} modules_prepare
