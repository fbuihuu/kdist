%description
cpupower is a collection of tools to examine and tune power saving
related features of your processor.

This collection of tools allow users and developers to have *one* tool
to get an overview what their system supports and to monitor and debug
CPU power management in detail.


%package -n %{libname}
Summary:		The shared library for %{name}
Group:			System/Kernel and hardware

%description -n %{libname}
"libcpupower" is a library which offers a unified access method for
userspace tools and programs to the cpufreq core and drivers in the
Linux kernel. This allows for code reduction in userspace tools, a
clean implementation of the interaction to the cpufreq core, and
support for both the sysfs and proc interfaces.


%package -n %{devname}
Summary:		The development files for %{name} shared library
Group:			System/Kernel and hardware
Requires:		%{libname} = %{version}-%{release}
Provides:		cpupower-devel = %{version}-%{release}

%description -n %{devname}
The development files needed for cpupower's shared library.

"libcpupower" is a library which offers a unified access method for
userspace tools and programs to the cpufreq core and drivers in the
Linux kernel. This allows for code reduction in userspace tools, a
clean implementation of the interaction to the cpufreq core, and
support for both the sysfs and proc interfaces.
