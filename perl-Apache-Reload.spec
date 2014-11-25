%define		pdir	Apache
%define		pnam	Reload
%include	/usr/lib/rpm/macros.perl
Summary:	Reload changed modules
Summary(pl.UTF-8):	Przeładowywanie zmodyfikowanych w trakcie pracy Apache'a modułów
Name:		perl-Apache-Reload
Version:	0.11
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ec02f93aeef08f2d9e6734645a131a21
URL:		http://search.cpan.org/dist/Apache-Reload/
BuildRequires:	perl-Apache-Test
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

%description -l pl.UTF-8
Ten moduł to dwie rzeczy. Pierwsza to adaptacja modułu
Stonehenge::Reload napisanego przez Randala Schwartza, próbująca być
nieco bardziej intuicyjna i ułatwiająca używanie. Stonehenge::Reload
został napisany, aby poszczególne moduły się przeładowywały, kiedy
zostaną zmienione. W przeciwieństwie do Apache::StatINC moduł
Stonehenge::Reload sprawdzał tylko czas zmiany modułów, które się
zarejestrowały przy użyciu Stonehenge::Reload, redukując liczbę
wywołań stat(). Apache::Reload ponadto oferuje tą samą funkcjonalność
co Apache::StatINC i jest zaprojektowany tak, aby być zamiennikiem.
Apache::Reload sprawdza tylko moduły, które się zarejestrowały przy
użyciu Apache::Reaload tylko jeśli emulacja StatINC została wyłączona.
Podobnie jak Apache::StatINC Apache::Reload musi być zainstalowany
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
%{perl_vendorlib}/Apache2/Reload.pm
%{_mandir}/man3/*
