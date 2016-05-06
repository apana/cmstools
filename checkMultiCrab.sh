#!/bin/bash

if [ $# -lt 2 ]
then
    # echo "Please supply crab command e.g. status, kill, etc."
    echo "Usage: $0 logdir command"
    echo -e "\tcommand = status, kill, etc."
  exit 1
fi

if ! hash crab 2>/dev/null; then
    echo "Crab not setup -- Exiting"
    exit 1
fi

logDir=$1
command=$2

if [ $# -eq 3 ]
then
  command="$command $3"
fi

# echo $command
## for subdir in `ls $logDir | grep crab_l1-tsg-v2-AKfix__259626_ZeroBias`
## for subdir in `ls $logDir | grep -v ht40`
for subdir in `ls $logDir `
do
  echo -e "\n"
  dirName="$logDir"/"$subdir"
  ## echo $dirName
  echo crab $command -d $dirName
  crab $command -d $dirName
done
