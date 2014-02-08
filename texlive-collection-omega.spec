# revision 25844
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-omega
Epoch:		1
Version:	20120413
Release:	2
Summary:	Omega packages
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


%changelog
* Sat Apr 14 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120413-1
+ Revision: 790883
- Update to latest release.

* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120327-1
+ Revision: 787863
- Update to latest release.

* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780505
- Update to latest release.
- Import texlive-collection-omega
- Import texlive-collection-omega

