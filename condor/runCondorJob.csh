#!/bin/csh

        if ($#argv < 2) then
            echo "Please supply a configuration file and your working Directory"
            echo " "
            exit 1
        endif

set cfgFile=$argv[1]
set workDir=$argv[2]

echo "Beginning runCondorJob.csh"

echo "-------------------------------"
echo "Current Directory: "
pwd
echo "-------------------------------"

source /uscmst1/prod/sw/cms/setup/cshrc prod
cd $workDir

eval `scram runtime -csh`

echo "-------------------------------"
echo "Working Directory: "
pwd
echo "-------------------------------"


echo "Submitting job on `date`" 

cmsRun "$cfgFile"

echo "Job finished on `date`" 
