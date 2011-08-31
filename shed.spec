#
Summary:	shed - a simple hex editor
Summary(pl.UTF-8):	Prosty hex-edytor
Name:		shed
Version:	1.15
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/shed/%{name}-%{version}.tar.gz
# Source0-md5:	c7d7d464d6b4fa28a7980270d03e0906
Patch0:		%{name}-autoconf.patch
URL:		http://shed.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
shed is an easy to use hex editor written for unix/linux using
ncurses, with a friendly pico-style interface.

%description -l pl.UTF-8
shed jest prostym hex-edytorem przeznaczonym dla systemów typu Unix,
wykorzystującym bibliotekę ncurses. Interfejs użytkownika sheda jest
wzorowany na pico.

%prep
%setup -q

%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/shed
%{_mandir}/man1/shed.1*
