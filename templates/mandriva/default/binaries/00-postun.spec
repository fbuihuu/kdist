%postun
#
# Keep backward compatibility with old mandriva and also current
# mageia systems which use drakx stuff to install new kernels.
#
if test -d /etc/kernel/postun.d; then
	run-parts --verbose --exit-on-error		\
		--arg=%{uname_r}			\
		--arg=/boot/vmlinuz-%{uname_r}		\
		/etc/kernel/postun.d

elif test -x /sbin/kernel_remove_initrd; then
	/sbin/kernel_remove_initrd %{uname_r}
fi
