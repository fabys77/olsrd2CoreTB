#!/bin/bash

addtables () {
echo "ToAdd" >>$3
echo "Table: $1" >>$3
echo "Route: $2" >>$3
ip rule add to $2 table 111 pref 38
ip rule add from $2 table 111 pref 38
#verso BGP
ip rule add from $2 lookup $1 pref 90
}


deltables () {
echo "ToRemove" >>$3
echo "Table: $1" >>$3
echo "Route: $2" >>$3
ip rule del to $2 table 111 pref 38
ip rule del from $2 table 111 pref 38
#verso BGP
ip rule del from $2 lookup $1 pref 90
}



newfile='/etc/ninux/compublic.new'
oldfile='/etc/ninux/compublic.old'
logfile='/var/log/nnx/route.log'


/bin/date >>$logfile
if [ -e $newfile ]; then
	mv $newfile $oldfile
else
	touch $oldfile
fi

cat /etc/olsrd2/olsrd2.conf | grep '^\[domain=[0-9]\{3\}' | cut -f 2 -d = | cut -f 1 -d ] |
while read TABLE; do
	SUBN=$(ip route show table $TABLE | grep -Ev ^default | grep -Ev ^blackhole | head -n1 | awk '{print $1}')
	if [ -z "$SUBN" ]; then continue;fi
	echo $TABLE $SUBN >> $newfile
	echo $TABLE $SUBN #DEBUG
done;

if [ ! -e $newfile ]; then
	touch $newfile
fi

#Cerchiamo le nuove rotte:
/usr/bin/diff $oldfile $newfile | grep ^\> | while read line; do
	TABLE=$(echo $line | awk '{print $2}')
	ROUTE=$(echo $line | awk '{print $3}')
	addtables $TABLE $ROUTE $logfile
done

/usr/bin/diff $oldfile $newfile | grep ^\< | while read line; do
	TABLE=$(echo $line | awk '{print $2}')
	ROUTE=$(echo $line | awk '{print $3}')
	deltables $TABLE $ROUTE $logfile
done

