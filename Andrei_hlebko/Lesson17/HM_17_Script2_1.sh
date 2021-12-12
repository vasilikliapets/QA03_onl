#!/bin/bash
lett=a
while [ "$lett" != "x" ]
do
echo "Пожалуйста введите букву:"
read lett
case $lett in
[[:lower:]])
echo "Буква в нижнем регистре"
;;
[[:upper:]])
echo "Буква в верхнем регистре"
;;
[0-9])
echo "Это цифра а не буква"
;;
*)
echo "Это спецсимвол а не буква"
;;
esac
done
exit 0


