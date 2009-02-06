Name:		megaupload-dl
Version:	0.2.1
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

%build


%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CHANGELOG README examples/* megaupload.com.terms.txt
%{_bindir}/megaupload_dl
%{py_puresitedir}/megaupload_dl
%{py_puresitedir}/*.egg-info
%exclude %{_datadir}/doc/megaupload_dl
