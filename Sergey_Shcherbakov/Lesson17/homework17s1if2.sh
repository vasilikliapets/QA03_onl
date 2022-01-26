#!/bin/bash
echo "Введите путь к файлу/директории:"
read path
if [ -e $path ]
	then
		if [ -d $path ]
			then
				echo "Директория есть"
			else
				echo "Файл есть"
		fi
	else
		echo "Файла/директории нет"
fi
