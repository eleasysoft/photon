Summary:        Operating system utility that allows programs to run as non-previleged user.
Name:           authbind
Version:        2.1.2
Release:        2%{?dist}
License:        GPL
URL:            http://www.chiark.greenend.org.uk/ucgi/~ian/git/authbind.git
Group:          Applications/utils
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        http://ftp.debian.org/debian/pool/main/a/%{name}/%{name}_%{version}.tar.gz
%define sha1 authbind=18434ebfbff5560e8691ebafcb2896837447a98f

%description
The authbind software allows a program that would normally require superuser privileges to access privileged network services to run as a non-privileged user.

%prep
%autosetup -p1 -n authbind
sed -i 's#-Wall#-Wall -Wno-unused-result#g' Makefile
sed -i 's#\/usr\/local#%{_prefix}#g' Makefile
sed -i 's#755 -s#755#g' Makefile

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir} \
         %{buildroot}%{_libdir} \
         %{buildroot}%{_sysconfdir} \
         %{buildroot}%{_mandir}/man1 \
         %{buildroot}%{_mandir}/man8

make install DESTDIR=%{buildroot} STRIP=/bin/true %{?_smp_mflags}
install -vm 755 authbind %{buildroot}%{_bindir}
install -vm 755 helper %{buildroot}%{_libdir}
install -vm 755 libauthbind.so.1.0 %{buildroot}%{_libdir}
cp -r %{_sysconfdir}/%{name} %{buildroot}%{_sysconfdir}
cp authbind.1* %{buildroot}%{_mandir}/man1
cp authbind-helper.8* %{buildroot}%{_mandir}/man8

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_libdir}/libauthbind.so*
%{_libdir}/helper
%{_sysconfdir}/authbind
%{_mandir}

%changelog
* Thu Oct 22 2020 Dweep Advani <dadvani@vmware.com> 2.1.2-2
- Fixed install failure
* Fri Jul 14 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.1.2-1
- Initial build. First version
