%if %no_source
%define outdir_opt	O=$(pwd)
%endif

%global __cpupower_make	make %{?_smp_mflags} -C %{source_path}tools/power/%{name}
%global _cpupower_make	%{__cpupower_make} bindir=%{_bindir} libdir=%{_libdir} mandir=%{_mandir}
%global cpupower_make	%{_cpupower_make} %{?outdir_opt} DESTDIR=%{buildroot} CPUFREQ_BENCH=false

%if %build_srpm
%prep
%setup -q -n %{archive}
%endif
# when reusing the kernel source, the empty archive misses the
# README, so import it in that case.
test -f README || cp %{source_path}tools/power/%{name}/README .

# We're rebuilding in any cases (srpm or rpm) since the flags passed
# to make are not the same as the ones used by the user previously.
%build
%{cpupower_make}
