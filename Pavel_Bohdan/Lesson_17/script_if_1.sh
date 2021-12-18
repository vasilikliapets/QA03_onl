#!/bin/bash

x=$1

if [ "$x" -eq "0" ]
then
	echo "$x равно 0"
else
	if [ "$x" -gt "0" ]
	then
		echo "$x положительное"
	else
		echo "$x отрицательное"
	fi
fi



	
