#!/bin/bash
PS3='Хотите ли Вы установить python? '
echo
select option in "да" "нет"
	do
	case $option in
		("да") echo "Вы выбрали установить python"
			break
			;;
		("нет") echo "Уходи дверь закрой"
			break
			;;
	esac
	done
exit 
