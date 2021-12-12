#!/bin/bash
printf "Пожалуйста, введите букву:"
read lett
case $lett in
[[:lower:]])
echo "Буква в нижнем регистре"
;;
[[:upper:]])
echo "Буква в верхнем регистре"
;;
[0-9])
echo "Это число"
;;
*)
echo "Это спецсимвол"
esac
