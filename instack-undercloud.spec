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
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  git
Requires:       instack
Requires:       openstack-tripleo-heat-templates
Requires:       openstack-tripleo-image-elements
Requires:       redhat-lsb-core
Requires:       policycoreutils-python
Requires:       openstack-tripleo-puppet-elements
Requires:       python-psutil
Requires:       python-os-client-config
Requires:       python-oslo-config >= 2:4.0.0
Requires:       pystache
Requires:       jq
Requires:       os-apply-config
Requires:       os-net-config
Requires:       os-refresh-config
Requires:       python-heat-agent
Requires:       puppet
Requires:       openstack-puppet-modules
Requires:       python-six
Requires:       python-keystoneclient >= 3.8.0
Requires:       python-ironicclient >= 1.14.0
Requires:       python-mistralclient >= 3.1.0
Requires:       python-novaclient >= 1:9.0.0
Requires:       python-swiftclient >= 3.2.0
Requires:       python-netaddr
Requires:       python-netifaces

Requires:       selinux-policy

%description
instack-undercloud is a collection of installation tools to install an
undercloud via python-instack. It contains scripts and elements to complete the
installation.

%package container
Summary:        Components required for a containerized undercloud

# Required for containerized undercloud
Requires:       instack-undercloud
Requires:       openstack-tripleo-common
Requires:       docker
Requires:       docker-distribution
Requires:       python-ipaddr
Requires:       openvswitch
Requires:       openstack-heat-api
Requires:       openstack-heat-engine
Requires:       openstack-heat-agents
# required as we now use --heat-native
Requires:       openstack-heat-monolith

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
