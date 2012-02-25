#
# All this mess in order to have vmlinux build-id unmodified, its
# symtab section preserved and the generated source codes included in
# the debuginfo package.
#
# It also handles the different packaging cases (srpm, srpm+source,
# rpm), with more or less restrictions. But for the 'official' one,
# that is srpm using the kernel-source package, there shouldn't be
# any.
#
%define debuginfodir /usr/lib/debug

#
# Install vmlinux in a temporary (and arbitrary) place with the exec
# bit set so find-debuginfo will consider it.
#
cp vmlinux %{buildroot}/vmlinux-%{uname_r}
chmod +x %{buildroot}/vmlinux-%{uname_r}

#
# When using kernel-source package, find-debuginfo is only used to
# install the _generated_ source code (mostly arrays of data).
# Otherwise it installs both the source code and the generated one.
#
# In any cases, it generates the modules debug files, the module
# symlinks and the list of the generated source files.
#
%__debug_install_post
%define __debug_install_post %{nil}

#
# Now remove vmlinux since the build-id has been changed and doesn't
# match anymore the one embedded in the bzImage.
# Also remove the associated symlink, assuming it's the only
# dangling one.
#
rm -f %{buildroot}/vmlinux-%{uname_r}
rm -f %{buildroot}%{debuginfodir}/vmlinux-%{uname_r}.debug
sed -i -e \\,%{debuginfodir}/vmlinux-%{uname_r},d debugfiles.list

find %{buildroot}%{debuginfodir}/.build-id/ -name \*.debug | \
while read symlink
do
	symlink=${symlink%%.debug}
	readlink -e $symlink && continue
	# Dangling symlink, be sure it points to vmlinux
	case $(readlink -f $symlink) in
	%{buildroot}/vmlinux-%{uname_r})
		rm -f $symlink $symlink.debug
		sed -i -e \\,${symlink#%{buildroot}},d debugfiles.list
		break ;;
	*)
		exit 1
	esac
done

#
# Restore vmlinux with the preserved build-id. No need to create a
# separate debuginfo file and the associated symlink for now.
#
# Don't even try to install it in /boot since it includes the
# debug info.
#
mkdir -p %{buildroot}%{debuginfodir}/lib/modules/%{uname_r}
cp vmlinux %{buildroot}%{debuginfodir}/lib/modules/%{uname_r}

#
# Fix the source paths in the debug sections when not using the
# kernel-source package (including  build_srpm=0 case).
#
%if ! %{build_srpm} || ! %{no_source}
# build-id is not updated so it's not correct anymore but at least it
# still matches the one embedded in the bzImage. Actually build-id
# shouldn't be used for content verification, it's a unique identifier
# good only for matching.

# Thanks rpm5...
export PATH=/usr/lib/rpm:/usr/lib/rpm/bin:$PATH
debugedit -b %{_builddir} -d /usr/src/debug \
	%{buildroot}%{debuginfodir}/lib/modules/%{uname_r}/vmlinux
%endif
