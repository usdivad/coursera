#!/bin/bash
DIRECTORIES=./*

for d in $DIRECTORIES
do
if [[ -d $d ]]
then
    #./test.sh $d
    ./merge.sh $d
fi
done