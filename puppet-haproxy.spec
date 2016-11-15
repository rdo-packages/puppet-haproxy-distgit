%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-haproxy
%global commit 6ee818019078e7ac9a6316409c369bf907ec2afd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-haproxy
Version:        1.5.0
Release:        2%{?alphatag}%{?dist}
Summary:        Configures HAProxy servers and manages the configuration of backend member servers.
License:        Apache-2.0

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
* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 1.5.0-2.6ee8180.git
- Newton update 1.5.0 (6ee818019078e7ac9a6316409c369bf907ec2afd)

* Tue Sep 20 2016 Haikel Guemar <hguemar@fedoraproject.org> - 1.5.0-1.f8c5f27.git
- Newton update 1.5.0 (f8c5f2774f78fec9c2ee5b88d3e1c89e4013bd0a)


