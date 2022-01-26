#!/bin/bash
echo "Введите число:"
read number
if [ $number -lt -1 -o $number -eq 45 ]
        then
                echo "Число $number меньше -1 или равно 45"
        else
                echo "Число $number не удовлетворяет условию - меньше -1 или равно 45" 
fi
