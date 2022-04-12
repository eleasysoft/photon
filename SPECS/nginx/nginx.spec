%define njs_ver 0.2.1

Summary:        High-performance HTTP server and reverse proxy
Name:           nginx
Version:        1.16.1
Release:        5%{?dist}
License:        BSD-2-Clause
URL:            http://nginx.org/download/nginx-%{version}.tar.gz
Group:          Applications/System
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        %{name}-%{version}.tar.gz
%define sha1    %{name}=77ce4d26481b62f7a9d83e399454df0912f01a4b
Source1:        nginx.service
Source2:        nginx-njs-%{njs_ver}.tar.gz
%define sha1    nginx-njs=fd8c3f2d219f175be958796e3beaa17f3b465126

Patch0:         nginx-CVE-2019-20372.patch
Patch1:         0001-nginx-DNS-Resolver-Off-by-One-Heap-Write-in-ngx_reso.patch
Patch2:         nginx-CVE-2021-3618.patch

BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  which
BuildRequires:  systemd

%description
NGINX is a free, open-source, high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server.

%prep
%autosetup -p1
pushd ..
mkdir -p nginx-njs
tar -C nginx-njs -xf %{SOURCE2}
popd

%build
sh ./configure \
    --prefix=%{_sysconfdir}/nginx \
    --sbin-path=%{_sbindir}/nginx \
    --conf-path=/etc/nginx/nginx.conf \
    --pid-path=/var/run/nginx.pid \
    --lock-path=/var/run/nginx.lock \
    --error-log-path=/var/log/nginx/error.log \
    --http-log-path=/var/log/nginx/access.log \
    --add-module=../nginx-njs/njs-%{njs_ver}/nginx \
    --with-http_ssl_module \
    --with-pcre \
    --with-ipv6 \
    --with-stream \
    --with-http_auth_request_module \
    --with-http_sub_module \
    --with-http_v2_module \
    --with-http_stub_status_module

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -vdm755 %{buildroot}%{_unitdir}
install -vdm755 %{buildroot}%{_var}/log/nginx
install -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/nginx.service

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/%{name}/fastcgi.conf
%config(noreplace) %{_sysconfdir}/%{name}/fastcgi.conf.default
%config(noreplace) %{_sysconfdir}/%{name}/fastcgi_params
%config(noreplace) %{_sysconfdir}/%{name}/fastcgi_params.default
%config(noreplace) %{_sysconfdir}/%{name}/koi-utf
%config(noreplace) %{_sysconfdir}/%{name}/koi-win
%config(noreplace) %{_sysconfdir}/%{name}/mime.types
%config(noreplace) %{_sysconfdir}/%{name}/mime.types.default
%config(noreplace) %{_sysconfdir}/%{name}/nginx.conf
%config(noreplace) %{_sysconfdir}/%{name}/nginx.conf.default
%config(noreplace) %{_sysconfdir}/%{name}/scgi_params
%config(noreplace) %{_sysconfdir}/%{name}/scgi_params.default
%config(noreplace) %{_sysconfdir}/%{name}/uwsgi_params
%config(noreplace) %{_sysconfdir}/%{name}/uwsgi_params.default
%{_sysconfdir}/%{name}/win-utf
%{_sysconfdir}/%{name}/html/*
%{_sbindir}/*
%{_unitdir}/nginx.service
%dir %{_var}/log/nginx

%changelog
* Tue Apr 12 2022 Nitesh Kumar <kunitesh@vmware.com> 1.16.1-5
- Fix for CVE-2021-3618
* Thu Dec 16 2021 Shreenidhi Shedi <sshedi@vmware.com> 1.16.1-4
- Fix nginx service handling
* Wed May 19 2021 Keerthana K <keerthanak@vmware.com> 1.16.1-3
- Fix for CVE-2021-23017
* Tue Feb 11 2020 Ankit Jain <ankitja@vmware.com> 1.16.1-2
- Fix for CVE-2019-20372
* Tue Sep 03 2019 Satya Naga Vasamsetty <svasamsetty@vmware.com> 1.16.1-1
- Update to version 1.16.1-1
* Thu Apr 11 2019 Keerthana K <keerthanak@vmware.com> 1.15.11-1
- Update to version 1.15.11
* Fri Mar 15 2019 Keerthana K <keerthanak@vmware.com> 1.13.10-3
- Enable http_stub_status_module.
* Fri Feb 15 2019 Siju Maliakkal <smaliakkal@vmware.com> 1.13.10-2
- Patch for CVE-2018-16845
* Mon Jan 28 2019 Keerthana K <keerthanak@vmware.com> 1.13.10-1
- Update to version 1.13.10
* Thu Jan 17 2019 Keerthana K <keerthanak@vmware.com> 1.13.8-7
- Adding http v2 module support.
* Mon Dec 17 2018 Ankit Jain <ankitja@vmware.com> 1.13.8-6
- Fix for CVE-2018-16843 and CVE-2018-16844
* Wed Sep 12 2018 Keerthana K <keerthanak@vmware.com> 1.13.8-5
- Adding http_auth_request_module and http_sub_module.
* Fri Jul 20 2018 Keerthana K <keerthanak@vmware.com> 1.13.8-4
- Restarting nginx service on failure.
* Fri Jun 08 2018 Dheeraj Shetty <dheerajs@vmware.com> 1.13.8-3
- mark config files as non replaceable on upgrade.
* Fri Jun 08 2018 Dheeraj Shetty <dheerajs@vmware.com> 1.13.8-2
- adding module njs.
* Wed Mar 28 2018 Dheeraj Shetty <dheerajs@vmware.com> 1.13.8-1
- Update to version 1.13.8 to support nginx-ingress
* Wed Oct 04 2017 Xiaolin Li <xiaolinl@vmware.com> 1.13.5-1
- Update to version 1.13.5
* Mon May 01 2017 Dheeraj Shetty <dheerajs@vmware.com> 1.11.13-2
- adding module stream to nginx.
* Wed Apr 05 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.11.13-1
- update to 1.11.13
* Fri Nov 18 2016 Anish Swaminathan <anishs@vmware.com>  1.10.0-5
- Add patch for CVE-2016-4450
* Wed Jul 27 2016 Divya Thaluru<dthaluru@vmware.com> 1.10.0-4
- Removed packaging of debug files
* Fri Jul 8 2016 Divya Thaluru<dthaluru@vmware.com> 1.10.0-3
- Modified default pid filepath and fixed nginx systemd service
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.10.0-2
- GA - Bump release of all rpms
* Mon May 16 2016 Xiaolin Li <xiaolinl@vmware.com> 1.10.0-1
- Initial build. First version
