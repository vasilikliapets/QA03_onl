#!/bin/bash
echo "Введите любое число:"
read number
if [ $number -ne 0 ]
	then
		if [ $number -gt 0 ]
			then
				echo "$number положительное"
			else
				echo "$number отрицательное"
		fi
	else
		echo "$number ноль"
fi
