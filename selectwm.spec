Summary:	selectwm, select a window manager at X startup
Name:		selectwm
Version:	0.4
Release:	0.2
License:	GPL
URL:		http://ordiluc.net/selectwm
Group:		X11/Applications
BuildRequires:	gtk+2-devel
Source0:	%{name}-%{version}.tar.gz
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _mandir         %{_prefix}/man

%description
selectwm is a simple but robust program that will let you pick a
window manager (or other executable) to run at X startup, and
optionally after a window manager exits. It uses the GTK+ toolkit, and
includes options like a timer to start the default window manager, and
modification of the window manager list from within %{name}.

%prep

%setup -q

%build
CFLAGS="%{rpmcflags}"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__make} install DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/selectwm
%{_mandir}/man1/*
