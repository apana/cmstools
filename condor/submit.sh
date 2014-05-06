#!/bin/sh -f
##############################################
#This is script to submit EDAnalyzer jobs to the batch system. It takes 3 arguements
#
#$1 : Number of events per process
#$2 : lower edge of pt hat bin
#$3 : upper edge of pt hat bin

njobs=1

export WORKDIR=${PWD}
export WORKLOGS=${WORKDIR}/logs

if [ $# -lt 3 ] 
then
    echo "Usage: submit.sh [nevents] [ptmin] [ptmax]"
    exit
fi

echo " submitting: " ${1} "events in pt hat" ${4}-${5} "into the condor queue executing:"

submitScript=condorjob_${2}_${3}
jobScript=${PWD}/edanalyzer_cfg.sh

if [ -e ${submitScript} ]
then
    echo "Removing"
    /bin/rm -f ${submitScript}
fi

if [ ! -e ${WORKLOGS} ] 
then
  mkdir ${WORKLOGS}
fi

cat > ${submitScript} << +EOF

universe = vanilla
Executable = ${jobScript}

Requirements = Memory >= 500 && OpSys == "LINUX" && Arch == "INTEL"
#Requirements   = (Memory >= 1024 && OpSys == "LINUX" && (Arch == "INTEL" || Arch =="x86_64") && (Disk >= DiskUsage) && (TARGET.FileSystemDomain == MY.FileSystemDomain))
Should_Transfer_Files = NO
Output  = ${WORKLOGS}/job_\$(Cluster)_\$(Process).stdout
Error = ${WORKLOGS}/job_\$(Cluster)_\$(Process).stderr
Log = ${WORKLOGS}/job_\$(Cluster)_\$(Process).log
notify_user = ${LOGNAME}@fnal.gov
Arguments = \$(Process) ${1} ${2} ${3}
# LENGTH = "SHORT"
Queue ${njobs}

+EOF

/opt/condor/bin/condor_submit ${submitScript}
