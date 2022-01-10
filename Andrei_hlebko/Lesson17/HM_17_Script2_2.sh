#!/bin/bash
echo "Кто на свете всех милее?"
select who in "Вроде Я" "Точно Я" "Пока не поняла"
do
case $who in
"Вроде Я" | "Точно Я")
echo "На свете всех милее $who"
break
;;
"Пока не поняла")
echo "Так определяйся быстрее!!!"
break
;;
esac
done 
exit 0

