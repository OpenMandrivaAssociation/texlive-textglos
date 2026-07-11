%global tl_name textglos
%global tl_revision 30788

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Typeset and index linguistic gloss abbreviations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/textglos
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/textglos.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/textglos.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/textglos.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a set of macros for in-line linguistic examples (as
opposed to interlinear glossing, set apart from the main text). It
prevents hyphenated examples from breaking across lines and consistently
formats phonemic examples, orthographic examples, and more.

