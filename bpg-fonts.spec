%define fontname bpg
%define fontconf 64-%{fontname}.conf
%define common_ver 20090205

%define common_desc BPG Fonts are a set of GPL licensed Georgian Unicode fonts.


Name:		%{fontname}-fonts
Summary: 	Georgian Unicode fonts
Version:	%{common_ver}
Release:	6.1%{?dist}
# Font exception
# See: http://groups.google.com/group/bpg-fonts/web/gpl-gnu-license
# No version of the GPL is specified.
License:	GPL+ with exceptions
Group:		User Interface/X
# Source is actually http://bpg-fonts.googlegroups.com/web/BPG_GPL%26GNU_Fonts.zip
# but it is buried in Google Groups. Barf.
# Also, it has a & in its name, which confuses all sorts of things. 
# I renamed the zip file to replace & with _and_
Source0:	BPG_GPL_and_GNU_Fonts.zip
Source1:	%{name}-algeti-fontconfig.conf
Source2:	%{name}-chveulebrivi-fontconfig.conf
Source3:	%{name}-courier-fontconfig.conf
Source4:	%{name}-courier-s-fontconfig.conf
Source5:	%{name}-elite-fontconfig.conf
Source6:	%{name}-glaho-fontconfig.conf
Source7:	%{name}-ingiri-fontconfig.conf
Source8:	%{name}-nino-medium-fontconfig.conf
Source9:	%{name}-nino-medium-cond-fontconfig.conf
Source10:	%{name}-sans-fontconfig.conf
Source11:	%{name}-sans-medium-fontconfig.conf
Source12:	%{name}-sans-modern-fontconfig.conf
Source13:	%{name}-sans-regular-fontconfig.conf
Source14:	%{name}-serif-fontconfig.conf
Source15:	%{name}-serif-modern-fontconfig.conf
URL:		http://groups.google.com/group/bpg-fonts
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	fontpackages-devel
BuildArch:	noarch

%description
%common_desc

%package common
Summary:	Common files for BPG Georgian fonts (documentation...)
Group:		User Interface/X
Requires:	fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other BPG font packages.

%package -n %{fontname}-algeti-fonts
Summary:	Algeti Family of BPG Georgian Fonts
Version:	2.005
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-algeti-fonts
%common_desc

This package contains the Algeti font family.

%_font_pkg -n algeti -f %{fontconf}-algeti.conf "BPG_Algeti*.ttf"

%package -n %{fontname}-chveulebrivi-fonts
Summary:	Chveulebrivi family of BPG Georgian fonts
Version:	3.002
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-chveulebrivi-fonts
%common_desc

This package contains the Chveulebrivi font family.

%_font_pkg -n chveulebrivi -f %{fontconf}-chveulebrivi.conf "BPG_Chveulebrivi_*.ttf"

%package -n %{fontname}-courier-fonts
Summary:	Courier family of BPG Georgian fonts
Version:	4.002
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-courier-fonts
%common_desc

This package contains the Courier font family.

%_font_pkg -n courier -f %{fontconf}-courier.conf "BPG_Courier_GPL*.ttf"

%package -n %{fontname}-courier-s-fonts
Summary:	Courier S family of BPG Georgian fonts
Version:	4.000
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-courier-s-fonts
%common_desc

This package contains the Courier S font family.

%_font_pkg -n courier-s -f %{fontconf}-courier-s.conf "BPG_Courier_S*.ttf"

%package -n %{fontname}-elite-fonts
Summary:	Elite family of BPG Georgian fonts
Version:	3.000
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-elite-fonts
%common_desc

This package contains the Elite font family.

%_font_pkg -n elite -f %{fontconf}-elite.conf "BPG_Elite*.ttf"

%package -n %{fontname}-glaho-fonts
Summary:	Glaho family of BPG Georgian fonts
Version:	9.000
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-glaho-fonts
%common_desc

This package contains the Glaho font family.

%_font_pkg -n glaho -f %{fontconf}-glaho.conf "BPG_Glaho*.ttf"

%package -n %{fontname}-ingiri-fonts
Summary:	Ingiri family of BPG Georgian fonts
Version:	4.000
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-ingiri-fonts
%common_desc

This package contains the Ingiri font family.

%_font_pkg -n ingiri -f %{fontconf}-ingiri.conf "BPG_Ingiri*.ttf"

%package -n %{fontname}-nino-medium-fonts
Summary:	Nino Medium family of BPG Georgian fonts
Version:	4.005
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n	%{fontname}-nino-medium-fonts
%common_desc

This package contains the Nino Medium font family.

%_font_pkg -n nino-medium -f %{fontconf}-nino-medium.conf "BPG_Nino_Medium_GPL*.ttf"

%package -n %{fontname}-nino-medium-cond-fonts
Summary:	Nino Medium Cond family of BPG Georgian fonts
Version:	4.005
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-nino-medium-cond-fonts
%common_desc

This package contains the Nino Medium Cond font family.

%_font_pkg -n nino-medium-cond -f %{fontconf}-nino-medium-cond.conf "BPG_Nino_Medium_Cond*.ttf"

