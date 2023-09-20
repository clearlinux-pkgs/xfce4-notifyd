#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : xfce4-notifyd
Version  : 0.9.1
Release  : 30
URL      : https://archive.xfce.org/src/apps/xfce4-notifyd/0.9/xfce4-notifyd-0.9.1.tar.bz2
Source0  : https://archive.xfce.org/src/apps/xfce4-notifyd/0.9/xfce4-notifyd-0.9.1.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfce4-notifyd-bin = %{version}-%{release}
Requires: xfce4-notifyd-data = %{version}-%{release}
Requires: xfce4-notifyd-lib = %{version}-%{release}
Requires: xfce4-notifyd-license = %{version}-%{release}
Requires: xfce4-notifyd-locales = %{version}-%{release}
Requires: xfce4-notifyd-man = %{version}-%{release}
Requires: xfce4-notifyd-services = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libxfce4panel-2.0)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfce4util-1.0)
BuildRequires : pkgconfig(libxfconf-0)
BuildRequires : pkgconfig(sqlite3)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Xfce Notify Daemon
The Xfce Notify Daemon (or `xfce4-notifyd`) is a small program that implements
the "server-side" portion of the Freedesktop desktop notifications
specification. Applications that wish to pop up a notification bubble in a
standard way can implicitly make use of xfce4-notifyd to do so by sending
standard messages over D-Bus using the `org.freedesktop.Notifications`
interface.

%package bin
Summary: bin components for the xfce4-notifyd package.
Group: Binaries
Requires: xfce4-notifyd-data = %{version}-%{release}
Requires: xfce4-notifyd-license = %{version}-%{release}
Requires: xfce4-notifyd-services = %{version}-%{release}

%description bin
bin components for the xfce4-notifyd package.


%package data
Summary: data components for the xfce4-notifyd package.
Group: Data

%description data
data components for the xfce4-notifyd package.


%package lib
Summary: lib components for the xfce4-notifyd package.
Group: Libraries
Requires: xfce4-notifyd-data = %{version}-%{release}
Requires: xfce4-notifyd-license = %{version}-%{release}

%description lib
lib components for the xfce4-notifyd package.


%package license
Summary: license components for the xfce4-notifyd package.
Group: Default

%description license
license components for the xfce4-notifyd package.


%package locales
Summary: locales components for the xfce4-notifyd package.
Group: Default

%description locales
locales components for the xfce4-notifyd package.


%package man
Summary: man components for the xfce4-notifyd package.
Group: Default

%description man
man components for the xfce4-notifyd package.


%package services
Summary: services components for the xfce4-notifyd package.
Group: Systemd services
Requires: systemd

%description services
services components for the xfce4-notifyd package.


%prep
%setup -q -n xfce4-notifyd-0.9.1
cd %{_builddir}/xfce4-notifyd-0.9.1
pushd ..
cp -a xfce4-notifyd-0.9.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695226999
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static --enable-dbus-start-daemon
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --enable-dbus-start-daemon
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1695226999
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xfce4-notifyd
cp %{_builddir}/xfce4-notifyd-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xfce4-notifyd/4cc77b90af91e615a64ae04893fdffa7939db84c || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
%find_lang xfce4-notifyd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/xfce4/notifyd/xfce4-notifyd
/usr/lib64/xfce4/notifyd/xfce4-notifyd

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/xfce4-notifyd-config
/usr/bin/xfce4-notifyd-config

%files data
%defattr(-,root,root,-)
/usr/share/applications/xfce4-notifyd-config.desktop
/usr/share/dbus-1/services/org.xfce.xfce4-notifyd.Notifications.service
/usr/share/dbus-1/services/org.xfce.xfce4-notifyd.Notifyd.service
/usr/share/icons/hicolor/16x16/apps/org.xfce.notification.png
/usr/share/icons/hicolor/48x48/apps/org.xfce.notification.png
/usr/share/icons/hicolor/scalable/apps/org.xfce.notification.svg
/usr/share/icons/hicolor/scalable/status/notification-disabled-symbolic.svg
/usr/share/icons/hicolor/scalable/status/notification-symbolic.svg
/usr/share/icons/hicolor/scalable/status/org.xfce.notification.unread-emblem-symbolic.svg
/usr/share/themes/Bright/xfce-notify-4.0/gtk.css
/usr/share/themes/Default/xfce-notify-4.0/gtk.css
/usr/share/themes/Retro/xfce-notify-4.0/gtk.css
/usr/share/themes/Smoke/xfce-notify-4.0/gtk.css
/usr/share/themes/ZOMG-PONIES!/xfce-notify-4.0/gtk.css
/usr/share/xfce4/panel/plugins/notification-plugin.desktop

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/xfce4/panel/plugins/libnotification-plugin.so
/usr/lib64/xfce4/panel/plugins/libnotification-plugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xfce4-notifyd/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xfce4-notifyd-config.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/xfce4-notifyd.service

%files locales -f xfce4-notifyd.lang
%defattr(-,root,root,-)

