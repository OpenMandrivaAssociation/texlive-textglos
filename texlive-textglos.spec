# revision 30788
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-textglos
Version:	1.0
Release:	2
Summary:	TeXLive textglos package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textglos.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textglos.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textglos.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive textglos package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/textglos/textglos.sty
%doc %{_texmfdistdir}/doc/latex/textglos/README
%doc %{_texmfdistdir}/doc/latex/textglos/README.txt
%doc %{_texmfdistdir}/doc/latex/textglos/textglos.pdf
#- source
%doc %{_texmfdistdir}/source/latex/textglos/textglos.dtx
%doc %{_texmfdistdir}/source/latex/textglos/textglos.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
