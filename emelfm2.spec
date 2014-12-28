Summary:	File manager using the two-pane design and Gtk+
Summary(pl.UTF-8):	Zarządca plików oparty na bibliotece GTK+
Name:		emelfm2
Version:	0.8.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://emelfm2.net/rel/%{name}-%{version}.tar.bz2
# Source0-md5:	8490d501e19009860f53ac6a98db74c1
URL:		http://emelfm2.net/
BuildRequires:	gettext-tools
BuildRequires:	gcc >= 5:3.2
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	pkgconfig
Requires:	file >= 4
Requires:	findutils >= 4.2
Requires:	grep
Requires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
emelFM is a file manager that implements the popular two-pane design.
It features a simple GTK+ interface, a flexible filetyping scheme, and
a built-in command line for executing commands without opening an
xterm.

%description -l pl.UTF-8
emelFM2 jest klasycznym, dwupanelowym zarządcą plików. Ma prosty
interfejs graficzny oparty o bibliotekę GTK+.

%prep
%setup -q
sed -i "s@GTK3=.*@GTK3=0@ ; s@GLIB3=.*@GLIB3=0@" Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="-ldl %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}}

install emelfm2 $RPM_BUILD_ROOT%{_bindir}
install objs/plugins/*.so $RPM_BUILD_ROOT%{_libdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so
