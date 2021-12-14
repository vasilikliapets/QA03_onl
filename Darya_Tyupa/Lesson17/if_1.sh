#!/bin/bash
number=$1
if [ $1 -ne 0 ]
then
	if [ $1 -gt 0 ]
	then 
		echo "$1 is a pozitive number"
	else 
		echo "$1 is a negative number"
	fi
else
       echo "$1"
fi

