#!/bin/bash
PS3='Do you want to install python?'

echo

select option in Yes No
do 
	case $option in
		Yes)
			echo "You choosed to install python"
			break
			;;
		No)
			echo "Get out!"
			break
			;;
	esac
done

exit 0

