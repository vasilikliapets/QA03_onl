#!/bin/bash

x=$1

if [ -f $x ]
then
	echo "$x является файлом"
else
	if [ -d $x ]
	then
		echo "$x является директорией"
	else
		echo "$x не является ни файлом, ни директорией"
	fi
fi