%package -n %{fontname}-sans-fonts
Summary:	Sans family of BPG Georgian fonts
Version:	1.005
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-sans-fonts
%common_desc

This package contains the Sans font family.

%_font_pkg -n sans -f %{fontconf}-sans.conf "BPG_Sans_GPL*.ttf"

%package -n %{fontname}-sans-medium-fonts
Summary:	Sans Medium family of BPG Georgian fonts
Version:	1.005
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-sans-medium-fonts
%common_desc

This package contains the Sans Medium font family.

%_font_pkg -n sans-medium -f %{fontconf}-sans-medium.conf "BPG_Sans_Medium*.ttf"

%package -n %{fontname}-sans-modern-fonts
Summary:	Sans Modern family of BPG Georgian fonts
Version:	2.025
License:	Bitstream Vera
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n	%{fontname}-sans-modern-fonts
%common_desc

This package contains the Sans Modern font family.

%_font_pkg -n sans-modern -f %{fontconf}-sans-modern.conf "BPG_Sans_Modern*.ttf"

%package -n %{fontname}-sans-regular-fonts
Summary:	Sans Regular family of BPG Georgian fonts
Version:	1.005
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-sans-regular-fonts
%common_desc

This package contains the Sans Regular font family.

%_font_pkg -n sans-regular -f %{fontconf}-sans-regular.conf "BPG_Sans_Regular*.ttf"

%package -n %{fontname}-serif-fonts
Summary:	Serif family of BPG Georgian fonts
Version:	1.005
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-serif-fonts
%common_desc

This package contains the Serif font family.

%_font_pkg -n serif -f %{fontconf}-serif.conf "BPG_Serif_GPL*.ttf"

%package -n %{fontname}-serif-modern-fonts
Summary:	Serif Modern family of BPG Georgian fonts
Version:	2.028
License:	Bitstream Vera
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-serif-modern-fonts
%common_desc

This package contains the Serif Modern font family.

%_font_pkg -n serif-modern -f %{fontconf}-serif-modern.conf "BPG_Serif_Modern*.ttf"

%prep
%setup -q -c -n %{name}
%{__unzip} -qqo "%{SOURCE0}"
# correct end-of-line encoding
sed -i 's/\r//' "Docs/BPG_GPL&GNU_Fonts.txt"

%build

%install
rm -rf %{buildroot}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-algeti.conf
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-chveulebrivi.conf
install -m 0644 -p %{SOURCE3} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-courier.conf
install -m 0644 -p %{SOURCE4} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-courier-s.conf
install -m 0644 -p %{SOURCE5} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-elite.conf
install -m 0644 -p %{SOURCE6} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-glaho.conf
install -m 0644 -p %{SOURCE7} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-ingiri.conf
install -m 0644 -p %{SOURCE8} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-nino-medium.conf
install -m 0644 -p %{SOURCE9} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-nino-medium-cond.conf
install -m 0644 -p %{SOURCE10} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p %{SOURCE11} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-medium.conf
install -m 0644 -p %{SOURCE12} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-modern.conf
install -m 0644 -p %{SOURCE13} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-regular.conf
install -m 0644 -p %{SOURCE14} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif.conf
install -m 0644 -p %{SOURCE15} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif-modern.conf

for fontconf in %{fontconf}-algeti.conf %{fontconf}-chveulebrivi.conf %{fontconf}-courier.conf %{fontconf}-courier-s.conf\
		%{fontconf}-elite.conf %{fontconf}-glaho.conf %{fontconf}-ingiri.conf %{fontconf}-nino-medium.conf\
		%{fontconf}-nino-medium-cond.conf %{fontconf}-sans.conf %{fontconf}-sans-medium.conf %{fontconf}-sans-modern.conf\
		%{fontconf}-sans-regular.conf %{fontconf}-serif.conf %{fontconf}-serif-modern.conf
do
	ln -s %{_fontconfig_templatedir}/$fontconf %{buildroot}%{_fontconfig_confdir}/$fontconf
done

%clean
rm -rf %{buildroot}

%files common
%defattr(0644,root,root,0755)
%doc Docs/*
%dir %{_fontdir}

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 20090205-6.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090205-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Tom "spot" Callaway <tcallawa@redhat.com> 20090205-5
- take & out of filename

* Tue Feb 17 2009 Tom "spot" Callaway <tcallawa@redhat.com> 20090205-4
- missing semicolon in fontconfig files

* Tue Feb 17 2009 Tom "spot" Callaway <tcallawa@redhat.com> 20090205-3
- fix fontconfig files to not use reserved character, alias for fonts with old names

* Thu Feb 12 2009 Tom "spot" Callaway <tcallawa@redhat.com> 20090205-2
- update fontconfig files, change priority to 64
- don't need to own fontdir in -common, but we'll leave it in for good measure.

* Thu Feb 5 2009 Tom "spot" Callaway <tcallawa@redhat.com> 20090205-1
- update to 20090205 source with proper licensing

* Tue Feb 3 2009 Tom "spot" Callaway <tcallawa@redhat.com> 20090203-1
- Initial package for Fedora
