Summary:        A 2D graphics library.
Name:           cairo
Version:        1.17.2
Release:        2%{?dist}
License:        LGPLv2 or MPLv1.1
URL:            http://www.linuxfromscratch.org/blfs/view/svn/x/cairo.html
Group:          System Environment/Libraries
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        http://cairographics.org/releases/%{name}-%{version}.tar.xz
%define sha1    cairo=ce1234bd120bb0c1679a75a5c3c76d0b2edcc88f
Patch0:         CVE-2020-35492.patch
BuildRequires:  pkg-config
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel
BuildRequires:  pixman-devel
BuildRequires:  freetype2-devel
BuildRequires:  fontconfig-devel
BuildRequires:  glib-devel
Requires:       pixman
Requires:       glib
Requires:       libpng
Requires:       expat
%description
Cairo is a 2D graphics library with support for multiple output devices.

%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}-%{release}
Requires:	freetype2-devel
Requires:	pixman-devel
%description	devel
It contains the libraries and header files to create applications.

%prep
%setup -cqn %{name}-%{version}
mv %{name}-%{version}*/* .
%patch0 -p1

%build
# add this since build failed in not find automake-1.15 in making test for cairo
# Before running ./configure try running autoreconf -f -i.
# The autoreconf program automatically runs autoheader, aclocal, automake, autopoint and libtoolize as required.
autoreconf -f -i

%configure \
    --enable-xlib=no        \
    --enable-xlib-render=no \
    --enable-win32=no       \
    CFLAGS="-O3 -fPIC"      \
    --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -delete

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/cairo/*.so*

%files devel
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
*   Thu Apr 1 2021 Michelle Wang <michellew@vmware.com> 1.17.2-2
-   Add patch for CVE-2020-3549
*   Tue Jul 14 2020 Gerrit Photon <photon-checkins@vmware.com> 1.17.2-1
-   Automatic Version Bump
*   Thu Mar 14 2019 Michelle Wang <michellew@vmware.com> 1.16.0-1
-   Upgrade cairo to 1.16.0 for CVE-2018-18064
-   CVE-2018-18064 is for version up to (including) 1.15.14
*   Tue Sep 11 2018 Dheeraj Shetty <dheerajs@vmware.com> 1.14.12-1
-   Update to version 1.14.12
*   Tue Oct 10 2017 Dheeraj Shetty <dheerajs@vmware.com> 1.14.8-3
-   Fix CVE-2017-9814
*   Tue Jun 06 2017 Chang Lee <changlee@vmware.com> 1.14.8-2
-   Remove %check
*   Wed Apr 05 2017 Dheeraj Shetty <dheerajs@vmware.com> 1.14.8-1
-   Initial version
