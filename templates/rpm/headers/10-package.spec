Name:			%{name}
Summary:		Linux kernel header files mostly used by your C library
Version:		%{version}
Release:		%{source_release}.%{build_release}
License:		GPLv2
Group:			System/Kernel and hardware
URL:			http://www.kernel.org
%if %build_srpm
Source:			%{archive}.tar.bz2
%endif
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
AutoReqProv:		no
%if %no_source
BuildRequires:          kernel-source = %{version}-%{source_release}
%endif

%define debug_package	%{nil}
%define __check_files	%{nil}

%description
C header files from the Linux kernel. The header files define
structures and constants that are needed for building most
standard programs, notably the C library.

This package is not suitable for building kernel modules, you
should use the '%{name}-devel' package instead.

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
make -C %{source_path} INSTALL_HDR_PATH=%{buildroot}/usr $extra_opts headers_install

%clean
rm -rf %{buildroot}

%files
%defattr (-, root, root)
/usr/include

