%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	Library to access various Google services via their public API
Name:		libkgapi
Version:	23.04.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.dvratil.cz/category/akonadi-google/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5WebKitWidgets)
BuildRequires:	cmake(Qt5WebEngineWidgets)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	pkgconfig(libsasl2)
BuildRequires:	qt5-qtwayland
Obsoletes:	%{mklibname KPimGAPIBlogger} < %{EVRD}
Obsoletes:	%{mklibname KPimGAPICalendar} < %{EVRD}
Obsoletes:	%{mklibname KPimGAPIContacts} < %{EVRD}
Obsoletes:	%{mklibname KPimGAPICore} < %{EVRD}
Obsoletes:	%{mklibname KPimGAPIDrive} < %{EVRD}
Obsoletes:	%{mklibname KPimGAPILatitude} < %{EVRD}
Obsoletes:	%{mklibname KPimGAPIMaps} < %{EVRD}
Obsoletes:	%{mklibname KPimGAPITasks} < %{EVRD}

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

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/libkgapi.categories
%{_libdir}/sasl2/libkdexoauth2.so*

%dependinglibpackage KPim5GAPIBlogger 5
%dependinglibpackage KPim5GAPICalendar 5
%dependinglibpackage KPim5GAPICore 5
%dependinglibpackage KPim5GAPIDrive 5
%dependinglibpackage KPim5GAPILatitude 5
%dependinglibpackage KPim5GAPIMaps 5
%dependinglibpackage KPim5GAPIPeople 5
%dependinglibpackage KPim5GAPITasks 5

%define devname %mklibname KF5GAPI -d

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Provides:	%{name}-devel = %{EVRD}
Requires:	%{mklibname KPim5GAPIBlogger} = %{EVRD}
Requires:	%{mklibname KPim5GAPICalendar} = %{EVRD}
Requires:	%{mklibname KPim5GAPICore} = %{EVRD}
Requires:	%{mklibname KPim5GAPIDrive} = %{EVRD}
Requires:	%{mklibname KPim5GAPILatitude} = %{EVRD}
Requires:	%{mklibname KPim5GAPIMaps} = %{EVRD}
Requires:	%{mklibname KPim5GAPIPeople} = %{EVRD}
Requires:	%{mklibname KPim5GAPITasks} = %{EVRD}
Obsoletes:	%{mklibname kgapi -d} <= 5.3.1-2

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%dir %{_includedir}/KPim5/KGAPI
%{_includedir}/KPim5/KGAPI/KGAPI
%{_includedir}/KPim5/KGAPI/kgapi
%{_includedir}/KPim5/kgapi_version.h
%{_libdir}/libKPim5GAPIBlogger.so
%{_libdir}/libKPim5GAPICalendar.so
%{_libdir}/libKPim5GAPICore.so
%{_libdir}/libKPim5GAPIDrive.so
%{_libdir}/libKPim5GAPILatitude.so
%{_libdir}/libKPim5GAPIMaps.so
%{_libdir}/libKPim5GAPIPeople.so
%{_libdir}/libKPim5GAPITasks.so
%{_libdir}/cmake/KPim5GAPI
%{_libdir}/cmake/KPimGAPI
%{_libdir}/qt5/mkspecs/modules/*.pri

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html --with-qt
