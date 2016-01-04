%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name net-scp

Summary: A pure Ruby implementation of the SCP client protocol
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.2.1
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/net-ssh/net-scp
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(net-ssh) >= 2.5.6
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
#BuildRequires: %{?scl_prefix}rubygem(net-ssh)
#BuildRequires: %{?scl_prefix_ror}rubygem(mocha)
#BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A pure Ruby implementation of the SCP client protocol

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
# We don't have test/unit nor compatible minitest version
#ruby -Itest test/test_all.rb
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.travis.yml
%{gem_libdir}
%doc %{gem_instdir}/LICENSE.txt
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/Manifest
%{gem_instdir}/Rakefile
%{gem_instdir}/net-scp.gemspec
%{gem_instdir}/gem-public_cert.pem
%exclude %{gem_instdir}/setup.rb
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGES.txt
%{gem_instdir}/test
%doc %{gem_docdir}

%changelog
* Fri Jun 05 2015 Josef Stribny <jstribny@redhat.com> - 1.2.1-3
- Disable tests due to test/unit requirement

* Thu Oct 16 2014 Josef Stribny <jstribny@redhat.com> - 1.2.1-2
- Add SCL macros

* Tue Jun 17 2014 Vít Ondruch <vondruch@redhat.com> - 1.2.1-1
- Update to net-scp 1.2.1.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 09 2013 Vít Ondruch <vondruch@redhat.com> - 1.1.0-1
- Update to net-scp 1.1.0.

* Fri Mar 08 2013 Vít Ondruch <vondruch@redhat.com> - 1.0.4-7
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.4-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 17 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.4-2
- Removed obsolete cleanup.
- Removed explicit requires.

* Tue Feb 08 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.4-1
- Initial package
