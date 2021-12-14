#!/bin/bash
echo "Insert number:"
read number
if [ $number -lt -1 ] || [ $number -eq 45 ]
then 
	echo "True"
else
	echo "False"
fi
