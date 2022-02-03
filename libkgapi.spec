%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	Library to access various Google services via their public API
Name:		libkgapi
Version:	21.12.2
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
