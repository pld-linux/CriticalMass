Summary:	Critical Mass - space shoot'em up game
Summary(pl):	Critical Mass - kosmiczna strzelanina
Name:		CriticalMass
Version:	0.98
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/criticalmass/%{name}-%{version}.tar.bz2
# Source0-md5:	af1fdb1e4156723423255a394ee8312f
URL:		http://criticalmass.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.0
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel >= 1.0.12
BuildRequires:	zlib >= 1.1.3
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
 
%description -l pl
Critical Mass (Critter) to oparta na SDL/OpenGL kosmiczna strzelanina.
¦wiat zosta³ zaatakowany przez agresywn± armiê kosmicznych stworzeñ.
Napadniêty i nieprzygotowany rz±d nie by³ w stanie obroniæ swoich
zasobów. Jako ostatnia szansa na odzyskanie czê¶ci dóbr, gracz zosta³
umieszczony w ma³ym statku kosmicznym i wys³any za kosmitami.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO Readme.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/Critical_Mass
%{_mandir}/man6/*
