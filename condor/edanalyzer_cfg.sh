#!/bin/sh -f
#
#
#echo "Number of Arguments: $#"

Process=$1
nevts=$2
ptmin=$3
ptmax=$4

echo
echo ">>> Beginning cmsRun execution on `date`  <<<"
echo ">>> Number of events to process: $nevts <<<"
echo

#create config file
export WORKDIR=${PWD}
if [ -n "${CMS_PATH:-}" ]; then
  echo "CMSSW computing environment already setup"
else
#setup the environment
   echo "Setting up CMSSW computing environment"
   export PATH=/bin:/usr/bin:/usr/local/bin:/usr/krb5/bin:/usr/afsws/bin:/usr/krb5/bin/aklog:{$PATH}
   . /uscmst1/prod/sw/cms/shrc uaf
   export SCRAM_ARCH=`scramv1 arch`
fi

cd $WORKDIR
pwd
eval `scramv1 runtime -sh`

cd ${WORKDIR}
export CFG=runjob_${ptmin}_${ptmax_}${RANDOM}.cfg

if [ $_CONDOR_SCRATCH_DIR ]
then
  BSCRATCH=${_CONDOR_SCRATCH_DIR}
  /bin/cat /etc/redhat-release
  echo "Batch system: Condor"
  echo "SCRAM_ARCH:   "${SCRAM_ARCH}
  #let current=($1 + $2)
  #@ current = ($1 + $2)
  #echo "processing Run: " $current " with:  " $3 "events"
elif [ $FBS_SCRATCH ]
then
  BSCRATCH=$FBS_SCRATCH
  /bin/cat /etc/redhat-release
  echo "Batch system: FBSNG"
  echo "SCRAM_ARCH:   "${SCRAM_ARCH}
  #let current=(${FBS_PROC_NO} + $2 - 1)
  #@ current = (${FBS_PROC_NO} + $2 - 1)
  #echo "processing Run: "$current" with:  ", $3, "events"
else
    echo "Unknown Batch System"
    exit
fi

cat > $CFG <<EOF
process ANALYSIS  = {

    source = PoolSource {
	untracked vstring fileNames = {
	    "file:/uscmst1b_scratch/lpc1/cmsjtmet/apana/hlt/dev/CMSSW_1_3_0_pre5/src/run/jetmet_l1accepted_qcd_${ptmin}_${ptmax}_noPU_fromDigi.root"
	}
	untracked int32 maxEvents = ${nevts}
    }

   es_module = CaloGeometryBuilder {}

   #Geometry
   include "Geometry/CMSCommonData/data/cmsSimIdealGeometryXML.cfi"

   module l1analysisPE1 = HLTJetAnalyzer{
     string recjets = "iterativeCone5CaloJets"
     string genjets = "iterativeCone5GenJets"
     string recmet  = "met"
     string genmet  = "genMet"
     string hltobj  = "l1s1jetPE1"
     string calotowers = "towerMaker"
     InputTag l1collections= l1extraParticles
     PSet RunParameters =
     {
       string HistogramFile = "analysis_l1jetpe1_pt_${ptmin}_${ptmax}_l1extra.root"
       string HLTPath = "L11jetPE1"
       bool Monte = true
       bool Debug = false
       double EtaMin   = -5.0
       double EtaMax   = 5.0
     }
   }

    path p1 = {l1analysisPE1}
		
}		
EOF
cmsRun -p ${WORKDIR}/${CFG}
