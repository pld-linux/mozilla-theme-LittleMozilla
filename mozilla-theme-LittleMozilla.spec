Summary:	Minimal chrome, maximum usability
Summary(pl):	Ma³e ikonki, maksymalna u¿yteczno¶æ
Name:		mozilla-theme-LittleMozilla
Version:	1.2
%define	fver	%(echo %{version} | tr -d .)
%define		_realname	littlemozilla_%{fver}
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.uk1.mozdev.org/rsync/themes/themes/%{_realname}.xpi
# Source0-md5:	b0e634c1cfc0bed04ed5b1337097ef23
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/themes/littlemozilla.html
BuildRequires:	unzip
Requires(post,postun):	textutils
Requires:	mozilla >= 1.2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_libdir}/mozilla/chrome

%description
Minimal chrome, maximum usability. A theme designed to be a clean,
simple and consequent UI for the Mozilla platform. Focus on reduced
screen space usage, improved interaction (almost everything that can
be clicked, responds on mouse hovering, etc.). Consequent use of
colours, and symbolics.

%description -l pl
Ma³e ikonki, maksymalna u¿yteczno¶æ. Motyw zaprojektowany tak, aby by³
przejrzystym, prostym i konsekwentnym interfejsem u¿ytkownika dla
platformy Mozilli. Skupiono siê na ograniczonym u¿yciu przestrzeni
ekranu, zwiêkszonej interakcji (prawie wszystko mo¿e byæ klikniête,
odpowiada na zbli¿enie kursora myszy itd.). Konsekwentne u¿ycie
kolorów i symboliki.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}
unzip %{SOURCE0} %{_realname}.jar -d $RPM_BUILD_ROOT%{_chromedir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
