%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-haproxy
%global commit 6215a5e735b7f7bb470d0c10c5e8f72e6c17f4b7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-haproxy
Version:        2.1.0
Release:        2%{?alphatag}%{?dist}
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
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 2.1.0-2.6215a5egit
- Update to post 2.1.0 (6215a5e735b7f7bb470d0c10c5e8f72e6c17f4b7)



