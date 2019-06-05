#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : iptraf
Version  : 3.0.0
Release  : 20
URL      : ftp://iptraf.seul.org/pub/iptraf/iptraf-3.0.0.tar.gz
Source0  : ftp://iptraf.seul.org/pub/iptraf/iptraf-3.0.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: iptraf-bin
BuildRequires : libc6-dev
BuildRequires : pkgconfig(ncurses)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: iptraf-header-file-location.patch
Patch2: iptraf-makefile.patch

%description
==========================================================================
--------------------------------------------------------------------------
See the RELEASE-NOTES for important update information.
See the INSTALL file for installation instructions.
--------------------------------------------------------------------------

%package bin
Summary: bin components for the iptraf package.
Group: Binaries

%description bin
bin components for the iptraf package.


%prep
%setup -q -n iptraf-3.0.0
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517970662
pushd src
make  %{?_smp_mflags} V=1 CFLAGS="$CFLAGS"
popd

%install
export SOURCE_DATE_EPOCH=1517970662
rm -rf %{buildroot}
pushd src
%make_install
popd
## make_install_append content
mkdir -p %{buildroot}/usr
mv %{buildroot}/bin %{buildroot}/usr/bin
chmod a+x %{buildroot}/usr/bin
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/iptraf
/usr/bin/rvnamed
