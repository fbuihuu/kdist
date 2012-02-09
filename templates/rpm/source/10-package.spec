Name:			%{name}
Summary:		Linux kernel source files
Version:		%{version}
Release:		%{source_release}
License:		GPLv2
Group:			System/Kernel and hardware
URL:			http://www.kernel.org
Source0:		%{archive}.tar.bz2
Buildarch:		noarch
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
AutoReqProv:		no

%define debug_package	%{nil}
%define __check_files	%{nil}

%description
This package provides the whole kernel source files.

%install
mkdir -p %{buildroot}%{_source_path}
tar -xf %{SOURCE0} --strip-components=1 -C %{buildroot}%{_source_path}

%clean
rm -rf %{buildroot}

%files
%defattr (-, root, root)
%{_source_path}
