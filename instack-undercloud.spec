%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           instack-undercloud
Version:        XXX
Release:        XXX
Summary:        Installation tools to install an undercloud via instack

Group:          Development/Languages
License:        ASL 2.0
Url:            https://github.com/openstack/instack-undercloud
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools
BuildRequires:  git
Requires:       instack
Requires:       openstack-tripleo-heat-templates
Requires:       openstack-tripleo-image-elements
Requires:       redhat-lsb-core
Requires:       policycoreutils-python
Requires:       openstack-tripleo-puppet-elements
Requires:       python2-psutil
Requires:       python2-os-client-config
Requires:       python2-oslo-config >= 2:5.1.0
Requires:       python2-oslo-utils >= 3.33.0
Requires:       pystache
Requires:       jq
Requires:       os-apply-config
Requires:       os-net-config
Requires:       os-refresh-config
Requires:       python-heat-agent
Requires:       puppet
Requires:       puppet-tripleo
Requires:       python2-six
Requires:       python2-keystoneclient >= 1:3.8.0
Requires:       python2-ironicclient >= 2.2.0
Requires:       python2-mistralclient >= 3.1.0
Requires:       python2-novaclient >= 1:9.1.0
Requires:       python2-swiftclient >= 3.2.0
Requires:       python2-netaddr
Requires:       python-netifaces

Requires:       selinux-policy

%description
instack-undercloud is a collection of installation tools to install an
undercloud via python-instack. It contains scripts and elements to complete the
installation.


%prep
%autosetup -S git -n %{name}-%{upstream_version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}


%files
%doc README.md
%doc LICENSE
%{_datadir}/instack-undercloud
%{_bindir}/instack-*
%{python2_sitelib}/instack_undercloud*
%exclude %{python2_sitelib}/instack_undercloud/tests


%changelog
