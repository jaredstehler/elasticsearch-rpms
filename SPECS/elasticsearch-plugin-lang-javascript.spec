%define debug_package %{nil}
%define base_install_dir %{_javadir}/elasticsearch

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-lang-javascript
Version:        1.3.0
Release:        2%{?dist}
Summary:        ElasticSearch plugin to use Javascript for script execution

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/elasticsearch/elasticsearch-lang-javascript

Source0:        https://download.elasticsearch.org/elasticsearch/elasticsearch-lang-javascript/elasticsearch-lang-javascript-1.1.0.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       elasticsearch >= 0.90.0

%description
The Groovy language plugin allows to have javascript
as the language of scripts to execute.

%prep
rm -fR %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
cd %{name}-%{version}
%{__mkdir} -p plugins
unzip %{SOURCE0} -d plugins/lang-javascript

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins
%{__install} -D -m 755 plugins/lang-javascript/elasticsearch-lang-javascript-%{version}.jar %{buildroot}/%{base_install_dir}/plugins/lang-javascript/elasticsearch-lang-javascript.jar
%{__install} -D -m 755 plugins/lang-javascript/rhino-1.7R3.jar -t %{buildroot}/%{base_install_dir}/plugins/lang-javascript/

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/lang-javascript
%{base_install_dir}/plugins/lang-javascript/*

%changelog
* Tue Nov 27 2012 Tavis Aitken tavisto@tavisto.net 1.1.0-2
- Fixed base_install_dir

* Wed Mar 21 2012 Tavis Aitken tavisto@tavisto.net 1.1.0-1
- Tweaked to make the package conform to fedora build specs

* Tue Feb 22 2012 Sean Laurent 1.1.0-0
- Initial package

