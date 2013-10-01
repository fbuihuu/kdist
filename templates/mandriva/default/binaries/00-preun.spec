%preun
#
# Keep backward compatibility with old mandriva and also current
# mageia systems which use drakx stuff to install new kernels.
#
if test -d /etc/kernel/preun.d; then
	run-parts --verbose --exit-on-error		\
		--arg=%{uname_r}			\
		--arg=/boot/vmlinuz-%{uname_r}		\
		/etc/kernel/preun.d

elif test -x /sbin/installkernel; then
	/sbin/installkernel -R %{uname_r}
fi
