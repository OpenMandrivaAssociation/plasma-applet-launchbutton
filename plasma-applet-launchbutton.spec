%define name	plasma-applet-launchbutton
%define version	0.0.4
%define release	%mkrel 1

Name: %{name}
Version: %{version}
Release: %{release}
Summary: A plasma applet that's a configurable launching button
Group: Graphical desktop/KDE
License: GPLv3+
Source: %{name}-%{version}.tar.bz2
# upstream is maarten.vanraes@gmail.com , URL might be added in later versions

BuildRoot: %{_tmppath}/%{name}-%{version}
BuildRequires: qt4-devel
BuildRequires: kde4-macros
BuildRequires: X11-devel
BuildRequires: kdebase4-devel >= 1:4.2.98
BuildRequires: kdebase4-workspace-devel >= 2:4.2.98
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
