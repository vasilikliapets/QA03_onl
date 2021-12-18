#!/bin/bash

echo "Кто на свете всех милее?"

select x in "вроде Я" "точно Я" "Пока не понял"
do
        if [ "$x" == "вроде Я" ]
        then
                echo "На свете всех милее вроде Я"
        else
		if [ "$x" == "точно Я" ]
		then
			echo "На свете всех милее точно Я"
		else
			echo "Так определяйся быстрее!!!"
		fi
        fi
break
done

