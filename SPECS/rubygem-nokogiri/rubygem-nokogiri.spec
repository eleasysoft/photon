%global debug_package   %{nil}
%global gem_name        nokogiri
%global gemdir          %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})

Summary:        Nokogiri is an HTML, XML, SAX, and Reader parser.
Name:           rubygem-nokogiri
Version:        1.10.9
Release:        4%{?dist}
License:        MIT
Group:          Development/Languages
Vendor:         VMware, Inc.
Distribution:   Photon
URL:            https://rubygems.org/gems/nokogiri

Source0: https://rubygems.org/downloads/nokogiri-%{version}.gem
%define sha512 %{gem_name}=2833efb389399001c75a63bfd71afa85edd6ced07bde8b8be899f0c39016c813a4d04ff358e467d594e609db51d151ecab4561aaa20f293c58608ba3d2f7206b

BuildRequires:  ruby >= 2.4.0
BuildRequires:  rubygem-mini_portile2
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel

Requires:       ruby >= 2.4.0
Requires:       rubygem-mini_portile2
Requires:       libxml2
Requires:       libxslt

%description
Nokogiri is an HTML, XML, SAX, and Reader parser. Among Nokogiri's many features is the ability to search documents via XPath or CSS3 selectors.

%prep
%autosetup -c -T -p1

%build

%install
NOKOGIRI_USE_SYSTEM_LIBRARIES=1 gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{SOURCE0}

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root,-)
%{gemdir}

%changelog
* Fri Oct 07 2022 Shreenidhi Shedi <sshedi@vmware.com> 1.10.9-4
- Bump version as a part of libxslt upgrade
* Thu Jun 16 2022 Ashwin Dayanand Kamat <kashwindayan@vmware.com> 1.10.9-3
- Bump version as a part of libxslt upgrade
* Wed Nov 17 2021 Nitesh Kumar <kunitesh@vmware.com> 1.10.9-2
- Release bump up to use libxml2 2.9.12-1.
* Mon Jun 22 2020 Gerrit Photon <photon-checkins@vmware.com> 1.10.9-1
- Automatic Version Bump
* Tue Sep 11 2018 srinidhira0 <srinidhir@vmware.com> 1.8.4-1
- Update to version 1.8.4
* Thu Apr 13 2017 Siju Maliakkal <smaliakkal@vmware.com> 1.7.1-2
- Change ruby version in buildrequires and requires
* Wed Mar 22 2017 Xiaolin Li <xiaolinl@vmware.com> 1.7.1-1
- Updated to version 1.7.1.
* Wed Jan 25 2017 Anish Swaminathan <anishs@vmware.com> 1.6.7.2-4
- Bump up release number to reflect ruby upgrade
* Thu Oct 27 2016 Anish Swaminathan <anishs@vmware.com> 1.6.7.2-3
- Use SYSTEM_LIBRARIES for nokogiri
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.6.7.2-2
- GA - Bump release of all rpms
* Wed Jan 20 2016 Anish Swaminathan <anishs@vmware.com> 1.6.7.2-1
- Upgrade version.
* Wed Nov 11 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.6.6.2-1
- Initial build
