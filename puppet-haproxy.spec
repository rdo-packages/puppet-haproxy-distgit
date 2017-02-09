%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-haproxy
%global commit f6fed46e7a5c3f9e4791240eaffb1a115d8f0135
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-haproxy
Version:        1.5.0
Release:        3%{?alphatag}%{?dist}
Summary:        Configures HAProxy servers and manages the configuration of backend member servers.
License:        ASL 2.0

URL:            https://github.com/puppetlabs/puppetlabs-haproxy

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-concat
Requires:       puppet >= 2.7.0

%description
Configures HAProxy servers and manages the configuration of backend member servers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/haproxy/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/haproxy/



%files
%{_datadir}/openstack-puppet/modules/haproxy/


%changelog
* Thu Feb 09 2017 Alfredo Moralejo <amoralej@redhat.com> 1.5.0-3.f6fed46git
- Ocata update 1.5.0 (f6fed46e7a5c3f9e4791240eaffb1a115d8f0135)

