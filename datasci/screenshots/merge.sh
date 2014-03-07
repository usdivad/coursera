#!/bin/bash

#Timing
start=`date +%s`

#Set $IFS so we don't get tripped on filenames with spaces
PREV_IFS=$IFS
IFS=$(echo -en "\n\b")

#cd the directory we want to grab images from
input=$1
cd ./$input
destination="../../lectures/${PWD##*/}.pdf"


#Create filelist
echo "" > filelist.txt

#Sort by name (ignore case), and add filenames to list with quotes around
for i in `ls *.png | sort -f`
do
    echo "'$i'" >> filelist.txt
done

#ImageMagick conversion (reduced size)
#convert @filelist.txt -filter box -sample 51% -compress zip -define pdf:extent=25000kb $destination
#convert @filelist.txt -filter gaussian -resize 66% -compress zip $destination

#full quality conversion
convert @filelist.txt -compress zip $destination

#Timing
end=`date +%s`
runtime=$((end-start))
msg="Converted in "
echo $msg$runtime "seconds"
times

#Reset $IFS to original value
IFS=$PREV_IFS