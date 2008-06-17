%define module Gnome2-VFS
%define fmodule Gnome2/VFS

Summary: Perl module for the gnome2-2.x VFS libraries
Name:    perl-%module
Version: 1.081
Release: %mkrel 2
License: GPL or Artistic
Group:   Development/GNOME and GTK+
# http://sourceforge.net/project/showfiles.php?group_id=64773&package_id=102457
Source:  %module-%version.tar.bz2
URL: http://gtk2-perl.sf.net/
BuildRequires: libgnome-vfs2-devel => 2.6, perl-Glib => 1.00, perl-Gtk2
BuildRequires: perl-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig 
Requires: perl-Glib >= 1.00, libgnome-vfs2 >= 2.6
Conflicts: drakxtools < 9.1-15mdk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module provides perl access to GNOME-2.x VFS libraries.

The GNOME Virtual File System provides an abstraction to common file
system operations like reading, writing and copying files, listing
directories and so on.

%prep
%setup -q -n %module-%version
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
export GTK2_PERL_CFLAGS="$RPM_OPT_FLAGS"
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc LICENSE examples/*
%{_mandir}/*/*
%{perl_vendorarch}/%fmodule
%{perl_vendorarch}/%fmodule.pm
%{perl_vendorarch}/auto/%fmodule


