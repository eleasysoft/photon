%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}

Summary:       Python documentation generator
Name:          python3-sphinx
Version:       3.2.1
Release:       1%{?dist}
Group:         Development/Tools
License:       BSD-2-Clause
URL:           http://www.vmware.com
Vendor:        VMware, Inc.
Distribution:  Photon
Source0:       https://pypi.python.org/packages/a7/df/4487783152b14f2b7cd0b0c9afb119b262c584bf972b90ab544b61b74c62/Sphinx-%{version}.tar.gz
%define sha1    Sphinx=00491c562965c8e9d5f14fe83eef9a2211fa5ea5
BuildRequires: python3
BuildRequires: python3-libs
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-babel
BuildRequires: python3-docutils
BuildRequires: python3-jinja2
BuildRequires: python3-Pygments
BuildRequires: python3-six
BuildRequires: python3-alabaster
BuildRequires: python3-imagesize
BuildRequires: python3-requests
BuildRequires: python3-snowballstemmer
BuildRequires: python3-typing
BuildRequires: python3-pytest
BuildRequires: python3-pip

Requires:      python3
Requires:      python3-libs
Requires:      python3-babel
Requires:      python3-docutils
Requires:      python3-jinja2
Requires:      python3-Pygments
Requires:      python3-six
Requires:      python3-alabaster
Requires:      python3-imagesize
Requires:      python3-requests
Requires:      python3-snowballstemmer
Requires:      python3-typing

BuildArch:      noarch

%description
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.


%prep
%setup -q -n Sphinx-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
mv %{buildroot}/%{_bindir}/sphinx-quickstart %{buildroot}/%{_bindir}/sphinx-quickstart3
mv %{buildroot}/%{_bindir}/sphinx-build %{buildroot}/%{_bindir}/sphinx-build3
mv %{buildroot}/%{_bindir}/sphinx-autogen %{buildroot}/%{_bindir}/sphinx-autogen3
mv %{buildroot}/%{_bindir}/sphinx-apidoc %{buildroot}/%{_bindir}/sphinx-apidoc3

%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}

%clean

%files
%defattr(-,root,root)
%{_bindir}/sphinx-quickstart3
%{_bindir}/sphinx-build3
%{_bindir}/sphinx-autogen3
%{_bindir}/sphinx-apidoc3
%{python3_sitelib}/*

%changelog
*   Wed Aug 19 2020 Gerrit Photon <photon-checkins@vmware.com> 3.2.1-1
-   Automatic Version Bump
*   Tue Aug 11 2020 Gerrit Photon <photon-checkins@vmware.com> 3.2.0-1
-   Automatic Version Bump
*   Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 3.1.2-1
-   Automatic Version Bump
*   Mon Jun 15 2020 Tapas Kundu <tkundu@vmware.com> 1.7.9-2
-   Mass removal python2
*   Sun Sep 09 2018 Tapas Kundu <tkundu@vmware.com> 1.7.9-1
-   Update to version 1.7.9
*   Wed Jun 07 2017 Xiaolin Li <xiaolinl@vmware.com> 1.5.3-5
-   Add python3-setuptools and python3-xml to python3 sub package Buildrequires.
*   Thu Jun 01 2017 Dheeraj Shetty <dheerajs@vmware.com> 1.5.3-4
-   Keep the original python2 scripts and rename the python3 scripts
*   Wed Apr 26 2017 Dheeraj Shetty <dheerajs@vmware.com> 1.5.3-3
-   BuildRequires and Requires python-babel, python-docutils, python-jinja2,
    python-Pygments, python-six, python-alabaster, python-imagesize,
    python-requests and python-snowballstemmer. Adding python3 version
*   Tue Apr 25 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.5.3-2
-   Fix arch
*   Thu Mar 30 2017 Sarah Choi <sarahc@vmware.com> 1.5.3-1
-   Upgrade version to 1.5.3
*   Fri Dec 16 2016 Dheeraj Shetty <dheerajs@vmware.com> 1.5.1-1
-   Initial
