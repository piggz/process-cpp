#
# spec file for package process-cpp
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           process-cpp
Version:	    3.0.1
Release:	    0
License:    	LGPL-3.0	
Summary:	    A simple convenience library for handling processes in C++11
Url:	        https://launchpad.net/process-cpp
Group:	        System/Libraries
Source:	        %{name}_%{version}.orig.tar.gz
Patch:	        no-gtest.patch
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	boost-devel
BuildRequires:	pkgconfig
BuildRequires:	properties-cpp-devel
BuildRequires:	doxygen
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A simple convenience library for handling processes in C++11.

%package -n libprocess-cpp3
Summary:	C++11 library for handling processes - runtime library
Group:	        System/Libraries

%description -n libprocess-cpp3
A simple convenience library for handling processes in C++11.

This package provides shared libraries for process-cpp.

%package devel
Summary:	Development headers for process-cpp
Group:	        Development/Libraries/C and C++
Requires:	libprocess-cpp3 = %{version}
Requires:	properties-cpp-devel

%description devel
A simple convenience library for handling processes in C++11.

This package provides development headers for process-cpp.

%prep
%setup -q %{name}/%{name}
%patch -p1

%build
mkdir -p build
cd build
%cmake -Wno-dev ../%{name}
make %{?_smp_mflags}

%install
cd build
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%post -n libprocess-cpp3 -p /sbin/ldconfig

%postun -n libprocess-cpp3 -p /sbin/ldconfig

%files -n libprocess-cpp3
%defattr(-,root,root)
%{_libdir}/libprocess-cpp.so.3
%{_libdir}/libprocess-cpp.so.3.0.0

%files devel
%defattr(-,root,root)
%{_includedir}/core
%{_libdir}/libprocess-cpp.so
%{_libdir}/pkgconfig/process-cpp.pc
%{_docdir}/%{name}
