
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:		instack-undercloud
Version:	4.2.1
Release:	1%{?dist}
Summary:	Installation tools to install an undercloud via instack

Group:		Development/Languages
License:	ASL 2.0
Url:		https://github.com/openstack/instack-undercloud
Source0:	https://github.com/openstack/instack-undercloud/archive/%{version}%{?milestone}.tar.gz

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
* Tue May 23 2017 Alfredo Moralejo <amoralej@redhat.com> 4.2.1-1
- Update to 4.2.1

* Fri Jun 17 2016 Haikel Guemar <hguemar@fedoraproject.org> 4.1.0-1
- Update to 4.1.0

* Wed Mar 30 2016 RDO <rdo-list@redhat.com> 4.0.0-1
- RC1 Rebuild for Mitaka RC1 
