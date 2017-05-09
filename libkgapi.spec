Summary:	Library to access various Google services via their public API
Name:		libkgapi
Version:	17.04.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.dvratil.cz/category/akonadi-google/
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5WebKitWidgets)
BuildRequires:	cmake(Qt5WebEngineWidgets)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Test)

%description
LibKGAPI (previously called LibKGoogle) is a C++ library that implements APIs
for various Google services.

Currently supported APIs:
  - Calendar API v3 (https://developers.google.com/google-apps/calendar)
  - Contacts API v3 (https://developers.google.com/google-apps/contacts/v3/)
  - Tasks API v1 (https://developers.google.com/google-apps/tasks)
  - Latitude API v1 (https://developers.google.com/latitude/v1/)
  - Static Google Maps API v2
    (https://developers.google.com/maps/documentation/staticmaps/)
  - Drive API v2 (https://developers.google.com/drive/v2/reference)

%files
%{_sysconfdir}/xdg/libkgapi.categories
%lang(mr) %{_localedir}/mr/LC_MESSAGES/libkgapi_qt.qm
%lang(nds) %{_localedir}/nds/LC_MESSAGES/libkgapi_qt.qm
%lang(gl) %{_localedir}/gl/LC_MESSAGES/libkgapi_qt.qm
%lang(hu) %{_localedir}/hu/LC_MESSAGES/libkgapi_qt.qm
%lang(ca) %{_localedir}/ca/LC_MESSAGES/libkgapi_qt.qm
%lang(sk) %{_localedir}/sk/LC_MESSAGES/libkgapi_qt.qm
%lang(bs) %{_localedir}/bs/LC_MESSAGES/libkgapi_qt.qm
%lang(ro) %{_localedir}/ro/LC_MESSAGES/libkgapi_qt.qm
%lang(fr) %{_localedir}/fr/LC_MESSAGES/libkgapi_qt.qm
%lang(pl) %{_localedir}/pl/LC_MESSAGES/libkgapi_qt.qm
%lang(tr) %{_localedir}/tr/LC_MESSAGES/libkgapi_qt.qm
%lang(pt_BR) %{_localedir}/pt_BR/LC_MESSAGES/libkgapi_qt.qm
%lang(nb) %{_localedir}/nb/LC_MESSAGES/libkgapi_qt.qm
%lang(sh_TW) %{_localedir}/zh_TW/LC_MESSAGES/libkgapi_qt.qm
%lang(da) %{_localedir}/da/LC_MESSAGES/libkgapi_qt.qm
%lang(fi) %{_localedir}/fi/LC_MESSAGES/libkgapi_qt.qm
%lang(ko) %{_localedir}/ko/LC_MESSAGES/libkgapi_qt.qm
%lang(cs) %{_localedir}/cs/LC_MESSAGES/libkgapi_qt.qm
%lang(de) %{_localedir}/de/LC_MESSAGES/libkgapi_qt.qm
%lang(it) %{_localedir}/it/LC_MESSAGES/libkgapi_qt.qm
%lang(zh_CN) %{_localedir}/zh_CN/LC_MESSAGES/libkgapi_qt.qm
%lang(sl) %{_localedir}/sl/LC_MESSAGES/libkgapi_qt.qm
%lang(pt) %{_localedir}/pt/LC_MESSAGES/libkgapi_qt.qm
%lang(km) %{_localedir}/km/LC_MESSAGES/libkgapi_qt.qm
%lang(et) %{_localedir}/et/LC_MESSAGES/libkgapi_qt.qm
%lang(en) %{_localedir}/en_GB/LC_MESSAGES/libkgapi_qt.qm
%lang(el) %{_localedir}/el/LC_MESSAGES/libkgapi_qt.qm
%lang(es) %{_localedir}/es/LC_MESSAGES/libkgapi_qt.qm
%lang(nl) %{_localedir}/nl/LC_MESSAGES/libkgapi_qt.qm
%lang(ca) %{_localedir}/ca@valencia/LC_MESSAGES/libkgapi_qt.qm
%lang(ast) %{_localedir}/ast/LC_MESSAGES/libkgapi_qt.qm
%lang(ja) %{_localedir}/ja/LC_MESSAGES/libkgapi_qt.qm
%lang(sv) %{_localedir}/sv/LC_MESSAGES/libkgapi_qt.qm
%lang(kk) %{_localedir}/kk/LC_MESSAGES/libkgapi_qt.qm
%lang(lt) %{_localedir}/lt/LC_MESSAGES/libkgapi_qt.qm
%lang(ga) %{_localedir}/ga/LC_MESSAGES/libkgapi_qt.qm
%lang(ug) %{_localedir}/ug/LC_MESSAGES/libkgapi_qt.qm
%lang(uk) %{_localedir}/uk/LC_MESSAGES/libkgapi_qt.qm
%lang(ru) %{_localedir}/ru/LC_MESSAGES/libkgapi_qt.qm
%lang(ar) %{_localedir}/ar/LC_MESSAGES/libkgapi_qt.qm
%lang(nn) %{_localedir}/nn/LC_MESSAGES/libkgapi_qt.qm
%lang(sr) %{_localedir}/sr/LC_MESSAGES/libkgapi_qt.qm


%dependinglibpackage KPimGAPIBlogger 5
%dependinglibpackage KPimGAPICalendar 5
%dependinglibpackage KPimGAPIContacts 5
%dependinglibpackage KPimGAPICore 5
%dependinglibpackage KPimGAPIDrive 5
%dependinglibpackage KPimGAPILatitude 5
%dependinglibpackage KPimGAPIMaps 5
%dependinglibpackage KPimGAPITasks 5

%define devname %mklibname KF5GAPI -d

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Provides:	%{name}-devel = %{EVRD}
Requires:	%{mklibname KPimGAPIBlogger 5} = %{EVRD}
Requires:	%{mklibname KPimGAPICalendar 5} = %{EVRD}
Requires:	%{mklibname KPimGAPIContacts 5} = %{EVRD}
Requires:	%{mklibname KPimGAPICore 5} = %{EVRD}
Requires:	%{mklibname KPimGAPIDrive 5} = %{EVRD}
Requires:	%{mklibname KPimGAPILatitude 5} = %{EVRD}
Requires:	%{mklibname KPimGAPIMaps 5} = %{EVRD}
Requires:	%{mklibname KPimGAPITasks 5} = %{EVRD}
Obsoletes:	%{mklibname kgapi -d} <= 5.3.1-2

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%dir %{_includedir}/KPim/KGAPI
%{_includedir}/KPim/KGAPI/KGAPI
%{_includedir}/KPim/KGAPI/kgapi
%{_includedir}/KPim/kgapi_version.h
%{_libdir}/libKPimGAPIBlogger.so
%{_libdir}/libKPimGAPICalendar.so
%{_libdir}/libKPimGAPIContacts.so
%{_libdir}/libKPimGAPICore.so
%{_libdir}/libKPimGAPIDrive.so
%{_libdir}/libKPimGAPILatitude.so
%{_libdir}/libKPimGAPIMaps.so
%{_libdir}/libKPimGAPITasks.so
%{_libdir}/cmake/KPimGAPI
%{_libdir}/cmake/KF5GAPI
%{_libdir}/qt5/mkspecs/modules/*.pri

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
