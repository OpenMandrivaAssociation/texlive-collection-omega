# revision 20778
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-omega
Version:	20120223
Release:	1
Summary:	Omega
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-omega.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-antomega
Requires:	texlive-lambda
Requires:	texlive-mxedruli
Requires:	texlive-omega
Requires:	texlive-aleph
Requires:	texlive-omegaware
Requires:	texlive-collection-basic
Requires:	texlive-collection-latex

%description
Omega, a 16-bit extended TeX by John Plaice and Yannis
Haralambous.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
