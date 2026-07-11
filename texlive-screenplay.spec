%global tl_name screenplay
%global tl_revision 27223

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	A class file to typeset screenplays
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/screenplay
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/screenplay.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/screenplay.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/screenplay.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class implements the format recommended by the Academy of Motion
Picture Arts and Sciences.

