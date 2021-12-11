#!/bin/bash

echo "Script name is $0"
if [ -n "$1" ]
then
	echo "list of arguments - $@"
	echo "number of arguments - $#"
else 
	echo "no arguments"
fi
echo "current directory is:"
pwd

exit 0
