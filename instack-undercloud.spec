%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:		instack-undercloud
Version:	7.4.12
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
Requires:	python-oslo-config >= 2:4.0.0
Requires:	pystache
Requires:	jq
Requires:	os-apply-config
Requires:	os-net-config
Requires:	os-refresh-config
Requires:	python-heat-agent
Requires:	puppet
Requires:	openstack-puppet-modules
Requires:	python-six
Requires:	python-keystoneclient >= 3.8.0
Requires:	python-ironicclient >= 1.14.0
Requires:	python-mistralclient >= 3.1.0
Requires:	python-novaclient >= 1:9.0.0
Requires:	python-swiftclient >= 3.2.0
Requires:	python-netaddr
Requires:   python-netifaces

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
* Tue May 29 2018 RDO <dev@lists.rdoproject.org> 7.4.12-1
- Update to 7.4.12

* Tue Mar 27 2018 RDO <dev@lists.rdoproject.org> 7.4.11-1
- Update to 7.4.11

* Wed Mar 07 2018 RDO <dev@lists.rdoproject.org> 7.4.10-1
- Update to 7.4.10

* Mon Feb 12 2018 RDO <dev@lists.rdoproject.org> 7.4.9-1
- Update to 7.4.9

* Wed Jan 24 2018 RDO <dev@lists.rdoproject.org> 7.4.8-1
- Update to 7.4.8

* Mon Jan 08 2018 RDO <dev@lists.rdoproject.org> 7.4.7-1
- Update to 7.4.7

* Sat Dec 09 2017 RDO <dev@lists.rdoproject.org> 7.4.6-1
- Update to 7.4.6

* Wed Nov 22 2017 RDO <dev@lists.rdoproject.org> 7.4.5-1
- Update to 7.4.5

* Tue Nov 14 2017 RDO <dev@lists.rdoproject.org> 7.4.4-1
- Update to 7.4.4

* Fri Nov 03 2017 RDO <dev@lists.rdoproject.org> 7.4.3-1
- Update to 7.4.3

* Tue Oct 10 2017 rdo-trunk <javier.pena@redhat.com> 7.4.2-1
- Update to 7.4.2

* Wed Oct 04 2017 rdo-trunk <javier.pena@redhat.com> 7.4.1-1
- Update to 7.4.1

* Sun Sep 10 2017 rdo-trunk <javier.pena@redhat.com> 7.4.0-1
- Update to 7.4.0

* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 7.3.0-1
- Update to 7.3.0

