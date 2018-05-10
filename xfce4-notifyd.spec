#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfce4-notifyd
Version  : 0.4.1
Release  : 11
URL      : http://archive.xfce.org/src/apps/xfce4-notifyd/0.4/xfce4-notifyd-0.4.1.tar.bz2
Source0  : http://archive.xfce.org/src/apps/xfce4-notifyd/0.4/xfce4-notifyd-0.4.1.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfce4-notifyd-bin
Requires: xfce4-notifyd-config
Requires: xfce4-notifyd-lib
Requires: xfce4-notifyd-data
Requires: xfce4-notifyd-locales
Requires: xfce4-notifyd-doc
BuildRequires : intltool
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libxfce4panel-2.0)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfce4util-1.0)
BuildRequires : pkgconfig(libxfconf-0)
BuildRequires : pkgconfig(x11)
Patch1: 0001-xfce4-notify-Set-the-default-theme-to-Arc.patch

%description
Xfce Notify Daemon
==================
The Xfce Notify Daemon (or "xfce4-notifyd") is a small program that implements
the "server-side" portion of the Freedesktop desktop notifications
specification. Applications that wish to pop up a notification bubble in a
standard way can implicitly make use of xfce4-notifyd to do so by sending
standard messages over D-Bus using the org.freedesktop.Notifications
interface.

%package bin
Summary: bin components for the xfce4-notifyd package.
Group: Binaries
Requires: xfce4-notifyd-data
Requires: xfce4-notifyd-config

%description bin
bin components for the xfce4-notifyd package.


%package config
Summary: config components for the xfce4-notifyd package.
Group: Default

%description config
config components for the xfce4-notifyd package.


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


%package lib
Summary: lib components for the xfce4-notifyd package.
Group: Libraries
Requires: xfce4-notifyd-data

%description lib
lib components for the xfce4-notifyd package.


%package locales
Summary: locales components for the xfce4-notifyd package.
Group: Default

%description locales
locales components for the xfce4-notifyd package.


%prep
%setup -q -n xfce4-notifyd-0.4.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513104461
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1513104461
rm -rf %{buildroot}
%make_install
%find_lang xfce4-notifyd

%files
%defattr(-,root,root,-)
/usr/lib64/xfce4/notifyd/xfce4-notifyd

%files bin
%defattr(-,root,root,-)
/usr/bin/xfce4-notifyd-config

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/user/xfce4-notifyd.service

%files data
%defattr(-,root,root,-)
/usr/share/applications/xfce4-notifyd-config.desktop
/usr/share/dbus-1/services/org.xfce.xfce4-notifyd.Notifications.service
/usr/share/icons/hicolor/16x16/apps/xfce4-notifyd.png
/usr/share/icons/hicolor/24x24/apps/xfce4-notifyd.png
/usr/share/icons/hicolor/32x32/apps/xfce4-notifyd.png
/usr/share/icons/hicolor/48x48/apps/xfce4-notifyd.png
/usr/share/icons/hicolor/scalable/apps/xfce4-notifyd.svg
/usr/share/icons/hicolor/scalable/status/notification-disabled-new-symbolic.svg
/usr/share/icons/hicolor/scalable/status/notification-disabled-symbolic.svg
/usr/share/icons/hicolor/scalable/status/notification-new-symbolic.svg
/usr/share/icons/hicolor/scalable/status/notification-symbolic.svg
/usr/share/themes/Bright/xfce-notify-4.0/gtk.css
/usr/share/themes/Default/xfce-notify-4.0/gtk.css
/usr/share/themes/Retro/xfce-notify-4.0/gtk.css
/usr/share/themes/Smoke/xfce-notify-4.0/gtk.css
/usr/share/themes/ZOMG-PONIES!/xfce-notify-4.0/gtk.css
/usr/share/xfce4/panel/plugins/notification-plugin.desktop

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/xfce4/panel/plugins/libnotification-plugin.so

%files locales -f xfce4-notifyd.lang
%defattr(-,root,root,-)

