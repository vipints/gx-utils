#!/bin/bash 
##
# compress the files from base folder. 
# 
##

set -e

# input requirement 
if [ -z "$1" ]
then
    echo "Usage: $0 <threads>"
    exit 1
else
    threads="$1"
fi

counter="0"

## start to search for flat files named *.dat from the current folder
for file in `find . -type f -name *.dat`
do
    counter=$(($counter+1))
    echo compressing $file
   
    ## compress with lzma 
    lzma -9 $file &

    ## utilize the resources in parallel mode
    if [ "$counter" -eq "$threads" ]
    then
        wait
        echo 
        counter="0"
    fi
done


