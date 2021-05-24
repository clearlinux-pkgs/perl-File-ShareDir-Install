#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-ShareDir-Install
Version  : 0.13
Release  : 22
URL      : http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/File-ShareDir-Install-0.13.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/File-ShareDir-Install-0.13.tar.gz
Summary  : 'Install shared files'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-ShareDir-Install-license = %{version}-%{release}
Requires: perl-File-ShareDir-Install-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution File-ShareDir-Install,
version 0.13:
Install shared files

%package dev
Summary: dev components for the perl-File-ShareDir-Install package.
Group: Development
Provides: perl-File-ShareDir-Install-devel = %{version}-%{release}
Requires: perl-File-ShareDir-Install = %{version}-%{release}

%description dev
dev components for the perl-File-ShareDir-Install package.


%package license
Summary: license components for the perl-File-ShareDir-Install package.
Group: Default

%description license
license components for the perl-File-ShareDir-Install package.


%package perl
Summary: perl components for the perl-File-ShareDir-Install package.
Group: Default
Requires: perl-File-ShareDir-Install = %{version}-%{release}

%description perl
perl components for the perl-File-ShareDir-Install package.


%prep
%setup -q -n File-ShareDir-Install-0.13
cd %{_builddir}/File-ShareDir-Install-0.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-ShareDir-Install
cp %{_builddir}/File-ShareDir-Install-0.13/LICENSE %{buildroot}/usr/share/package-licenses/perl-File-ShareDir-Install/58243c3de2463126a3a838b6c161fc3b11678eaa
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::ShareDir::Install.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-ShareDir-Install/58243c3de2463126a3a838b6c161fc3b11678eaa

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/File/ShareDir/Install.pm
