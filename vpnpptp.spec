Name:           vpnpptp
Version:        0.3.4
Release:        2%{?dist}
Summary:        Tools for setup and control VPN via PPTP/L2TP/OpenL2TP
Summary(ru):    Инструмент для установки и управления VPN через PPTP/L2TP/OpenL2TP
Summary(uk):    Інструмент для встановлення та керування VPN через PPTP/L2TP/OpenL2TP

License:        GPLv2
Group:          Applications/System
Url:            http://code.google.com/p/vpnpptp
Source0:        http://vpnpptp.googlecode.com/files/%{name}-src-%{version}.tar.gz


BuildRequires:  fpc-src >= 2.4.2
BuildRequires:  fpc >= 2.4.2
BuildRequires:  lazarus >= 0.9.30

Requires:       xroot
Requires:       pptp
Requires:       xl2tpd >= 1.2.7
Requires:       openl2tp

%description
Tools for easy and quick setup and control VPN via PPTP/L2TP/OpenL2TP

%description -l ru
Инструмент для легкого и быстрого подключения и управления соединением
VPN через PPTP/L2TP/OpenL2TP

%description -l uk
Інструмент для легкого і швидкого підключення і керування з'єднанням
VPN через PPTP/L2TP/OpenL2TP

%prep
%setup -q -n %{name}-src-%{version}

%build
%ifarch x86_64
    ./mandriva.compile.sh x86_64 lib64
%else
    ./mandriva.compile.sh i386 lib
%endif

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/vpnpptp
mkdir -p %{buildroot}%{_datadir}/vpnpptp/scripts
mkdir -p %{buildroot}%{_datadir}/vpnpptp/wiki
mkdir -p %{buildroot}%{_datadir}/vpnpptp/lang
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps

cp -f ./vpnpptp/vpnpptp %{buildroot}%{_bindir}
cp -f ./ponoff/ponoff %{buildroot}%{_bindir}
cp -f ./ponoff.png %{buildroot}%{_datadir}/pixmaps/
cp -f ./vpnpptp.png %{buildroot}%{_datadir}/pixmaps/
chmod 0644 %{buildroot}%{_datadir}/pixmaps/ponoff.png
chmod 0644 %{buildroot}%{_datadir}/pixmaps/vpnpptp.png
cp -f ./*.ico %{buildroot}%{_datadir}/vpnpptp
cp -f ./vpnlinux %{buildroot}%{_bindir}
cp -rf ./scripts %{buildroot}%{_datadir}/vpnpptp/
cp -rf ./wiki %{buildroot}%{_datadir}/vpnpptp/
cp -rf ./lang %{buildroot}%{_datadir}/vpnpptp/

install -dm 755 %{buildroot}%{_datadir}/applications
cat > ponoff.desktop << EOF
#!/usr/bin/env xdg-open

[Desktop Entry]
Encoding=UTF-8
GenericName=VPN PPTP/L2TP/OpenL2TP Control
GenericName[ru]=Управление соединением VPN PPTP/L2TP/OpenL2TP
GenericName[uk]=Керування з'єднанням VPN PPTP/L2TP/OpenL2TP
Name=ponoff
Name[ru]=ponoff
Name[uk]=ponoff
Exec=/usr/bin/ponoff
Comment=Control VPN via PPTP/L2TP/OpenL2TP
Comment[ru]=Управление соединением VPN через PPTP/L2TP/OpenL2TP
Comment[uk]=Керування з'єднанням VPN через PPTP/L2TP/OpenL2TP
Icon=/usr/share/pixmaps/ponoff.png
Type=Application
Categories=GTK;System;Network;Monitor;X-MandrivaLinux-CrossDesktop;
X-KDE-autostart-after=kdesktop
StartupNotify=false
EOF
install -m 0644 ponoff.desktop \
%{buildroot}%{_datadir}/applications/ponoff.desktop

install -dm 755 %{buildroot}%{_datadir}/applications
cat > vpnpptp.desktop << EOF
#!/usr/bin/env xdg-open

[Desktop Entry]
Encoding=UTF-8
GenericName=VPN PPTP/L2TP/OpenL2TP Setup
GenericName[ru]=Настройка соединения VPN PPTP/L2TP/OpenL2TP
GenericName[uk]=Налаштування з’єднання VPN PPTP/L2TP/OpenL2TP
Name=vpnpptp
Name[ru]=vpnpptp
Name[uk]=vpnpptp
Exec=/usr/bin/vpnpptp
Comment=Setup VPN via PPTP/L2TP/OpenL2TP
Comment[ru]=Настройка соединения VPN PPTP/L2TP/OpenL2TP
Comment[uk]=Налаштування з’єднання VPN PPTP/L2TP/OpenL2TP
Icon=/usr/share/pixmaps/vpnpptp.png
Type=Application
Categories=GTK;System;Network;Monitor;X-MandrivaLinux-CrossDesktop;
StartupNotify=false
EOF
install -m 0644 vpnpptp.desktop \
%{buildroot}%{_datadir}/applications/vpnpptp.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-,root, root)

%{_bindir}/vpnpptp
%{_bindir}/ponoff
%{_bindir}/vpnlinux
%{_datadir}/vpnpptp/lang
%{_datadir}/pixmaps/ponoff.png
%{_datadir}/pixmaps/vpnpptp.png
%{_datadir}/vpnpptp/*.ico
%{_datadir}/vpnpptp/scripts
%{_datadir}/vpnpptp/wiki
%{_datadir}/applications/ponoff.desktop
%{_datadir}/applications/vpnpptp.desktop

%changelog
* Tue May 11 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.3.4-2.R
- clean spec

* Tue Apr 19 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.3.4-1.R
- update to 0.3.4

* Wed Jul 20 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 0.3.3-3.R
- corrected requires

* Wed Jul 20 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 0.3.3-1.R
- update to 0.3.3

* Mon Jun 20 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.3.2-1.R
- update to 0.3.2

* Sat Feb 19 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.3.0-1
- update to 0.3.0

* Mon Jan 24 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.2.8-5
- add R: usermode-gtk

* Fri Jan 14 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.2.8-4
- create /var/lib/vpnpptp dir

* Fri Jan 14 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.2.8-3
- clean up spec
- works via consolehelper

* Thu Jan 14 2011 Alexei Panov <elemc AT atisserv.ru> - 0.2.8-2
- change script for make source tarboll
- change from polkit to beesu. source code of the draft programming is rigidly tied to beesu

* Thu Jan 13 2011 Alexei Panov <elemc AT atisserv.ru> - 0.2.8-1
- Initial build
