#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfce4-notifyd
Version  : 0.2.4
Release  : 2
URL      : http://archive.xfce.org/src/apps/xfce4-notifyd/0.2/xfce4-notifyd-0.2.4.tar.bz2
Source0  : http://archive.xfce.org/src/apps/xfce4-notifyd/0.2/xfce4-notifyd-0.2.4.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfce4-notifyd-bin
Requires: xfce4-notifyd-data
Requires: xfce4-notifyd-locales
Requires: xfce4-notifyd-doc
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libxfce4ui-1)
BuildRequires : pkgconfig(libxfce4util-1.0)
BuildRequires : pkgconfig(libxfconf-0)
BuildRequires : pkgconfig(x11)
Patch1: 0001-xfce4-notify-Set-the-default-theme-to-Arc.patch

%description
Xfce Notify Daemon
The Xfce Notify Daemon (xfce4-notifyd for short) is a smallish program that
implements the "server-side" portion of the Freedesktop desktop notifications
specification.  Applications that wish to pop up a notification bubble in
a standard way can implicitly make use of xfce4-notifyd to do so by
sending standard messages over D-Bus using the org.freedesktop.Notifications
interface.

%package bin
Summary: bin components for the xfce4-notifyd package.
Group: Binaries
Requires: xfce4-notifyd-data

%description bin
bin components for the xfce4-notifyd package.


%package data
Summary: data components for the xfce4-notifyd package.
Group: Data

%description data
data components for the xfce4-notifyd package.


%package doc
Summary: doc components for the xfce4-notifyd package.
Group: Documentation

%description doc
doc components for the xfce4-notifyd package.


%package locales
Summary: locales components for the xfce4-notifyd package.
Group: Default

%description locales
locales components for the xfce4-notifyd package.


%prep
%setup -q -n xfce4-notifyd-0.2.4
%patch1 -p1

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang xfce4-notifyd

%files
%defattr(-,root,root,-)
/usr/lib64/xfce4/notifyd/xfce4-notifyd

%files bin
%defattr(-,root,root,-)
/usr/bin/xfce4-notifyd-config

%files data
%defattr(-,root,root,-)
/usr/share/applications/xfce4-notifyd-config.desktop
/usr/share/dbus-1/services/org.xfce.xfce4-notifyd.Notifications.service
/usr/share/icons/hicolor/48x48/apps/xfce4-notifyd.png
/usr/share/themes/Default/xfce-notify-4.0/gtkrc
/usr/share/themes/Smoke/xfce-notify-4.0/gtkrc
/usr/share/themes/ZOMG-PONIES!/xfce-notify-4.0/gtkrc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files locales -f xfce4-notifyd.lang 
%defattr(-,root,root,-)

