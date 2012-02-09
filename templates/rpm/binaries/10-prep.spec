%prep
%if %build_srpm
%setup -q -n %{archive}
cp %{_sourcedir}/%{uname_r}-%{asm}-defconfig .config

%if %no_source
make -C %{source_path} O=$(pwd) outputmakefile
%endif

# localversion is updated here so the user can increase
# the release number anytime.
echo -n .%{build_release} >localversion

%endif
