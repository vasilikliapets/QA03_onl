#!/bin/bash
echo "Введите число:"
read number
if [ $number -gt 15 -a $number -lt 45 ]
        then
		echo "Число  $number больше 15, но меньше 45"
	else
		echo "Число $number не удовлетворяет одновременному условию - больше 15 и меньше 45" 
fi
