%ifarch x86_64
%define libdirpart lib64
%define fpc_arch x86_64
%else
%define libdirpart lib
%define fpc_arch i386
%endif

Summary:        Tools for setup and control VPN via PPTP/L2TP
Summary(ru):    Инструмент для установки и управления соединением VPN через PPTP/L2TP
Summary(uk):    Інструмент для встановлення та керування з'єднанням VPN через PPTP/L2TP
Name:           vpnpptp
Version:        0.3.3
Release:        2%{?dist}

License:        GPL2
Group:          System Environment/Base
Url:            http://code.google.com/p/vpnpptp
Source0:        http://vpnpptp.googlecode.com/files/%{name}-src-%{version}.tar.gz
Source2:        %{name}.desktop
Source3:        ponoff.desktop
Source10:       Makefiles.tar.bz2
Source100:      make_source.sh
Source101:      change-opt.sh

# root auth
Source200:      vpnpptp.pam
Source201:      vpnpptp.consoleapp
Source202:      ponoff.pam
Source203:      ponoff.consoleapp

BuildRequires:  fpc-src >= 2.4.2
BuildRequires:  fpc >= 2.4.2
BuildRequires:  lazarus >= 0.9.29
BuildRequires:  desktop-file-utils

Requires:       pptp
Requires:       xl2tpd >= 1.2.7
Requires:       usermode-gtk
Requires:       open2ltp


%description
Tools for easy and quick setup and control VPN via PPTP/L2TP


%description -l ru
Инструмент для легкого и быстрого подключения и управления соединением
VPN через PPTP/L2TP


%description -l uk
Інструмент для легкого і швидкого підключення і керування з'єднанням
VPN через PPTP/L2TP


%prep
%setup -q -n %{name}-src-%{version}

tar xf %{SOURCE10}
for ext in pas lpi; do
    find . -type f -name *.${ext} -exec sh %{SOURCE101} {} \;
done;

%build
./mandriva.compile.sh %{fpc_arch} %{libdirpart}


%install
make LIBDIRPART=%{libdirpart} \
    INSTALL_ROOT=$RPM_BUILD_ROOT/usr \
    LIBDIR=$RPM_BUILD_ROOT/%{_libdir} \
    DATADIR=$RPM_BUILD_ROOT/%{_datadir}/%{name} \
    BINDIR=$RPM_BUILD_ROOT/%{_bindir} \
    MACHINE_ARCH=%{fpc_arch} install

install -dD $RPM_BUILD_ROOT/%{_sysconfdir}/{pam.d,security/console.apps}
install -m644 %{SOURCE200} $RPM_BUILD_ROOT/%{_sysconfdir}/pam.d/%{name}
install -m644 %{SOURCE202} $RPM_BUILD_ROOT/%{_sysconfdir}/pam.d/ponoff

install -m644 %{SOURCE201} \
    $RPM_BUILD_ROOT/%{_sysconfdir}/security/console.apps/%{name}
install -m644 %{SOURCE203} \
    $RPM_BUILD_ROOT/%{_sysconfdir}/security/console.apps/ponoff

install -dD $RPM_BUILD_ROOT/%{_localstatedir}/lib/%{name}

install -dD $RPM_BUILD_ROOT/%{_sbindir}
mv $RPM_BUILD_ROOT/%{_bindir}/* $RPM_BUILD_ROOT/%{_sbindir}
ln -s consolehelper $RPM_BUILD_ROOT%{_bindir}/%{name}
ln -s consolehelper $RPM_BUILD_ROOT%{_bindir}/ponoff

desktop-file-install \
    --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
    %{SOURCE2}

desktop-file-install \
    --remove-category=X-MandrivaLinux-CrossDesktop \
    --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
    %{SOURCE3}


%post
update-desktop-database -q


%postun
update-desktop-database -q


%files
%defattr(-,root, root)
%doc LICENSE.txt README.txt
%attr(0644,root,root) %config %{_sysconfdir}/pam.d/%{name}
%attr(0644,root,root) %config %{_sysconfdir}/security/console.apps/%{name}
%attr(0644,root,root) %config %{_sysconfdir}/pam.d/ponoff
%attr(0644,root,root) %config %{_sysconfdir}/security/console.apps/ponoff
%{_bindir}/%{name}
%{_bindir}/ponoff
%{_sbindir}/%{name}
%{_sbindir}/ponoff
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.ico
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/wiki/*
%{_datadir}/%{name}/lang/*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop
%{_localstatedir}/lib/%{name}


%changelog
* Wed Jul 20 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 0.3.3-2.R
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
