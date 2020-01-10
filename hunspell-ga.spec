Name: hunspell-ga
Summary: Irish hunspell dictionaries
Version: 4.6
Release: 7%{?dist}
Source0: http://gaelspell.googlecode.com/files/ispell-gaeilge-%{version}.tar.gz
Source1: myspell-header
Source2: hunspell-header
Group: Applications/Text
URL: http://borel.slu.edu/ispell/index.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch
BuildRequires: hunspell-devel
Patch1: ispell-gaeilge-4.2-buildhunspell.patch

Requires: hunspell

%description
Irish hunspell dictionaries.

%prep
%setup -q -n ispell-gaeilge-%{version}
%patch1 -p1 -b .buildhunspell.patch

%build
make
cat %{SOURCE1} %{SOURCE2} > header
export LANG=en_IE.UTF-8
iconv -f utf-8 -t iso-8859-1 < gaeilge.aff > gaeilge.aff.iso-8859-1
ispellaff2myspell gaeilge.aff.iso-8859-1 --myheader header | sed -e "s/\"\"/0/g" | sed -e "s/\"//g" > ga_IE.aff

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ga_IE.dic ga_IE.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING ChangeLog
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4.6-7
- Mass rebuild 2013-12-27

* Tue May 28 2013 Caolán McNamara <caolanm@redhat.com> - 4.6-6
- Resolves: rhbz#967637 encoding bustage

* Mon May 27 2013 Caolán McNamara <caolanm@redhat.com> - 4.6-5
- Resolves: rhbz#967637 empty ga.aff

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 29 2011 Caolán McNamara <caolanm@redhat.com> - 4.6-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 31 2010 Caolán McNamara <caolanm@redhat.com> - 4.5-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 05 2008 Caolán McNamara <caolanm@redhat.com> - 4.4-1
- latest version

* Wed Mar 05 2008 Caolán McNamara <caolanm@redhat.com> - 4.3-3
- build the .aff from gaeilge.aff and ispellaff2myspell

* Tue Mar 04 2008 Caolán McNamara <caolanm@redhat.com> - 4.3-2
- update to latest .aff

* Mon Nov 05 2007 Caolán McNamara <caolanm@redhat.com> - 4.3-1
- latest version

* Mon Aug 20 2007 Caolán McNamara <caolanm@redhat.com> - 4.2-1
- bump to latest upstream

* Fri Aug 03 2007 Caolán McNamara <caolanm@redhat.com> - 0.20060731-2
- clarify license version

* Thu Dec 07 2006 Caolán McNamara <caolanm@redhat.com> - 0.20060731-1
- initial version
