#!/bin/sh
#

if [ $# -lt 1 ]
then
    echo "Usage: toBatch.sh [cfgfile] [outputCastorDir]"
    echo " outputCastorDir is optional -- use it to copy output to Castor; output rootfile should go to local directory "
    echo " e.g. /castor/cern.ch/user/a/apana/205"
    echo "" 
    exit
fi

outputCastorDir=XXX
if [ $# -eq 2 ] 
then
  outputCastorDir=$2
fi

echo
echo ">>> Beginning cmsRun execution on `date`  <<<"
echo


# lsf provids a variable for the current working directory
dir=$LS_SUBCWD
# dir=$PWD
cd $dir

echo "Current directory: $dir"
echo ""
cfg=$PWD/$1

#echo "CPUINFO:"
#cat /proc/cpuinfo
#echo ""
#echo "MEMINFO:"
#cat /proc/meminfo
#echo ""


echo "Running cmsRun job with configuration file: $cfg"
echo "Current directory $PWD"

#eval `scramv1 runtime -sh`
if [ -n "${CMS_PATH:-}" ]; then
  echo "CMSSW computing environment already setup"
else
  export SCRAM_ARCH=`scramv1 arch`
fi
eval `scramv1 runtime -sh`


#echo -------------- Printing Configuation File ---------------------------
#echo
#cat $cfg
#echo --------------- End of Configuation File ---------------------------
cd -
echo "Current directory $PWD"
cmsRun -p $cfg
echo ""
echo "Directory listing:"
ls -xs 
echo " "

if [ ${outputCastorDir} != "XXX" ]
then
   for file in *.root
   do
     echo "Copying" $file " to " ${outputCastorDir}
     rfcp $file ${outputCastorDir}
     rm $file
   done
fi

echo
echo ">>> Ending cmsRun execution on `date`  <<<"
echo

exit
