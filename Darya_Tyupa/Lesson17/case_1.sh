#!/bin/bash
printf 'Please, insert a letter: '
read var
case $var in
	[[:lower:]])
		echo "The letter in lower case"
		;;
	[[:upper:]])
		echo "The letter in upper case"
		;;
	[0-9])
		echo "It is a number"
		;;
esac	
