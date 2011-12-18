make oldconfig
# Sanity check uname_r (it can be modified)
test %{uname_r} = $(make -s kernelrelease)

%if %build_srpm
make %{?_smp_mflags}
%endif
