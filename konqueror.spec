#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE file and web browser
Name:		konqueror
Version:	26.04.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/network/konqueror/-/archive/%{gitbranch}/konqueror-%{gitbranchd}.tar.bz2#/konqueror-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/konqueror-%{version}.tar.xz
%endif
BuildSystem:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(PlasmaActivities)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Su)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6Sonnet)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6TextToSpeech)
BuildRequires:	pkgconfig(Qt6WebEngineCore)
BuildRequires:	pkgconfig(Qt6WebEngineWidgets)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	tidy-devel
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	hunspell
BuildRequires:	myspell-en
Suggests:	plasma6-keditbookmarks
Suggests:	%{name}-plugins
Requires:	%{name}-webenginepart
%rename plasma6-konqueror

%description
KDE file and web browser.

%files -f %{name}.lang
%config %{_sysconfdir}/xdg/konqautofiltersrc
%{_datadir}/qlogging-categories6/konqueror.categories
%{_datadir}/applications/kfmclient.desktop
%{_datadir}/applications/kfmclient_html.desktop
%{_datadir}/applications/kfmclient_war.desktop
%{_datadir}/applications/kfmclient_dir.desktop
%{_datadir}/applications/konqbrowser.desktop
%{_sysconfdir}/xdg/autostart/konqy_preload.desktop
%{_bindir}/kfmclient
%{_bindir}/konqueror
%{_datadir}/config.kcfg/konqueror*
%{_datadir}/kcmcss/template.css
%{_datadir}/kcontrol/*
%{_datadir}/konqueror/about/*
%{_datadir}/konqueror/pics/indicator_*.png
%{_datadir}/icons/*/*/*/konqueror.*
%{_datadir}/metainfo/org.kde.konqueror.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.?onqueror.*.xml
%{_libdir}/qt6/plugins/konqueror_kcms
%{_sysconfdir}/xdg/useragenttemplatesrc
%{_datadir}/applications/bookmarks.desktop
%{_qtdir}/plugins/kf6/kio/bookmarks.so

#------------------------------------------------

%package plugins
Summary:	Konqueror plugins
Group:		Graphical desktop/KDE
Requires:	konqueror >= 6.0
%rename plasma6-konqueror-plugins

%description plugins
This module contains plugins that interact with Konqueror.

%files plugins -f plugins.lang
%{_qtdir}/plugins/temporarysavedir.so
%{_qtdir}/plugins/webenginepart/kpartplugins/temporarysavedirwebenginepart_kpartplugins.so
%{_datadir}/konqueror/partsrcfiles/temporarysavedir.rc
%{_bindir}/fsview
%{_datadir}/akregator/pics/feed.png
%{_datadir}/konqueror/icons/hicolor/*/actions/google.*
%{_datadir}/konqueror/partsrcfiles/akregatorkonqfeedicon.rc
%{_datadir}/konqueror/partsrcfiles/autorefresh.rc
%{_datadir}/konqueror/partsrcfiles/babelfishplugin.rc
%{_datadir}/konqueror/partsrcfiles/dirfilterplugin.rc
%{_datadir}/konqueror/partsrcfiles/khtmlsettingsplugin.rc
%{_datadir}/konqueror/partsrcfiles/kimgallery.rc
%{_datadir}/konqueror/partsrcfiles/konq_shellcmdplugin.rc
%{_datadir}/konqueror/partsrcfiles/konqueror_kget_browser_integration.rc
%{_datadir}/konqueror/partsrcfiles/searchbarplugin.rc
%{_datadir}/konqueror/partsrcfiles/uachangerplugin.rc
%{_datadir}/konqueror/partsrcfiles/webarchiverplugin.rc
%{_iconsdir}/hicolor/*/actions/babelfish.*
%{_iconsdir}/hicolor/*/actions/imagegallery.*
%{_iconsdir}/hicolor/*/apps/fsview.*
%{_sysconfdir}/xdg/translaterc
%{_qtdir}/plugins/akregatorkonqfeedicon.so
%{_qtdir}/plugins/autorefresh.so
%{_qtdir}/plugins/babelfishplugin.so
%{_qtdir}/plugins/dolphinpart/kpartplugins/kimgallery.so
%{_qtdir}/plugins/dolphinpart/kpartplugins/konq_shellcmdplugin.so
%{_qtdir}/plugins/dolphinpart/kpartplugins/dirfilterplugin.so
%{_qtdir}/plugins/khtmlsettingsplugin.so
%{_qtdir}/plugins/konqueror/kpartplugins/searchbarplugin.so
%{_qtdir}/plugins/konqueror_kget_browser_integration.so
%{_qtdir}/plugins/webenginepart/kpartplugins/akregatorkonqfeediconwebenginepart_kpartplugins.so
%{_qtdir}/plugins/webenginepart/kpartplugins/autorefreshwebenginepart_kpartplugins.so
%{_qtdir}/plugins/webenginepart/kpartplugins/babelfishpluginwebenginepart_kpartplugins.so
%{_qtdir}/plugins/webenginepart/kpartplugins/khtmlsettingspluginwebenginepart_kpartplugins.so
%{_qtdir}/plugins/webenginepart/kpartplugins/konqueror_kget_browser_integrationwebenginepart_kpartplugins.so
%{_qtdir}/plugins/webenginepart/kpartplugins/uachangerpluginwebenginepart_kpartplugins.so
%{_qtdir}/plugins/webenginepart/kpartplugins/webarchiverpluginwebenginepart_kpartplugins.so
%{_qtdir}/plugins/kf6/parts/fsviewpart.so
%{_qtdir}/plugins/kf6/parts/konq_sidebar.so
%{_datadir}/qlogging-categories6/akregatorplugin.categories
%{_libdir}/qt6/plugins/kf6/kfileitemaction/akregatorplugin.so
%{_datadir}/webenginepart/error.html
%{_sysconfdir}/xdg/konqsidebartngrc
%{_qtdir}/plugins/uachangerplugin.so
%{_datadir}/konqsidebartng
%{_datadir}/qlogging-categories6/fsview.categories
%{_datadir}/applications/org.kde.konqueror.desktop
%{_datadir}/applications/kcm_speeddial.desktop
%{_datadir}/applications/speeddial.desktop
%{_datadir}/konqueror/webengine_dictionaries
# = webarchive plugin =
%{_bindir}/kcreatewebarchive
%{_libdir}/qt6/plugins/webarchiverplugin.so
%{_libdir}/qt6/plugins/kf6/thumbcreator/webarchivethumbnail.so
%{_datadir}/config.kcfg/kcreatewebarchive.kcfg
%{_datadir}/icons/hicolor/*/actions/webarchiver.*
%{_datadir}/kconf_update/webenginepart.upd
%{_libdir}/qt6/plugins/konqueror_kcms/kcm_bookmarks.so
%{_libdir}/qt6/plugins/konqueror_kcms/kcm_history.so
%{_libdir}/qt6/plugins/konqueror_kcms/kcm_konq.so
%{_libdir}/qt6/plugins/konqueror_kcms/kcm_performance.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_appearance.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_behavior.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_filter.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_general.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_java_js.so
%{_libdir}/qt6/plugins/konqueror/sidebar
%{_datadir}/applications/kcm_bookmarks.desktop
%{_datadir}/kio_bookmarks

