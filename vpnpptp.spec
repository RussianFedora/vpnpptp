%define libdirpart lib
%define fpc_arch i386
%ifarch x86_64
    %define libdirpart lib64
    %define fpc_arch x86_64
%endif

Summary: Tools for setup and control VPN via PPTP/L2TP
Summary(ru): Инструмент для установки и управления соединением VPN через PPTP/L2TP
Summary(uk): Інструмент для встановлення та керування з'єднанням VPN через PPTP/L2TP
Name: vpnpptp
Version: 0.2.8
Release: 2%{?dist}
License: GPL2
Group: Network

Source0: %{name}-%{version}.tar.bz2
Source2: %{name}.desktop
Source3: ponoff.desktop
Source10: Makefiles.tar.bz2
Source100: make_source.sh
Source101: change-opt.sh

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: fpc-src >= 2.2.4 fpc >= 2.2.4 lazarus desktop-file-utils
Requires: beesu pptp xl2tpd

%description
Tools for easy and quick setup and control VPN via PPTP/L2TP
%description -l ru
Инструмент для легкого и быстрого подключения и управления соединением VPN через PPTP/L2TP
%description -l uk
Інструмент для легкого і швидкого підключення і керування з'єднанням VPN через PPTP/L2TP

%prep
%setup -q
tar xf %{SOURCE10}
for ext in pas lpi; do
    find . -type f -name *.${ext} -exec sh %{SOURCE101} {} \;
done;

%build
make VERBOSE=1 %{?_smp_mflags} LIBDIRPART=%{libdirpart} INSTALL_ROOT=$RPM_BUILD_ROOT/usr MACHINE_ARCH=%{fpc_arch}

%install
make LIBDIRPART=%{libdirpart} INSTALL_ROOT=$RPM_BUILD_ROOT/usr LIBDIR=$RPM_BUILD_ROOT/%{_libdir} DATADIR=$RPM_BUILD_ROOT/%{_datadir}/%{name} BINDIR=$RPM_BUILD_ROOT/%{_bindir} MACHINE_ARCH=%{fpc_arch} install
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2}
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE3}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root, root)
%{_bindir}/%{name}
%{_bindir}/ponoff
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.ico
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/wiki/*
%{_datadir}/%{name}/lang/*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop
%doc LICENSE.txt README.txt

%changelog
* Thu Jan 14 2011 Alexei Panov <elemc AT atisserv.ru> - 0.2.8-2
- change script for make source tarboll
- change from polkit to beesu. source code of the draft programming is rigidly tied to beesu
* Thu Jan 13 2011 Alexei Panov <elemc AT atisserv.ru> - 0.2.8-1
- Initial build
