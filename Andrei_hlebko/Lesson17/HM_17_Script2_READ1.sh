#!/bin/bash
echo "Введите число:"
read x
if [ $x -gt 15 ] && [ $x -lt 45 ]
then
echo "Число в диапазоне от 15 до 45"
else
echo "Число не в нужно диапазоне!"
fi 

