#!/bin/bash
way=$1
if [ -d $1 ] || [ -e $1 ]
then
	if [ -d $1 ]
	then 
		echo "The directory exist"
	else
		echo "The file exist"
	fi
else
	echo "There is no such file or directory"
fi
