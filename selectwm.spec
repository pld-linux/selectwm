Summary:	selectwm, select a window manager at X startup
Summary(pl):	selectwm - wybór zarz±dcy okien przy starcie X
Name:		selectwm
Version:	0.4
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://ordiluc.net/selectwm/%{name}-%{version}.tar.bz2
Patch0:		%{name}-am_fixes.patch
URL:		http://ordiluc.net/selectwm/
BuildRequires:	autoconf
BuildRequires:	automake
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

%description -l pl
selectwm to prosty, ale u¿yteczny program, który pozwala wybraæ
menad¿era okien (lub inny program) do uruchomienia przy starcie X oraz
opcjonalnie po zakoñczeniu menad¿era okien. U¿ywa toolkitu GTK+ i ma
takie opcje, jak czas po którym uruchamia domy¶lnego menad¿era oraz
modyfikowanie listy zarz±dców okien z programu.

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/selectwm
%{_mandir}/man1/*
