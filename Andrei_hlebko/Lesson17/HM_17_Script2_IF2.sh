#!/bin/bash
mydir=$1
if [ -d $mydir ] || [ -e $mydir]
then
if [ -d $mydir ]
then
echo "The Directory exist"
else
echo "The File exist"
fi
else
echo "There is not such directory or file"
fi


