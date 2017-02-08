%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:		instack-undercloud
Version:	XXX
Release:	XXX
Summary:	Installation tools to install an undercloud via instack

Group:		Development/Languages
License:	ASL 2.0
Url:		https://github.com/openstack/instack-undercloud
Source0:	https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:	noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  git
Requires:	instack
Requires:	openstack-tripleo-heat-templates
Requires:	openstack-tripleo-image-elements
Requires:	redhat-lsb-core
Requires:	policycoreutils-python
Requires:	openstack-heat-templates
Requires:	openstack-tripleo-puppet-elements
Requires:	python-psutil
Requires:	pystache
Requires:	jq
Requires:	os-net-config
Requires:	os-cloud-config
Requires:	python-heat-agent
Requires:	puppet
Requires:	openstack-puppet-modules

Requires:	selinux-policy

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