Summary:	Critical Mass - space shoot'em up game
Summary(pl.UTF-8):	Critical Mass - kosmiczna strzelanina
Name:		CriticalMass
Version:	1.0.2
Release:	1
Epoch:		1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/criticalmass/%{name}-%{version}.tar.bz2
# Source0-md5:	e2aff114bffa717fb79c82e1dc473ebe
Source1:	%{name}.desktop
URL:		http://criticalmass.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel >= 1.2.5
BuildRequires:	SDL_mixer-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel >= 1.0.12
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel >= 1.1.3
Requires:	OpenGL
Requires:	SDL >= 1.2.3
Requires:	SDL_image >= 1.2.0
Requires:	SDL_mixer >= 1.2.0
Requires:	libpng >= 1.0.12
Requires:	zlib >= 1.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Critical Mass (Critter) is an SDL/OpenGL space shoot'em up game.
Your world has been infested by an aggressive army of space critters.
Overrun and unprepared, your government was unable to defend its
precious resources. As a last effort to recapture some of the
'goodies', you have been placed into a tiny spacecraft and sent after
them.

%description -l pl.UTF-8
Critical Mass (Critter) to oparta na SDL/OpenGL kosmiczna strzelanina.
Świat został zaatakowany przez agresywną armię kosmicznych stworzeń.
Napadnięty i nieprzygotowany rząd nie był w stanie obronić swoich
zasobów. Jako ostatnia szansa na odzyskanie części dóbr, gracz został
umieszczony w małym statku kosmicznym i wysłany za kosmitami.

%prep
%setup -q

%build
sed -i 's/curl//' Makefile.am
sed -i 's/\.\.\/curl\/lib\/libcurl\.a/\/usr\/lib\/libcurl.so/' game/Makefile.am
sed -i 's/AC_CONFIG_SUBDIRS(curl)//' configure.in
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install critter.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

# this one gets installed by author's mistake
rm -f $RPM_BUILD_ROOT%{_bindir}/Packer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO Readme.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/Critical_Mass
%{_mandir}/man6/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
