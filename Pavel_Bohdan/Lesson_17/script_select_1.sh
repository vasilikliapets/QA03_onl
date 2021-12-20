#!/bin/bash

echo "Хотите ли Вы установить python?"

select x in Да Нет
do
	if [ "$x" == "Да" ]
	then
		echo "Вы выбрали установить python"
	else
		echo "Уходи дверь закрой"
	fi
break
done
