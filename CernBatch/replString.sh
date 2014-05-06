#!/bin/sh
#
# replace a given string in a file using sed
#

nargs=$#
if [ $nargs -lt 1 ]
then
  echo
  echo "Please pass output directory name"
  exit
fi  
outdir=$1

for indx in {1..11}
do

  #oldstring="ijob=0"
  #newstring="ijob="${indx}

  oldstring="JOBID=0"
  newstring="JOBID="${indx}

  orgFile=HLTBitAnalysis_cfg.py
  newFile="$outdir"/HLTBitAnalysis_cfg_${indx}.py

    # echo $replstring
  # carrot at the beginning means replace only if oldstring occurs at beginning of line
  sed -e 's/^'$oldstring'/'$newstring'/' ${orgFile} > ${newFile}

done
