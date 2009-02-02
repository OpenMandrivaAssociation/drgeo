%define version 1.1.0
%define release %mkrel 12

Summary:	Interactive geometry software
Name:		drgeo
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sciences/Mathematics
URL:		http://www.ofset.org/drgeo/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Source:		http://prdownloads.sourceforge.net/ofset/%{name}-%{version}.tar.bz2
Source1:	gnome-drgenius.png
Patch0:		drgeo-fix-menu-entry.patch
Patch1:		drgeo-1.1.0-fix-str-fmt.patch
Patch2:		03-fix_segfault.dpatch
BuildRequires:	imagemagick
BuildRequires:	guile-devel
BuildRequires:	libxml2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:  perl(XML::Parser)
BuildRequires:	desktop-file-utils

%description
Dr. Genius is the GNOME interactive geometry software. It allows one to
create geometric figure plus the interactive manipulation of such figure
in respect with their geometric constraints. It is usable in teaching
situation with students from primary or secondary level.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-MoreApplications-Sciences-Mathematics" \
  --add-category="Science" \
  --add-category="Math" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

# icons
mkdir -p %{buildroot}%{_iconsdir} \
	 %{buildroot}%{_miconsdir}
install -m 0644 -D      %{SOURCE1} %{buildroot}%{_liconsdir}/gnome-drgenius.png
convert -geometry 32x32 %{SOURCE1} %{buildroot}%{_iconsdir}/gnome-drgenius.png
convert -geometry 16x16 %{SOURCE1} %{buildroot}%{_miconsdir}/gnome-drgenius.png

# TeXmacs was supposed to locate in another directory for MDK
pushd %{buildroot}%{_datadir}
mv texmacs/TeXmacs ./
rmdir texmacs
popd

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_datadir}/TeXmacs/plugins/drgeo
%{_iconsdir}/gnome-drgenius.png
%{_miconsdir}/gnome-drgenius.png
%{_liconsdir}/gnome-drgenius.png


