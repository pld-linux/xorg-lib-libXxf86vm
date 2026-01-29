Summary:	XFree86-VidMode X extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia X XFree86-VidMode
Name:		xorg-lib-libXxf86vm
Version:	1.1.7
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXxf86vm-%{version}.tar.xz
# Source0-md5:	bea9e3707fae6c3275769e771006fa0f
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel >= 1.6
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86vidmodeproto-devel >= 2.2.99.1
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libX11 >= 1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XFree86-VidMode X extension library.

%description -l pl.UTF-8
Biblioteka rozszerzenia X XFree86-VidMode.

%package devel
Summary:	Header files for libXxf86vm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXxf86vm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel >= 1.6
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-xf86vidmodeproto-devel >= 2.2.99.1

%description devel
XFree86-VidMode X extension library.

This package contains the header files needed to develop programs that
use libXxf86vm.

%description devel -l pl.UTF-8
Biblioteka rozszerzenia X XFree86-VidMode.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXxf86vm.

%package static
Summary:	Static libXxf86vm library
Summary(pl.UTF-8):	Biblioteka statyczna libXxf86vm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
XFree86-VidMode X extension library.

This package contains the static libXxf86vm library.

%description static -l pl.UTF-8
Biblioteka rozszerzenia X XFree86-VidMode.

Pakiet zawiera statyczną bibliotekę libXxf86vm.

%prep
%setup -q -n libXxf86vm-%{version}

# support __libmansuffix__ with "x" suffix (per FHS 2.3)
%{__sed} -i -e 's,\.so man__libmansuffix__/,.so man3/,' man/*.man

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libXxf86vm.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_libdir}/libXxf86vm.so.*.*.*
%ghost %{_libdir}/libXxf86vm.so.1

%files devel
%defattr(644,root,root,755)
%{_libdir}/libXxf86vm.so
%{_includedir}/X11/extensions/xf86vmode.h
%{_pkgconfigdir}/xxf86vm.pc
%{_mandir}/man3/XF86VM.3*
%{_mandir}/man3/XF86VidMode*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXxf86vm.a
