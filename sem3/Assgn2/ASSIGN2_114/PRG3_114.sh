#!/bin/bash
file_name=$1
x=$2
while IFS= read -r line;
do
	arr=($line)
		if [ "$[arr[2]]" -gt "$x" ]
			then
				echo ${arr[0]}
		fi
done < "$file_name"
