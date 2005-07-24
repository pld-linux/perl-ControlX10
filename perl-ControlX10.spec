#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	ControlX10
%define		pnam	CM11
Summary:	Control X10 via CM11A device
Summary(pl):	Obs³uga X10 przez urz±dzenie CM11A
Name:		perl-ControlX10
Version:	2.09
Release:	0.1
License:	same as perl
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b59c85e92eae2c14ffa63af7ac0a1d9a
URL:		http://search.cpan.org/~bbirth/ControlX10-CM11-2.09/CM11.pm
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
The CM11A is a bi-directional X10 controller that connects to a serial
port and transmits commands via AC power line to X10 devices. This
module translates human-readable commands (eg. 'A2', 'AJ') into the
Interface Communication Protocol accepted by the CM11A.

%description -l pl
CM11A jest dwukierunkowym kontrolerem X10 pod³±czanym do portu
szeregowego. Steruje on urz±dzeniami zgodnymi z X10 transmituj±c
polecenia po linni zasilania AC. Ten modu³ t³umaczy polecenia z
postaci czytelnej dla cz³owieka (np 'A2', 'AJ') na polecenia
interfejsu ICP akcepotowalne przez CM11A.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
# Don't use pipes here: they generally don't work. Apply a patch.
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
# use macros:
%{perl_vendorlib}/ControlX10/CM11.pm
#%%{perl_vendorarch}/...
%{_mandir}/man3/*
