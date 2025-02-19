%{!?python3_sitelib: %global python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}

Summary:        rt-tests tests various real-time features of linux
Name:           rt-tests
Version:        2.4
Release:        1%{?dist}
License:        GPL-2.0
Group:          Development/Tools
URL:            https://git.kernel.org/pub/scm/utils/rt-tests/rt-tests.git/
Source0:        %{name}-%{version}.tar.gz
%define sha512  rt-tests=34c157cc0ad049146560812ea61be073730610081723c5d1ab93c8d0c83017991a6c5b06eac7bb6dc974b35a57591f0056a1e0ab912906e2c6d31ba8a1ced497
Vendor:         VMware, Inc.
Distribution:   Photon
BuildRequires:  build-essential
BuildRequires:  libnuma-devel
BuildRequires:  python3
Requires:       python3
Requires:       libnuma
Requires:       glibc

%description
rt-tests includes various programs that test different real-time
features of the linux kernel. Refer to documentation on each test
for detailed descriptions.

%prep
%autosetup -n %{name}-%{version}

%build
%make_build prefix=%{_prefix}

%install
%make_install %{?_smp_mflags} prefix=%{_prefix}
ln -s %{python3_sitelib}/get_cyclictest_snapshot.py %{_bindir}/get_cyclictest_snapshot
ln -s %{python3_sitelib}/hwlatdetect.py %{_bindir}/hwlatdetect

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{python3_sitelib}/hwlatdetect.py
%{python3_sitelib}/get_cyclictest_snapshot.py
%{_mandir}/man8/*

%changelog
* Thu Sep 08 2022 Sharan Turlapati <sturlapati@vmware.com> 2.4-1
- Initial version of rt-tests for Photon
