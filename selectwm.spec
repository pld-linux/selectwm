Summary:	selectwm, select a window manager at X startup
Name:		selectwm
Version:	0.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ordiluc.net/selectwm/%{name}-%{version}.tar.bz2
Patch0:		%{name}-am_fixes.patch
URL:		http://ordiluc.net/selectwm/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gtk+2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
selectwm is a simple but robust program that will let you pick a
window manager (or other executable) to run at X startup, and
optionally after a window manager exits. It uses the GTK+ toolkit, and
includes options like a timer to start the default window manager, and
modification of the window manager list from within %{name}.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/selectwm
%{_mandir}/man1/*
