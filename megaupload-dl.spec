Name:		megaupload-dl
Version:	0.3.3
Release:	%mkrel 1 
Summary:	Megaupload automatic downloader
Group:		Networking/File transfer
License:	GPLv3
URL:		http://code.google.com/p/megaupload-dl/
Source0:	http://megaupload-dl.googlecode.com/files/%{name}-%{version}.tgz
Source1:	megaupload.com.terms.txt
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-beautifulsoup
BuildRequires:	python-imaging
BuildRequires:	tesseract
BuildRequires:	python-devel
Requires:	python-base >= 2.6
Requires:	python-beautifulsoup
Requires:	python-imaging
Requires:	tesseract
BuildArch:	noarch

%description
Megaupload-dl helps on the painful process of downloading
files hosted on the popular Megaupload site if you don't have
a premium account. The process is completely automatic as the
captcha is recognized using a OCR. The script
(run from the command line, there is no GUI) only returns the file link;
use your favorite web downloader to actually get the file.

%prep
%setup -q -n %{name}
cp %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

rm -rf %buildroot%{_datadir}/doc/megaupload_dl

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CHANGELOG README examples/* megaupload.com.terms.txt
%{_bindir}/*
%{py_puresitedir}/megaupload_dl
%{py_puresitedir}/*.egg-info
%{_datadir}/megaupload_dl/news_gothic_bt.ttf


%changelog
* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 0.3.3-1mdv2011.0
+ Revision: 598842
- update file list

* Tue Feb 23 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.3.3-1mdv2010.1
+ Revision: 510301
- update to 0.3.3
- fix requires
- fix file list

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.2.1-2mdv2010.0
+ Revision: 439796
- rebuild

* Fri Feb 06 2009 Jérôme Soyer <saispo@mandriva.org> 0.2.1-1mdv2009.1
+ Revision: 338185
- import megaupload-dl


