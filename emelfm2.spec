Summary:	File manager using the two-pane design and Gtk+
Summary(pl):	Zarz�dca plik�w oparty na bibliotece GTK+
Name:		emelfm2
Version:	0.1.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://emelfm2.net/rel/%{name}-%{version}.tar.gz
# Source0-md5:	da39b1d017366fb41700c5d40365a1ae
URL:		http://emelfm.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
emelFM is a file manager that implements the popular two-pane design.
It features a simple GTK+ interface, a flexible filetyping scheme, and
a built-in command line for executing commands without opening an
xterm.

%description -l pl
emelFM2 jest klasycznym, dwupanelowym zarz�dc� plik�w. Ma prosty
interfejs graficzny oparty o bibliotek� GTK+.

%prep
%setup  -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name},%{_desktopdir}}
install emelfm2 $RPM_BUILD_ROOT%{_bindir}
install plugins/* $RPM_BUILD_ROOT%{_libdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%dir (755,root,root) %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*
