#!/bin/bash
echo "Введите букву:"
read letter
case $letter in
       	([[:lower:]]) echo "Буква находится в нижнем регистре"
	       	;;
       	([[:upper:]]) echo "Буква находится в верхем регистре"
	       	;;
      	([0-9]) echo "Это число, а не буква"
		;;
esac

	

