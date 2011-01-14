#!/bin/sh
NAME=vpnpptp
LIBDIR=/var/lib/${NAME}
TMPDIR=/tmp/${NAME}
DATADIR=/usr/share/${NAME}
BINDIR=/usr/bin

sed -i "s|/opt/vpnpptp/config|${LIBDIR}/config|g" $1
sed -i "s|/opt/vpnpptp/ponoff.png|${DATADIR}/ponoff.png|g" $1
sed -i "s|/opt/vpnpptp/off.ico|${DATADIR}/off.ico|g" $1
sed -i "s|/opt/vpnpptp/on.ico|${DATADIR}/on.ico|g" $1
sed -i "s|/opt/vpnpptp/resolv.conf|${LIBDIR}/resolv.conf|g" $1
sed -i "s|/opt/vpnpptp/lang|${DATADIR}/lang|g" $1
sed -i "s|/opt/vpnpptp/hosts|${LIBDIR}/hosts|g" $1
sed -i "s|/opt/vpnpptp/vpnpptp.png|${DATADIR}/vpnpptp.png|g" $1
sed -i "s|/opt/vpnpptp/tmp|/${TMPDIR}|g" $1
sed -i "s|/opt/vpnpptp/scripts|${DATADIR}/scripts|g" $1
sed -i "s|/opt/vpnpptp/ponoff|${BINDIR}/ponoff|g" $1
sed -i "s|/opt/vpnpptp/route|${LIBDIR}/route|g" $1
sed -i "s|/opt/vpnpptp/vpnpptp|${BINDIR}/vpnpptp|g" $1
sed -i "s|/opt/vpnpptp/wiki|${DATADIR}/wiki|g" $1
