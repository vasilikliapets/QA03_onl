#!/bin/bash
echo "Хотели бы вы установить python?"
select option in Yes No
do
case $option in
Yes)
echo "Вы выбрали установить python"
break
;;
No)
echo "Уходи и дверь закрой"
break
;;
esac
done
exit 0
