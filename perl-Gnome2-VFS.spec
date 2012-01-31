%define	module	Gnome2-VFS
%define	fmodule	Gnome2/VFS

Summary:	Perl module for the gnome2-2.x VFS libraries
Name:		perl-%{module}
Version:	1.081
Release:	9
License:	LGPLv2.1+
Group:		Development/GNOME and GTK+
# http://sourceforge.net/project/showfiles.php?group_id=64773&package_id=102457
Source0:	%{module}-%{version}.tar.bz2
URL:		http://gtk2-perl.sf.net/
BuildRequires:	pkgconfig(gnome-vfs-2.0) perl-Glib => 1.00, perl-Gtk2
BuildRequires:	perl-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig 
Requires:	perl-Glib >= 1.00 pkgconfig(gnome-vfs-2.0)
Conflicts:	drakxtools < 9.1-15mdk

%description
This module provides perl access to GNOME-2.x VFS libraries.

The GNOME Virtual File System provides an abstraction to common file
system operations like reading, writing and copying files, listing
directories and so on.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%install
%makeinstall_std

%files
%doc LICENSE examples/*
%{_mandir}/*/*
%{perl_vendorarch}/%fmodule
%{perl_vendorarch}/%fmodule.pm
%{perl_vendorarch}/auto/%fmodule
