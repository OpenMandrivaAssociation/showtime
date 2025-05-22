%undefine _debugsource_packages
Name:           showtime
Version:        48.1
Release:        1
Summary:        Modern video player built using GTK4
Group:		      Video
License:        GPL-3.0-or-later
URL:            https://apps.gnome.org/Showtime/

Source0:        https://download.gnome.org/sources/%{name}/48/%{name}-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  desktop-file-utils
BuildRequires:  appstream
BuildRequires:  appstream-util
BuildRequires:  python-gi
BuildRequires:  python-gobject3

Requires:       python-gi
Requires:       gtk4
Requires:       libadwaita-common
Requires:       python3
Requires:       hicolor-icon-theme
Requires:       gstreamer1.0-plugins-base
Requires:       gstreamer-plugins-rs

Requires:      gstreamer1.0-plugins-good
Requires:      gstreamer1.0-plugins-bad
Requires:      gstreamer1.0-plugins-ugly

%description
Play your favorite movies and video files without hassle. Showtime
features simple playback controls that fade out of your way when
you're watching, fullscreen, adjustable playback speed, multiple
language and subtitle tracks, and screenshots — everything you
need for a straightforward viewing experience.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}


%files  -f %{name}.lang
%doc README.md
%license COPYING
%{python_sitelib}/showtime/
%{_bindir}/showtime
%{_datadir}/applications/org.gnome.Showtime.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Showtime.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Showtime.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Showtime-symbolic.svg
%{_metainfodir}/org.gnome.Showtime.metainfo.xml
%{_datadir}/showtime/
