#!/bin/bash

echo "Введите букву"
read x

while [ "$x" != "x" ]
do
	if [ ${#x} -eq "1" ]
	then
		case $x in
			[[:lower:]])
				echo "Буква в нижнем регистре"
				;;
			[[:upper:]])
				echo "Буква в верхнем регистре"
				;;
			[":!@#$%^*()-_+=|\/?><,."])
				echo "Введен спецсимвол"
		esac
	else
		echo "Введено более одного символа"
	fi
	echo "Введите букву"
	read x
done
echo "Конец"

