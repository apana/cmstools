#!/bin/sh
#
# replace a given string in a file using sed
#

nargs=$#
if [ $nargs -lt 3 ]
then
  echo "Usage: replString <cfg> <dir> <njobs>"
  echo
  exit
fi  
cfgFile=$1
outdir=$2
njobs=$3

if [ ! -d "$outdir" ]         #  Test whether directory exist.
then                          #  make it if not
  mkdir $outdir               
fi


len=$((${#cfgFile}-3))
cfgBase=${cfgFile:0:${len}}
# echo $cfgBase $len

for (( indx=1; indx<="$njobs"; indx++ ))
do

  oldstring="JOBID=0"
  newstring="JOBID="${indx}

  orgFile=${cfgFile}
  newFile="$outdir"/"$cfgBase"_${indx}.py

  # carrot at the beginning means replace only if oldstring occurs at beginning of line
  sed -e 's/^'$oldstring'/'$newstring'/' ${orgFile} > ${newFile}

done
