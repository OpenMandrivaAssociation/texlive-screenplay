Name:		texlive-screenplay
Version:	27223
Release:	2
Summary:	A class file to typeset screenplays
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/screenplay
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/screenplay.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/screenplay.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/screenplay.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class implements the format recommended by the Academy of
Motion Picture Arts and Sciences.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/screenplay/hardmarg.sty
%{_texmfdistdir}/tex/latex/screenplay/screenplay.cls
%doc %{_texmfdistdir}/doc/latex/screenplay/COPYING
%doc %{_texmfdistdir}/doc/latex/screenplay/README
%doc %{_texmfdistdir}/doc/latex/screenplay/example.tex
%doc %{_texmfdistdir}/doc/latex/screenplay/screenplay.pdf
%doc %{_texmfdistdir}/doc/latex/screenplay/test.pdf
%doc %{_texmfdistdir}/doc/latex/screenplay/test.tex
#- source
%doc %{_texmfdistdir}/source/latex/screenplay/screenplay.dtx
%doc %{_texmfdistdir}/source/latex/screenplay/screenplay.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
