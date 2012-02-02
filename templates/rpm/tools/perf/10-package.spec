Name:			%{name}
Summary:		The performance analysis tools for Linux
URL:			http://www.kernel.org
Group:			System/Kernel and hardware
License:		GPLv2
Version:		%{version}
Release:		%{source_release}.%{build_release}
%if %build_srpm
Source:			%{archive}.tar.bz2
%endif
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
%if %no_source
BuildRequires:          kernel-source = %{version}-%{source_release}
%endif
BuildRequires:		binutils-devel
BuildRequires:		elfutils-devel
BuildRequires:		newt-devel
BuildRequires:		python-devel
BuildRequires:		asciidoc
BuildRequires:		xmlto
BuildRequires:		gettext

%description
This package contains the performance analysis tools for Linux.

%if %no_source
%define outdir_opt	O=$(pwd)
%endif

%global __perf_make	make %{?_smp_mflags} -C %{source_path}tools/%{name}
%global _perf_make	%{__perf_make} prefix=%{_prefix}
%global perf_make()	%{_perf_make} %{?outdir_opt} DESTDIR=%{buildroot}

%if %build_srpm
%prep
%setup -q -n %{archive}
%endif

# We're rebuilding in any cases since the flags passed to make are not
# the same as the ones used by the user previously.
%build
%{perf_make} all
%{perf_make} man

%install
%{perf_make} install
%{perf_make} install-man

%clean
rm -rf %{buildroot}

%files
%defattr (-, root, root)
%{_bindir}/perf
%dir %{_prefix}/libexec/perf-core
%{_prefix}/libexec/perf-core/*
%{_mandir}/man[1-8]/*
