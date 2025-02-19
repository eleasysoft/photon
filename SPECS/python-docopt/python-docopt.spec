Name:           python3-docopt
Version:        0.6.2
Release:        3%{?dist}
Summary:        Pythonic argument parser to create command line interfaces.
License:        MIT
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/docopt
Vendor:         VMware, Inc.
Distribution:   Photon

Source0: docopt-%{version}.tar.gz
%define sha512 docopt=af138feccf8c37b374ee44fcda4938a88107d434df13c173214021b1a3348b152a595095a86982b66ac03a11db8e0f1e9e6a3a65c98deea92330311daeb831a3

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if 0%{?with_check}
BuildRequires:  python3-pytest
%endif

Requires:       python3
Requires:       python3-setuptools

BuildArch:      noarch

%description
docopt helps easily create most beautiful command-line interfaces.

%prep
%autosetup -p1 -n docopt-%{version}

%build
%py3_build

%install
%py3_install

%if 0%{?with_check}
%check
python3 setup.py test
%endif

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
* Tue Dec 15 2020 Shreenidhi Shedi <sshedi@vmware.com> 0.6.2-3
- Fix build with new rpm
* Tue Jun 16 2020 Tapas Kundu <tkundu@vmware.com> 0.6.2-2
- Mass removal python2
* Fri Aug 25 2017 Vinay Kulkarni <kulkarniv@vmware.com> 0.6.2-1
- Initial version of python-docopt package for Photon.
