#!/bin/bash
#
# script for copying files from CERN to Wisconsin dCache file system
#

# EXEC="lcg-cp --verbose -b -D srmv2"
# EXEC="lcg-cp -b --vo cms -D srmv2 "

# EXEC="lcg-cp -b --verbose -D srmv2"
EXEC="lcg-cp -D srmv2"

PREFIX=srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=
# INDIR=/11/store/user/apana/Skims/AODSkim_HLTJet240
# INDIR=/11/store/user/apana/QCD/JetPruning/HLTJet140U_v3
INDIR=/11/store/user/apana/QCD/JetPruning/HLTJet240

# OUTDIR=srm://srm-cms.cern.ch:8443/srm/managerv2?SFN=/castor/cern.ch/user/a/apana/QCD2011/JetPruning/HLTJet140U_v3
OUTDIR=srm://srm-cms.cern.ch:8443/srm/managerv2?SFN=/castor/cern.ch/user/a/apana/QCD2011/JetPruning/HLTJet240

#for filename in HLTTime-Minbias_default_12_reco.root \
#    HLTTime-Minbias_regional_12.root \
#    HLTTime-Minbias_regional_12_reco.root

# for filename in pMuX_l1Skim_111_99.root

# for filename in `ls /uscmst1b_scratch/lpc1/cmsjtmet/apana/hlt/l1skims`
for filename in `ls ${PNFS}${INDIR}`
# for filename in `cat ~/missing2.txt`
do


  # INFILE='"'${PREFIX}${INDIR}/${filename}'"'
  # OUTFILE='"'${OUTDIR}/${filename}'"'

  INFILE=${PREFIX}${INDIR}/${filename}
  OUTFILE=${OUTDIR}/${filename}

  echo $EXEC $INFILE $OUTFILE
  $EXEC $INFILE $OUTFILE
  echo " " 
done
