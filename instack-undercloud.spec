Name:		instack-undercloud
Version:	XXX
Release:	XXX%{?dist}
Summary:	Installation tools to install an undercloud via instack

Group:		Development/Languages
License:	ASL 2.0
Url:		https://github.com/rdo-management/instack-undercloud
Source0:	https://github.com/rdo-management/instack-undercloud/archive/%{version}.tar.gz

BuildArch:	noarch

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
%setup -q -n %{name}-%{upstream_version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}


%files
%doc README.md
%doc LICENSE
%{_datadir}/instack-undercloud
%{_bindir}/instack-*
%{python_sitelib}/instack_undercloud*

%changelog
