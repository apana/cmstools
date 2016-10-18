#!/bin/csh
#
# setup script for running Crab at CERN
#
## if ( $?GRID_ENV_LOCATION ) then
##   echo "Grid environment already setup"
## else
##   set SL6=`cat /etc/redhat-release | grep -c Carbon`
##   if ($SL6 == 0) then
##     echo "Setting up ui environment"
##     source /afs/cern.ch/cms/LCG/LCG-2/UI/cms_ui_env.csh
##   endif
## endif
## 
## # echo "Setting up CMSSW environment"
## # cmsenv
## echo
## echo "Setting up default CRAB"
## source /afs/cern.ch/cms/ccs/wm/scripts/Crab/crab.csh 
## 
## #echo "Setting up CRAB 2_1_2"
## #source /afs/cern.ch/cms/ccs/wm/scripts/Crab/CRAB_2_1_2/crab.csh 
##

echo "\nSetting up CRAB3"
## source /cvmfs/cms.cern.ch/crab3/crab.csh
source /cvmfs/cms.cern.ch/crab3/crab_standalone.csh
## eval `sh /cvmfs/cms.cern.ch/crab3/crab.sh -csh`
crab --version

echo
echo "Checking proxy"
voms-proxy-info
echo "    If needed, execute:  voms-proxy-init -voms cms -valid 168:0"
echo ""
