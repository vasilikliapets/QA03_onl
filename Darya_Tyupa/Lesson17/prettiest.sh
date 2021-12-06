#!/bin/bash
PS3='Who is the prettiest in the whole world?'

echo

select option in "Guess I am" "Definitely I am" "I am not sure" 
do 
	case $option in
		"Guess I am" | "Definitely I am")
			echo "$option the prettiest in the hole world"
			break
			;;
		"I am not sure")
		       echo "So decide faster!!!"
		       break
		       ;;	       
	esac
done

exit 0

