#!/bin/bash
#
# script for copying files from to FNAL dCache file system
#

EXEC="srmcp -debug -2"

PREFIX=file://
#INDIR=/uscmst1b_scratch/lpc1/lpctrig/apana/data/OpenHLT
#OUTDIR=srm://cmssrm.fnal.gov:8443/srm/managerv2?SFN=/resilient/apana/redoHLT

# INDIR=/uscms_data/d2/kkousour/7TeV/DijetMassAnalysis
# INDIR=/uscms_data/d2/apana/Higgs/Analysis/CMSSW_5_2_5/src
INDIR=/uscmst1b_scratch/lpc1/cmsjtmet/apana
OUTDIR=srm://cmssrm.fnal.gov:8443/srm/managerv2?SFN=/11/store/user/lpchbb/apana/Step1V33_Step2_V2

# individual or handful of files
#for filename in HLTTime-Minbias_default_12_reco.root \
#    HLTTime-Minbias_regional_12.root \
#    HLTTime-Minbias_regional_12_reco.root

for filename in DiJetPt_DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball_Skim_bjets.root

# directories
# for filename in `ls /uscmst1b_scratch/lpc1/cmsjtmet/apana/hlt/l1skims`
# for filename in `ls ${INDIR}`
do

  
  INFILE=${PREFIX}/${INDIR}/${filename}
  OUTFILE=${OUTDIR}/${filename}

  echo $INFILE
  echo $OUTFILE
  echo ""

  $EXEC $INFILE $OUTFILE

done
