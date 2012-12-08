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


%changelog
* Tue Jan 31 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.081-9
+ Revision: 770095
- remove junk
- cosmetics
- fix license
- fix buildrequires
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for perl-5.14.2
    - rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.081-6
+ Revision: 667183
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.081-5mdv2011.0
+ Revision: 564479
- rebuild for perl 5.12.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.081-4mdv2011.0
+ Revision: 426457
- rebuild

* Wed Sep 24 2008 Oden Eriksson <oeriksson@mandriva.com> 1.081-3mdv2009.0
+ Revision: 287781
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Feb 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.081-1mdv2008.1
+ Revision: 174586
- update to new version 1.081

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.080-2mdv2008.1
+ Revision: 152094
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Oct 08 2007 Thierry Vignaud <tv@mandriva.org> 1.080-1mdv2008.0
+ Revision: 95743
- new release

* Tue Jul 31 2007 Thierry Vignaud <tv@mandriva.org> 1.070-2mdv2008.0
+ Revision: 57079
- new release

* Tue Jun 26 2007 Thierry Vignaud <tv@mandriva.org> 1.061-2mdv2008.0
+ Revision: 44611
- rebuild


* Wed Nov 29 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.061-1mdv2007.0
+ Revision: 88804
- Import perl-Gnome2-VFS

* Wed Nov 29 2006 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.061-1mdv2007.1
- new release

* Thu Mar 16 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.060-1mdk
- new release

* Tue Jan 31 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.051-1mdk
- new release

* Tue Jan 03 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.050-1mdk
- new release

* Tue Oct 04 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.041-1mdk
- new release

* Fri Jun 24 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.022-1mdk
- new release

* Sat Apr 16 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.021-1mdk
- new release

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 1.011-2mdk
- Rebuild for new perl

* Tue Aug 17 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.011-1mdk
- new release

* Tue Aug 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.010-1mdk
- new release

* Wed Jun 30 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.003-1mdk
- new release

* Tue Jun 15 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.002-1mdk
- new release

* Sat Jun 05 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.001-2mdk
- rebuild for new gnome-vfs2

* Wed Mar 31 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.001-1mdk
- new release

* Fri Jan 30 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.90-1mdk
- new release

* Sat Jan 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.05-2mdk
- add example

* Sat Jan 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.05-1mdk
- initial release

