# Add "--without doc" option to disable documentation generation
%bcond_without doc
%bcond_with gtk2

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
BuildRequires:		kernel-source = %{version}-%{source_release}
%endif
BuildRequires:		bison flex
BuildRequires:		binutils-devel
BuildRequires:		elfutils-devel
BuildRequires:		newt-devel
BuildRequires:		python-devel
%if %{with gtk2}
BuildRequires:		gtk2-devel
%endif
%if %{with doc}
BuildRequires:		asciidoc
BuildRequires:		xmlto
BuildRequires:		gettext
%endif

%description
This package contains the performance analysis tools for Linux.

%if %no_source
%define outdir_opt	O=$(pwd)
%endif
%if %{without gtk2}
%define gtk2_opt	NO_GTK2=1
%endif

%global __perf_make	make %{?_smp_mflags} -C %{source_path}tools/%{name}
%global _perf_make	%{__perf_make} prefix=%{_prefix} %{?gtk2_opt}
%global perf_make()	%{_perf_make} %{?outdir_opt} DESTDIR=%{buildroot}

%if %build_srpm
%prep
%setup -q -n %{archive}
%endif

# We're rebuilding in any cases since the flags passed to make are not
# the same as the ones used by the user previously.
%build
%{perf_make} all
%if %{with doc}
%{perf_make} man
%endif

%install
%{perf_make} install
%if %{with doc}
%{perf_make} install-man
%endif

%clean
rm -rf %{buildroot}

%files
%defattr (-, root, root)
%{_bindir}/perf
%dir %{_prefix}/libexec/perf-core
%{_prefix}/libexec/perf-core/*
%if %{with doc}
%{_mandir}/man[1-8]/*
%endif
