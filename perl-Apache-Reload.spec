%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	Reload
Summary:	Reload changed modules
Summary(pl):	Prze�adowywanie zmodyfikowanych w trakcie pracy Apache'a modu��w
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
Ten modu� to dwie rzeczy. Pierwsza to adaptacja modu�u
Stonehenge::Reload napisanego przez Randala Schwartza, pr�buj�ca by�
nieco bardziej intuicyjna i u�atwiaj�ca u�ywanie. Stonehenge::Reload
zosta� napisany, aby poszczeg�lne modu�y si� prze�adowywa�y, kiedy
zostan� zmienione. W przeciwie�stwie do Apache::StatINC modu�
Stonehenge::Reload sprawdza� tylko czas zmiany modu��w, kt�re si�
zarejestrowa�y przy u�yciu Stonehenge::Reload, redukuj�c liczb�
wywo�a� stat(). Apache::Reload ponadto oferuje t� sam� funkcjonalno��
co Apache::StatINC i jest zaprojektowany tak, aby by� zamiennikiem.
Apache::Reload sprawdza tylko modu�y, kt�re si� zarejestrowa�y przy
u�yciu Apache::Reaload tylko je�li emulacja StatINC zosta�a wy��czona.
Podobnie jak Apache::StatINC Apache::Reload musi by� zainstalowany
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
