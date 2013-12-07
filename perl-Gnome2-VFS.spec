%define	module	Gnome2-VFS
%define	fmodule	Gnome2/VFS

Summary:	Perl module for the gnome2-2.x VFS libraries
Name:		perl-%{module}
Version:	1.081
Release:	11
License:	LGPLv2.1+
Group:		Development/GNOME and GTK+
# http://sourceforge.net/project/showfiles.php?group_id=64773&package_id=102457
Url:		http://gtk2-perl.sf.net/
Source0:	%{module}-%{version}.tar.bz2
BuildRequires:	perl-Glib => 1.00
BuildRequires:	perl-Gtk2
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig 
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(gnome-vfs-2.0)
Requires:	perl-Glib >= 1.00
Requires:	pkgconfig(gnome-vfs-2.0)

%description
This module provides perl access to GNOME-2.x VFS libraries.

The GNOME Virtual File System provides an abstraction to common file
system operations like reading, writing and copying files, listing
directories and so on.

%prep
%setup -qn %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%install
%makeinstall_std

%files
%doc LICENSE examples/*
%{perl_vendorarch}/%{fmodule}
%{perl_vendorarch}/%{fmodule}.pm
%{perl_vendorarch}/auto/%{fmodule}
%{_mandir}/man3/*

