#!/bin/bash
##############################################
#
#This is script to submit EDAnalyzer jobs to the condor batch system.
#

# --------------------------------------------------
# functions:
# --------------------------------------------------

makeJDL()
{

if [ -e ${jdlfile} ]
then
    echo "Removing " ${jdlfile}
    /bin/rm -f ${jdlfile}
fi

cat > ${jdlfile} << +EOF

universe = vanilla
Executable = ${condorScript}
should_transfer_files = NO
Output = ${WORKLOGS}/${jobName}_\$(Cluster)_\$(Process).stdout
Error  = ${WORKLOGS}/${jobName}_\$(Cluster)_\$(Process).stderr
Log    = ${WORKLOGS}/${jobName}_\$(Cluster)_\$(Process).condor
notify_user = ${USER}@fnal.gov
Requirements          = Memory >= 199 && OpSys == "LINUX" && (Arch != "DUMMY")
Arguments = \$(Cluster) \$(Process) ${jobName} ${runDir} ${jobScript} ${nevts}
Queue ${njobs}

+EOF
return
}

makeCondor()
{
if [ -e ${condorScript} ]
then
    echo "Removing " ${condorScript}
    /bin/rm -f ${condorScript}
fi

setupCMS='eval `scramv1 runtime -sh`'

cat > ${condorScript} << +EOF
#!/bin/bash

#
# variables from arguments string in jdl
#
# format:
#
# 1: condor cluster number
# 2: condor process number
# 3: CMSSW_DIR
# 4: RUN_DIR
# 5: PARAMETER_SET (full path, has to contain all needed files in PoolSource and filled following variables with keywords: maxEvents = CONDOR_MAXEVENTS, skipEvents = CONDOR_SKIPEVENTS, output fileName = CONDOR_OUTPUTFILENAME)
# 6: NUM_EVENTS_PER_JOB
#

CONDOR_CLUSTER=\$1
CONDOR_PROCESS=\$2
JOB_NAME=\$3
RUN_DIR=\$4
PARAMETER_SET=\$5
NUM_EVENTS_PER_JOB=\$6

#
# header 
#

echo ""
echo "CMSSW on Condor"
echo ""

#
# setup software environment at FNAL for the given CMSSW release
#
. /uscmst1/prod/sw/cms/shrc prod
if [ -n "\${CMS_PATH:-}" ]; then
    echo "CMSSW computing environment already setup"
else
    echo "Setting up CMSSW computing environment"
    export PATH=/bin:/usr/bin:/usr/local/bin:/usr/krb5/bin:/usr/afsws/bin:/usr/krb5/bin/aklog:{$\PATH}
    . /uscmst1/prod/sw/cms/shrc prod
    export SCRAM_ARCH=\`scramv1 arch\`
fi
$setupCMS


START_TIME=\`/bin/date\`
echo "started at \$START_TIME"

echo ""
echo "CONDOR_CLUSTER: \$CONDOR_CLUSTER"
echo "CONDOR_PROCESS: \$CONDOR_PROCESS"
echo "JOB_NAME: \$JOB_NAME"
echo "CMSSW_DIR: \${CMSSW_BASE}/src"
echo "RUN_DIR: \${RUN_DIR}"
echo "PARAMETER_SET: \$PARAMETER_SET"
echo "NUM_EVENTS_PER_JOB: \$NUM_EVENTS_PER_JOB"
#
# change to working directory
#
cd \${RUN_DIR}
#
# modify parameter-set
#

FINAL_PARAMETER_SET_NAME=\`echo \${JOB_NAME}_\${CONDOR_CLUSTER}_\${CONDOR_PROCESS}\`
FINAL_PARAMETER_SET=\`echo ${WORKLOGS}/\$FINAL_PARAMETER_SET_NAME.cfg\`
FINAL_LOG=\`echo ${WORKLOGS}/\$FINAL_PARAMETER_SET_NAME.log\`
FINAL_FILENAME=\`echo \$FINAL_PARAMETER_SET_NAME.root\`
echo ""
echo "Writing final parameter-set: \$FINAL_PARAMETER_SET"
echo ""

let "skip = \$CONDOR_PROCESS * \$NUM_EVENTS_PER_JOB"
cat \$PARAMETER_SET | sed -e s/CONDOR_MAXEVENTS/\$NUM_EVENTS_PER_JOB/ | sed -e s/CONDOR_SKIPEVENTS/\$skip/ | sed -e "s/CONDOR_OUTPUTFILENAME/\$FINAL_FILENAME/" > \$FINAL_PARAMETER_SET

#
# run cmssw
#

echo "run: time cmsRun \$FINAL_PARAMETER_SET > \$FINAL_LOG 2>&1"
cmsRun \$FINAL_PARAMETER_SET >> \$FINAL_LOG 2>&1
exitcode=\$?

#
# end run
#

echo ""
END_TIME=\`/bin/date\`
echo "finished at \$END_TIME"
echo "Now trying to copy output to dCache"

exit \$exitcode

+EOF
chmod +x ${condorScript}
return
}
# --------------------------------------------------
# main routine:
# --------------------------------------------------

npar=5
if [ $# -lt ${npar} ] 
then
    echo "Usage: submit.sh [njobs] [nevents] [cfgfile] [jobName] [runDir]"    
    echo -e "\tnjobs = number of jobs to run "
    echo -e "\tnevents = number of events per job "
    echo -e "\tcfgfile = CMSSW configuration file "
    echo -e "\tjobName = job name used for log files "
    echo -e "\trunDir = directory for output root files \n"
    exit
fi

njobs=${1}
nevts=${2}
cfg=${3}
jobName=${4}
runDir=${5}

echo
echo " Submitting: " ${njobs} "jobs, " ${nevts} " events per job"
echo " Configuration file: " ${cfg} 
echo " Job identifier: " ${jobName} 
echo " Output directory: " ${runDir} 
echo 

export WORKDIR=${PWD}
export WORKLOGS=${WORKDIR}/Skimlogs
if [ ! -e ${WORKLOGS} ] 
then
  mkdir ${WORKLOGS}
fi


jdlfile=condor.jdl
condorScript=${PWD}/condor.sh
jobScript=${PWD}/${3}

## create the jdl file
  makeJDL
## create the condor script
  makeCondor

/opt/condor/bin/condor_submit ${jdlfile}
