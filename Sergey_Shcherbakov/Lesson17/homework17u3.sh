#!/bin/bash
echo "Введите количество директорий которые будут созданы:"
read param1
eval mkdir {1..$param1}
exit 0
