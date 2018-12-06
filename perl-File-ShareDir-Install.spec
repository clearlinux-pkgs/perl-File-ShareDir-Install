#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-ShareDir-Install
Version  : 0.13
Release  : 9
URL      : http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/File-ShareDir-Install-0.13.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/File-ShareDir-Install-0.13.tar.gz
Summary  : 'Install shared files'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-ShareDir-Install-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution File-ShareDir-Install,
version 0.13:
Install shared files

%package dev
Summary: dev components for the perl-File-ShareDir-Install package.
Group: Development
Provides: perl-File-ShareDir-Install-devel = %{version}-%{release}

%description dev
dev components for the perl-File-ShareDir-Install package.


%package license
Summary: license components for the perl-File-ShareDir-Install package.
Group: Default

%description license
license components for the perl-File-ShareDir-Install package.


%prep
%setup -q -n File-ShareDir-Install-0.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-ShareDir-Install
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-File-ShareDir-Install/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/File/ShareDir/Install.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::ShareDir::Install.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-ShareDir-Install/LICENSE
