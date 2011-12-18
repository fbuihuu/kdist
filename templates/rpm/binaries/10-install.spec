if grep -q CONFIG_MODULES=y .config
then
	#
	# Don't specify parallel jobs here since it may break modules
	# installation somehow...
	#
	make -s INSTALL_MOD_PATH=%{buildroot} modules_install

	#
	# Mark all kernel modules as executable so they will be
	# stripped and their corresponding debug info files will be
	# generated if needed.
	#
	find %{buildroot} -name \*.ko -exec chmod u+x {} \;
else
	mkdir -p %{buildroot}/lib/modules/%{uname_r}
fi
mkdir -p %{buildroot}/boot

# symlinks are always created.
ln -snf %{kdevel_path} %{buildroot}/lib/modules/%{uname_r}/build
ln -snf build %{buildroot}/lib/modules/%{uname_r}/source
