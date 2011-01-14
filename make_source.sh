#!/bin/sh
# Script for make source-tree and pack it to tarboll
# Use: make_source.sh 0.2.8 - for download and make vpnpptp-0.2.8.tar.bz2
# or make_source.sh latest - to download and make vpnpptp-svn<current date>.tar.bz2 from trunk

NAME=vpnpptp
SVN_BIN=/usr/bin/svn
SVN_ADDITION=branches/0.2.8
ARCHIVE_NAME=${NAME}-0.2.8
if [ "$1" == "latest" ]; then
    SVN_DATE=`date +%Y%m%d`
    ARCHIVE_NAME=${NAME}-svn${SVN_DATE}
    SVN_ADDITION=trunk/
else
    ARCHIVE_NAME=${NAME}-$1
    SVN_ADDITION=branches/$1
fi

if [ -x $SVN_BIN ]; then
	$SVN_BIN checkout http://vpnpptp.googlecode.com/svn/${SVN_ADDITION} $ARCHIVE_NAME
	cd $ARCHIVE_NAME
	find . -type d -name .svn -exec rm -rf {} \;
	cd ..
	tar cfjv $ARCHIVE_NAME.tar.bz2 ./$ARCHIVE_NAME
	rm -rf $ARCHIVE_NAME
fi
