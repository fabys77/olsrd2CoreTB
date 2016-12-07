#!/bin/bash
cat /etc/olsrd2/olsrd2.conf | grep '^\[domain=[0-9]\{3\}' | cut -f 2 -d = | cut -f 1 -d ] |
while read TABLE; do
 ip route show table $TABLE | grep -Ev ^default | grep -Ev ^blackhole | awk '{print $1}' |
  while read ROUTE ; do
   if [ "$TABLE" -gt 150 ] ; then 
    #echo "ip rule add from $ROUTE lookup $TABLE pref 90"
    #echo "ip rule add from $ROUTE lookup 222  pref 40"
    #echo "ip rule add to $ROUTE lookup 222  pref 42"
    ip rule add from $ROUTE lookup $TABLE pref 90
    ip rule add from $ROUTE lookup 111  pref 40
    ip rule add to $ROUTE lookup 111  pref 42
   fi
  done
done
echo "Fatto!"
