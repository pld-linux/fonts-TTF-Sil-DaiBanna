Summary:	Free TrueType font for New Tai Lue script
Summary(pl.UTF-8):	Wolnodostępny font TrueType dla pisma nowe tai lue
Name:		fonts-TTF-Sil-DaiBanna
Version:	2.1
Release:	1
License:	SIL OFL, distributable
Group:		Fonts
# Source0Download:	http://scripts.sil.org/cms/scripts/render_download.php?site_id=nrsi&format=file&media_id=DaiBanna-2.1.zip&filename=DaiBanna-2.1.zip
Source0:	DaiBanna-%{version}.zip
# Source0-md5:	f78c170e5a600909bcdb1feb4d46f8cb
URL:		http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&item_id=DaiBannaSIL
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
he Dai Banna SIL Fonts include a complete set of New Tai Lue
consonants, vowels, tones and digits, along with punctuation and other
useful symbols. A basic set of Latin glyphs, including Arabic
numerals, is also provided. Chinese punctuation used in New Tai Lue
texts are included as well. Two font families, differing only in
weight, allow for a wide range of uses.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc doc/*
%{ttffontsdir}/DBSIL*.ttf
