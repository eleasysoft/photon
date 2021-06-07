Summary:        library for fast, message-based applications
Name:           zeromq
Version:        4.3.4
Release:        1%{?dist}
URL:            http://www.zeromq.org
License:        LGPLv3+
Group:          System Environment/Libraries
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        https://github.com/zeromq/libzmq/releases/download/v4.3.4/%{name}-%{version}.tar.gz
%define sha1 zeromq=47277a64749049123d1401600e8cfbab10a3ae28

Requires:       libstdc++

%description
The 0MQ lightweight messaging kernel is a library which extends the standard
socket interfaces with features traditionally provided by specialised messaging
middleware products. 0MQ sockets provide an abstraction of asynchronous message
queues, multiple messaging patterns, message filtering (subscriptions), seamless
access to multiple transport protocols and more.

%package    devel
Summary:    Header and development files for zeromq
Requires:   %{name} = %{version}
%description    devel
It contains the libraries and header files to create applications 

%prep
%autosetup


%build
./configure \
    --prefix=%{_prefix} \
    --with-libsodium=no \
    --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
find %{buildroot}%{_libdir} -name '*.la' -delete

%check
make %{?_smp_mflags} check

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING COPYING.LESSER NEWS
%{_bindir}/
%{_libdir}/libzmq.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libzmq.so
%{_libdir}/pkgconfig/libzmq.pc
%{_includedir}/
%{_mandir}/*

%changelog
*   Mon Jun 07 2021 Siju Maliakkal <smaliakkal@vmware.com> 4.3.4-1
-   Upgrading to Fix CVE-2021-20236
*   Thu Sep 03 2020 Shreenidhi Shedi <sshedi@vmware.com> 4.1.4-3
-   Fix CVE-2020-15166
*   Mon Jul 22 2019 Siju Maliakkal <smaliakkal@vmware.com> 4.1.4-2
-   Apply patch for CVE-2019-13132
*   Thu Apr 13 2017 Dheeraj Shetty <dheerajs@vmware.com> 4.1.4-1
-   Initial build. First version
