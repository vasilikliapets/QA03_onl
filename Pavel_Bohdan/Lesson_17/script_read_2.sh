#!/bin/bash 
echo "Введите число меньше -1 либо 45: " 
read x 
if [ $x -lt "-1" -o $x -eq "45" ]
then
	echo "число $x введено корректно"
else
	echo "число $x вне требуемого диапазона"
fi

