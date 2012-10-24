Name:			%{name}
Summary:		Linux kernel firmware files
Version:		%{version}
Release:		%{source_release}.%{build_release}
License:		GPLv2
Group:			System/Kernel and hardware
URL:			http://www.kernel.org
%if %build_srpm
Source:			%{archive}.tar.bz2
%endif
Buildarch:		noarch
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
AutoReqProv:		no
%if %no_source
BuildRequires:		kernel-source = %{version}-%{source_release}
%endif

%define debug_package	%{nil}
%define __check_files	%{nil}

%description
Firmware files needed by some devices.

%if %build_srpm
%prep
%setup -q -n %{archive}
%endif

%install
# Unfortunately we can't use "make outputmakefile" here because for
# some reasons this target requires a .config installed.
%if %no_source
extra_opts="O=$(pwd)"
%endif
make -C %{source_path} INSTALL_FW_PATH=%{buildroot}/lib/firmware $extra_opts firmware_install

%clean
rm -rf %{buildroot}

%files
%defattr (-, root, root)
/lib/firmware

