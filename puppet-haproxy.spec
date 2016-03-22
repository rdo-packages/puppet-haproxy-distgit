%define upstream_name puppetlabs-haproxy

Name:           puppet-haproxy
Version:        XXX
Release:        XXX
Summary:        Configures HAProxy servers and manages the configuration of backend member servers.
License:        Apache-2.0

URL:            https://github.com/puppetlabs/puppetlabs-haproxy

Source0:        https://github.com/puppetlabs/puppetlabs-haproxy/archive/%{version}.tar.gz

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

