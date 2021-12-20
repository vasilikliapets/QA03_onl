#!/bin/bash 
echo "Введите число от 16 до 44: " 
read x 
if [ $x -gt "15" -a $x -lt "45" ]
then
	echo "$x больше 15 и меньше 45"
else
	echo "число $x вне требуемого диапазона"
fi