#----------------------------------------------------------------------------

%package libkonq
Summary:	KDE Frameworks 6 Konq library support files
Group:		Graphical desktop/KDE
%rename		plasma6-konqueror-libkonq

%description libkonq
KDE Frameworks 6 Konq library support files.

%files libkonq -f libkonq.lang
%{_datadir}/kf6/kbookmark/directory_bookmarkbar.desktop

#----------------------------------------------------------------------------

%package webenginepart
Summary:	Plasma 6 embeddable HTML component
Group:		Graphical desktop/KDE
%rename plasma6-konqueror-webenginepart

%description webenginepart
Plasma 6 embeddable HTML component.

%files webenginepart -f webenginepart.lang
%{_iconsdir}/*/*/*/webengine.*
%{_libdir}/libkwebenginepart.so
%{_libdir}/qt6/plugins/kf6/parts/webenginepart.so

#----------------------------------------------------------------------------

%define kf6konq_major 7
%define libkf6konq %mklibname KF6Konq %{kf6konq_major}

%package -n %{libkf6konq}
Summary:	KDE Frameworks 6 Konq shared library
Group:		System/Libraries
Requires:	%{name}-libkonq

%description -n %{libkf6konq}
KDE Frameworks 6 Konq shared library.

%files -n %{libkf6konq}
%{_libdir}/libKF6Konq.so.%{kf6konq_major}*
%{_libdir}/libKF6Konq.so.5*
%{_libdir}/libKF6KonqSettings.so.*
%{_libdir}/libkonqsidebarplugin.so.*
%{_libdir}/libkonquerorprivate.so.*

#----------------------------------------------------------------------------

%define devkf6konq %mklibname KF6Konq -d

%package -n %{devkf6konq}
Summary:	Development files for KDE Frameworks 6 Konq library
Group:		Development/KDE and Qt
Requires:	%{libkf6konq} = %{EVRD}
Provides:	KF6Konq-devel = %{EVRD}

%description -n %{devkf6konq}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devkf6konq}
%{_includedir}/KF6/konq_events.h
%{_includedir}/KF6/konq_historyentry.h
%{_includedir}/KF6/konq_historyprovider.h
%{_includedir}/KF6/konq_kpart_plugin.h
%{_includedir}/KF6/konq_popupmenu.h
%{_includedir}/KF6/konq_version.h
%{_includedir}/KF6/libkonq_export.h
%{_includedir}/KF6/konqsettings.h
%{_includedir}/KF6/konqsettings_version.h
%{_includedir}/KF6/libkonqsettings_export.h
%{_includedir}/KF6/selectorinterface.h
%{_libdir}/cmake/KF6Konq
%{_libdir}/libKF6Konq.so
%{_libdir}/libKF6KonqSettings.so
%{_libdir}/libkonqsidebarplugin.so
%{_includedir}/KF6/konqsidebarplugin.h

%install -a
rm -f plugins.lang konqueror.lang
for i in akregator_konqplugin autorefresh babelfish dirfilterplugin fsview imgalleryplugin kcmbookmarks kcmkonqhtml kcmkonq kcmperformance kfmclient kgetplugin khtmlsettingsplugin khtmltts kshellcmdplugin searchbarplugin uachangerplugin webarchiver kio6_bookmarks konqsidebar temporarysavedir kcontrol speeddial; do
	%find_lang $i --with-html
	cat $i.lang >>plugins.lang
done

%find_lang konqueror --with-html
%find_lang libkonq --with-html
%find_lang webenginepart --with-html
