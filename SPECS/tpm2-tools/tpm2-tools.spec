Summary:        The source repository for the TPM (Trusted Platform Module) 2 tools
Name:           tpm2-tools
Version:        5.3
Release:        2%{?dist}
License:        BSD 2-Clause
URL:            https://github.com/tpm2-software/tpm2-tools
Group:          System Environment/Security
Vendor:         VMware, Inc.
Distribution:   Photon

Source0: https://github.com/tpm2-software/tpm2-tools/releases/download/%{version}/%{name}-%{version}.tar.gz
%define sha512 %{name}=224a5ea3448a877362abb35ac06b115c559c09b44b30d74c8326211be66d24e0e130c285b1e285be1842e7203ab488629b0f4e451cbd782c83ed72023d146675

BuildRequires: openssl-devel
BuildRequires: curl-devel
BuildRequires: tpm2-tss-devel
%if 0%{?with_check}
BuildRequires:  ibmtpm
BuildRequires:  systemd
%endif

Requires: openssl
Requires: curl
Requires: tpm2-tss

%description
The source repository for the TPM (Trusted Platform Module) 2 tools

%prep
%autosetup -p1

%build
sed -i "/compatibility/a extern int BN_bn2binpad(const BIGNUM *a, unsigned char *to, int tolen);" lib/tpm2_openssl.c
%configure --disable-static
%make_build

%install
%make_install %{?_smp_mflags}

%if 0%{?with_check}
%check
if [ ! -f /dev/tpm0 ];then
   systemctl start ibmtpm_server.service
   export TPM2TOOLS_TCTI=mssim:host=localhost,port=2321
   tpm2_startup -c
   tpm2_pcrlist
fi
make %{?_smp_mflags} check
%endif

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1
%{_datadir}/bash-completion/*

%changelog
* Sun Oct 09 2022 Shreenidhi Shedi <sshedi@vmware.com> 5.3-2
- Bump version as a part of ibmtpm upgrade
* Wed Oct 05 2022 Shreenidhi Shedi <sshedi@vmware.com> 5.3-1
- Upgrade to v5.3
* Tue Apr 19 2022 Gerrit Photon <photon-checkins@vmware.com> 5.2-1
- Automatic Version Bump
* Thu Jul 15 2021 Satya Naga Vasamsetty <svasamsetty@vmware.com> 5.0-2
- Openssl 3.0.0 support
* Tue Apr 13 2021 Gerrit Photon <photon-checkins@vmware.com> 5.0-1
- Automatic Version Bump
* Tue Feb 09 2021 Alexey Makhalov <amakhalov@vmware.com> 4.3.0-4
- Fix compilation issue with BN_bn2binpad
* Tue Jan 19 2021 Shreenidhi Shedi <sshedi@vmware.com> 4.3.0-3
- Removed patch which was added to fix a build issue
* Thu Oct 15 2020 Shreenidhi Shedi <sshedi@vmware.com> 4.3.0-2
- Fix build warnings
* Tue Sep 01 2020 Gerrit Photon <photon-checkins@vmware.com> 4.3.0-1
- Automatic Version Bump
* Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 4.2.1-1
- Automatic Version Bump
* Wed Jun 10 2020 Michelle Wang <michellew@vmware.com> 3.1.3-2
- update make check with ibmtpm
* Thu Feb 21 2019 Alexey Makhalov <amakhalov@vmware.com> 3.1.3-1
- Initial build. First version.
