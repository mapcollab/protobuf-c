Name:           protobuf-c
Version:        1.2.1
Release:        1%{?dist}
Summary:        C bindings for Google's Protocol Buffers


Group:          System Environment/Libraries
License:        BSD
URL:            https://github.com/protobuf-c/protobuf-c
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  protobuf-devel
BuildRequires:  protobuf-compiler

%description
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. This package provides a code generator and run-time
libraries to use Protocol Buffers from pure C (not C++).

%package compiler
Summary: Protocol Buffers C compiler
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description compiler
This package contains a modified version of the Protocol Buffers
compiler for the C programming language called protoc-c.

%package devel
Summary:        Protocol Buffers C headers and libraries
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-compiler = %{version}-%{release}

%description devel
This package contains protobuf-c headers and libraries.

%prep
%setup -q

%build
./autogen.sh
%configure --disable-static
# disabled parallel build due to https://github.com/protobuf-c/protobuf-c/issues/156
make

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/libprotobuf-c.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libprotobuf-c.so.*
%doc TODO LICENSE ChangeLog

%files compiler
%defattr(-,root,root,-)
%{_bindir}/protoc-c

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/google
%{_includedir}/protobuf-c
%{_includedir}/google/protobuf-c
%{_libdir}/libprotobuf-c.so
%{_libdir}/pkgconfig/libprotobuf-c.pc

%changelog
* Wed Feb 10 2016 Tomasz Rostanski <tomasz.rostanski@thalesgroup.com> 1.2.1-1
- Initial build 

* Mon Aug 17 2015 Adrian Reber <areber@redhat.com> - 1.0.2-2
- remove 'ExcludeArch' hack

* Fri Jul 17 2015 Adrian Reber <areber@redhat.com> - 1.0.2-1
- new upstream release
- split off protoc-c into protobuf-c-compiler to reduce runtime
  dependencies of the main package

* Wed Aug 06 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.0.1-1
- new upstream release

* Mon Aug 04 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.0.0-1
- new upstream release (#1126116)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 David Robinson <zxvdr.au@gmail.com> - 0.15-7
- rebuilt for protobuf-2.5.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 12 2011 David Robinson <zxvdr.au@gmail.com> - 0.15-3
- rebuilt for protobuf-2.4.1

* Sun Apr 24 2011 David Robinson <zxvdr.au@gmail.com> - 0.15-2
- Spec file cleanup

* Wed Apr 20 2011 David Robinson <zxvdr.au@gmail.com> - 0.15-1
- New upstream release
- Spec file cleanup

* Mon Jan 17 2011 Bobby Powers <bobby@laptop.org> - 0.14-1
- New upstream release
- Removed -devel dependency on protobuf-devel
- Small specfile cleanups

* Wed May 19 2010 David Robinson <zxvdr.au@gmail.com> - 0.13-2
- Spec file cleanup

* Wed May 19 2010 David Robinson <zxvdr.au@gmail.com> - 0.13-1
- Initial packaging
