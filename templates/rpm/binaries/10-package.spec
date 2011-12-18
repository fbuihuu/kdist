Summary:		The Linux Kernel for Mandriva %{flavour} systems
Provides:		kernel = %{version}-%{release}
Group:			System/Kernel and hardware
Requires:		kernel-firmware

%if %no_source
BuildRequires:		kernel-source = %{version}-%{source_release}
%endif
