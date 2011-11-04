# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/screenplay
# catalog-date 2009-01-07 11:54:09 +0100
# catalog-license gpl
# catalog-version 1.535
Name:		texlive-screenplay
Version:	1.535
Release:	1
Summary:	A class file to typeset screenplays
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/screenplay
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/screenplay.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/screenplay.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/screenplay.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The class implements the format recommended by the Academy of
Motion Picture Arts and Sciences.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}