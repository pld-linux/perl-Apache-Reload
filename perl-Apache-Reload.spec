%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	Reload
Summary:	Reload changed modules
Summary(pl):	Prze³adowywanie zmodyfikowanych w trakcie pracy Apache'a modu³ów
Name:		perl-Apache-Reload
Version:	0.07
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	68a57f98e5c140117cceded434df1a0a
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is two things. First it is an adaptation of Randal
Schwartz's Stonehenge::Reload module that attempts to be a little more
intuitive and makes the usage easier. Stonehenge::Reload was written
by Randal to make specific modules reload themselves when they
changed. Unlike Apache::StatINC, Stonehenge::Reload only checked the
change time of modules that registered themselves with
Stonehenge::Reload, thus reducing stat() calls. Apache::Reload also
offers the exact same functionality as Apache::StatINC, and is thus
designed to be a drop-in replacement. Apache::Reload only checks
modules that register themselves with Apache::Reload if you explicitly
turn off the StatINC emulation method (see below). Like
Apache::StatINC, Apache::Reload must be installed as an Init Handler.

%description -l pl
Ten modu³ to dwie rzeczy. Pierwsza to adaptacja modu³u
Stonehenge::Reload napisanego przez Randala Schwartza, próbuj±ca byæ
nieco bardziej intuicyjna i u³atwiaj±ca u¿ywanie. Stonehenge::Reload
zosta³ napisany, aby poszczególne modu³y siê prze³adowywa³y, kiedy
zostan± zmienione. W przeciwieñstwie do Apache::StatINC modu³
Stonehenge::Reload sprawdza³ tylko czas zmiany modu³ów, które siê
zarejestrowa³y przy u¿yciu Stonehenge::Reload, redukuj±c liczbê
wywo³añ stat(). Apache::Reload ponadto oferuje t± sam± funkcjonalno¶æ
co Apache::StatINC i jest zaprojektowany tak, aby byæ zamiennikiem.
Apache::Reload sprawdza tylko modu³y, które siê zarejestrowa³y przy
u¿yciu Apache::Reaload tylko je¶li emulacja StatINC zosta³a wy³±czona.
Podobnie jak Apache::StatINC Apache::Reload musi byæ zainstalowany
jako Init Handler.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
