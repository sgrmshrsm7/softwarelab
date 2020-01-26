#!/bin/bash
rollno=$1
file_name=$2
while IFS= read -r line
do
        arr=($line)
        for word in $arr
        do
                if [ "$word" == "$rollno" ]
                        then
                                echo ${arr[1]} ${arr[2]} ${arr[3]}
                fi
        done
done <"$file_name"


