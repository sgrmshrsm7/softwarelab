#!/bin/bash
arr=($1 $2 $3 $4 $5)
for string in "${arr[@]}"
do
	if [ "${#string}" -gt 4 ]
	then
		echo ${string}
	fi
done

