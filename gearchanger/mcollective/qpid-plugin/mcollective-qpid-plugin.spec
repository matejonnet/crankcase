Summary:        Plugin to enable m-collective communication over amqp 1.0 enabled broker
Name:           mcollective-qpid-plugin
Version:        0.0.1
Release:        1%{?dist}
Group:          Development/Languages
License:        ASL 2.0
URL:            http://openshift.redhat.com
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       mcollective
Requires:       ruby-qpid-qmf
BuildArch:      noarch

%description
m-collective communication plugin for amqp 1.0 enabled qpid broker

%prep
%setup -q

%clean
rm -rf %{buildroot}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/libexec/mcollective/mcollective/connector/
cp src/qpid.rb %{buildroot}/usr/libexec/mcollective/mcollective/connector/

%files
%defattr(-,root,root,-)
/usr/libexec/mcollective/mcollective/connector/qpid.rb

%changelog
* Wed May 30 2012 Krishna Raman <kraman@gmail.com> 0.0.1-1
- new package built with tito

* Fri May 25 2012 Krishna Raman <kraman@gmail.com> 0.0.1-1
- new package built with tito

* Fri May 25 2012 Krishna Raman <kraman@gmail.com> 0.0.1-1
- new package built with tito

