%files -n %{libname}
%doc README
%{_libdir}/libcpupower.so.%{major}*

%files -n %{devname}
%doc README
%{_includedir}/cpufreq.h
%{_libdir}/libcpupower.so
