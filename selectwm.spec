Summary:	selectwm, select a window manager at X startup
Summary(pl):	selectwm - wybór zarz±dcy okien przy starcie X
Name:		selectwm
Version:	0.4.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ordiluc.net/selectwm/%{name}-%{version}.tar.bz2
# Source0-md5:	160199961c552922b5880ebf7e201c3c
Patch0:		%{name}-am_fixes.patch
URL:		http://ordiluc.net/selectwm/
BuildRequires:	pkgconfig
BuildRequires:  glib2 >= 2.0.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
selectwm is a simple but robust program that will let you pick a
window manager (or other executable) to run at X startup, and
optionally after a window manager exits. It uses the GTK+ toolkit, and
includes options like a timer to start the default window manager, and
modification of the window manager list from within selectwm.

%description -l pl
selectwm to prosty, ale u¿yteczny program, który pozwala wybraæ
zarz±dcê okien (lub inny program) do uruchomienia przy starcie X oraz
opcjonalnie po zakoñczeniu dzia³ania zarz±dcy okien. U¿ywa biblioteki
narzêdziowej GTK+ i ma takie opcje, jak czas po którym uruchamia
domy¶lnego zarz±dcê okien oraz modyfikowanie listy zarz±dców okien z
programu.

%prep
%setup -q
%patch0 -p0

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/selectwm
%{_mandir}/man1/*
