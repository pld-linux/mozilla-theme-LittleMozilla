Summary:	Minimal chrome, maximum usability
Summary(pl):	Ma³e ikonki, maksymalna u¿yteczno¶æ
Name:		mozilla-theme-LittleMozilla
%define		_realname	littlemozilla
Version:	1.6b
%define	fver	%(echo %{version} | tr -d .)
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/themes/themes/%{_realname}_%{fver}.jar
# Source0-md5:	3f81d435d3599dd4c9e1efa7a9362ba6
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/themes/littlemozilla.html
Requires(post,postun):	textutils
Requires:	mozilla >= 5:1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

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

install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}/

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
