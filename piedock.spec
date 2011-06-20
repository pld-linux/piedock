Summary:	A task bar and application launcher in shape of a pie menu
Name:		piedock
Version:	1.3.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://www.markusfisch.de/downloads/PieDock-%{version}.tar.bz2
# Source0-md5:	45b3a86eb50c783fecedf4c57163fbc7
URL:		http://www.markusfisch.de/PieDock
BuildRequires:	freetype-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PieDock is a task bar and application launcher in shape of a pie menu.
It feels a little bit like the famous OS X dock in a circle.

%prep
%setup -q -n PieDock-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README res/PieDockrc.sample
%attr(755,root,root) %{_bindir}/PieDock*
