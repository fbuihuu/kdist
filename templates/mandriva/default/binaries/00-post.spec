%post
#
# Keep backward compatibility with old mandriva and also current
# mageia systems which use drakx stuff to install new kernels.
#
if test -d /etc/kernel/postinst.d; then
	run-parts --verbose				\
		--arg=%{uname_r}			\
		--arg=/boot/vmlinuz-%{uname_r}		\
		/etc/kernel/postinst.d

elif test -x /sbin/installkernel; then
	/sbin/installkernel %{uname_r}
fi
