Summary:	Xxf86vm library
Summary(pl):	Biblioteka Xxf86vm
Name:		xorg-lib-libXxf86vm
Version:	1.0.0
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC4/lib/libXxf86vm-%{version}.tar.bz2
# Source0-md5:	c6018b25cf965cb70ed44c9e7036ccda
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-xf86vidmodeproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xxf86vm library.

%description -l pl
Biblioteka Xxf86vm.

%package devel
Summary:	Header files for libXxf86vm library
Summary(pl):	Pliki nag³ówkowe biblioteki libXxf86vm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-xf86vidmodeproto-devel

%description devel
Xxf86vm library.

This package contains the header files needed to develop programs that
use libXxf86vm.

%description devel -l pl
Biblioteka Xxf86vm.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXxf86vm.

%package static
Summary:	Static libXxf86vm library
Summary(pl):	Biblioteka statyczna libXxf86vm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Xxf86vm library.

This package contains the static libXxf86vm library.

%description static -l pl
Biblioteka Xxf86vm.

Pakiet zawiera statyczn± bibliotekê libXxf86vm.

%prep
%setup -q -n libXxf86vm-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXxf86vm.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXxf86vm.so
%{_libdir}/libXxf86vm.la
%{_pkgconfigdir}/xxf86vm.pc
%{_mandir}/man3/*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXxf86vm.a
