%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:		instack-undercloud
Version:	5.3.2
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
Requires:	openstack-tripleo
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

%changelog
* Thu Oct 05 2017 rdo-trunk <javier.pena@redhat.com> 5.3.2-1
- Update to 5.3.2

* Mon Sep 04 2017 rdo-trunk <javier.pena@redhat.com> 5.3.1-1
- Update to 5.3.1

* Thu Apr 27 2017 rdo-trunk <javier.pena@redhat.com> 5.3.0-1
- Update to 5.3.0

* Wed Jan 04 2017 Jon Schlueter <jschluet@redhat.com> 5.2.0-1
- Update to 5.2.0

* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 5.1.0-1
- Update to 5.1.0

* Thu Oct 20 2016 Haikel Guemar <hguemar@fedoraproject.org> 5.0.0-1
- Update to 5.0.0

* Tue Oct 18 2016 Alfredo Moralejo <amoralej@redhat.com> 5.0.0-0.3.0rc3
- Update to 5.0.0.0rc3

* Thu Sep 29 2016 Haikel Guemar <hguemar@fedoraproject.org> 5.0.0-0.2.0rc2
- Update to 5.0.0.0rc2

* Wed Sep 14 2016 Haikel Guemar <hguemar@fedoraproject.org> 5.0.0-0.1.0b3
- Update to 5.0.0.0b3

