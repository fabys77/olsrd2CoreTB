#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
while true; do
	$DIR/compublic.sh
	sleep 60
done
