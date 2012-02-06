%global __debug_package	1

%package debuginfo
Summary:		The debug information for the %{flavour} kernel
Provides:		kernel-debuginfo = %{version}-%{release}
Group:			Development/Debug
AutoReqProv:		no
