#!/bin/bash
echo "Insert number:"
read number
if [ $number -gt 15 ] && [ $number -lt 45 ]
then 
	echo "True"
else
	echo "False"
fi
