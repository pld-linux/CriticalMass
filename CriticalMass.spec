Summary: 	Critical Mass.
Name:		CriticalMass
Version:	0.97
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://cesnet.dl.sourceforge.net/sourceforge/criticalmass/%{name}-%{version}.tar.bz2
URL:		http://criticalmass.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.3
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.0
BuildRequires:	OpenGL-devel
BuildRequires:	libpng-devel >= 1.0.12
BuildRequires:	zlib >= 1.1.3
BuildRequires:	libogg-devel
Requires:	SDL >= 1.2.3
Requires:	SDL_image >= 1.2.0
Requires:	SDL_mixer >= 1.2.0
Requires:	zlib >= 1.1.3
Requires:	libpng >= 1.0.12
Requires:	OpenGL
Requires:	libogg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Critical Mass (Critter) is an SDL/OpenGL space shoot'em up game.
Your world has been infested by an aggressive army of space critters.
Overrun and unprepared, your government was unable to defend its
precious resources. As a last effort to recapture some of the 'goodies',
you have been placed into a tiny spacecraft and sent after them.
 
 
%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog TODO Readme.html
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/Critical_Mass
%{_datadir}/Critical_Mass/*
%lang(en) %{_mandir}/man6/*
