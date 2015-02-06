%define name	plasma-applet-launchbutton
%define version	0.0.4
%define release	3

Name: %{name}
Version: %{version}
Release: %{release}
Summary: A plasma applet that's a configurable launching button
Group: Graphical desktop/KDE
License: GPLv3+
Source: %{name}-%{version}.tar.bz2
# upstream is maarten.vanraes@gmail.com , URL might be added in later versions

BuildRoot: %{_tmppath}/%{name}-%{version}
BuildRequires: kdelibs4-devel
BuildRequires: qt4-qtdbus
Requires: kdebase4-workspace
Requires: kdeplasma4
Provides: plasma-applet

%description
Plasma launchbutton applet is a configurable image button to execute a
command or a DBUS function. In addition, you can let it open a configurable
File Dialog to have it's filenames append as arguments.


%files
%defattr(-,root,root)
%{_kde_libdir}/kde4/plasma_applet_launchbutton.so
%{_kde_services}/%{name}.desktop

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -fr %{buildroot}
%makeinstall_std -C build

%clean
rm -fr %{buildroot}


%changelog
* Mon Feb 07 2011 Funda Wang <fwang@mandriva.org> 0.0.4-2mdv2011.0
+ Revision: 636575
- tighten BR

* Fri Sep 03 2010 Maarten Vanraes <alien@mandriva.org> 0.0.4-1mdv2011.0
+ Revision: 575681
- import plasma-applet-launchbutton

