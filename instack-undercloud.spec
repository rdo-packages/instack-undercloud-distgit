%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:		instack-undercloud
Version:	6.1.3
Release:	1%{?dist}
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
Requires:	openstack-tripleo-puppet-elements
Requires:	python-psutil
Requires:	python-oslo-config
Requires:	pystache
Requires:	jq
Requires:	os-apply-config
Requires:	os-net-config
Requires:	os-cloud-config
Requires:	os-refresh-config
Requires:	python-heat-agent
Requires:	puppet
Requires:	openstack-puppet-modules
Requires:	python-six
Requires:	python-keystoneclient
Requires:	python-mistralclient
Requires:	python-novaclient
Requires:	python-netaddr

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
* Wed Nov 22 2017 RDO <dev@lists.rdoproject.org> 6.1.3-1
- Update to 6.1.3

* Fri Nov 03 2017 RDO <dev@lists.rdoproject.org> 6.1.2-1
- Update to 6.1.2

* Mon Sep 04 2017 rdo-trunk <javier.pena@redhat.com> 6.1.1-1
- Update to 6.1.1

* Fri Apr 28 2017 rdo-trunk <javier.pena@redhat.com> 6.1.0-1
- Update to 6.1.0

* Wed Mar 08 2017 Alfredo Moralejo <amoralej@redhat.com> 6.0.0-1
- Update to 6.0.0

* Mon Mar 06 2017 Alfredo Moralejo <amoralej@redhat.com> 6.0.0-0.2.0rc2
- Update to 6.0.0.0rc2

* Fri Feb 17 2017 Alfredo Moralejo <amoralej@redhat.com> 6.0.0-0.1.0rc1
- Update to 6.0.0.0rc1

