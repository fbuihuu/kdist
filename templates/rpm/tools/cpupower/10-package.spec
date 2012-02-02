Name:			%{name}
Summary:		The power analysis tools for your processor
URL:			http://www.kernel.org
Group:			System/Kernel and hardware
License:		GPLv2
Version:		%{version}
Release:		%{source_release}.%{build_release}
ExclusiveArch:		%{ix86} x86_64
%if %build_srpm
Source:			%{archive}.tar.bz2
%endif
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
%if %no_source
BuildRequires:		kernel-source = %{version}-%{source_release}
%endif
BuildRequires:		pciutils-devel
