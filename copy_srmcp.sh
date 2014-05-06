#!/bin/bash

#MINB=(15 20 30 50  80 120 170 230 300 380 470)
#MAXB=(20 30 50 80 120 170 230 300 380 470 600)
#NBINS=8  # max=11


MINB=(50 300)
MAXB=(80 380)
NBINS=1  # max=9


((ibin=0))
# Double parentheses permit space when setting a variable, as in C.

while (( ibin < NBINS ))
do
  #INFILE=srm://srm.cern.ch:8443//srm/managerv1?SFN=/castor/cern.ch/user/a/apana/160pre4/HLToutput_RelVal151QCD_pt_${MINB[ibin]}_${MAXB[ibin]}_dijet.root
  #OUTFILE=srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/apana/HLT/160pre4/HLToutput_RelVal151QCD_pt_${MINB[ibin]}_${MAXB[ibin]}_dijet.root

  INFILE=srm://srm.cern.ch:8443//srm/managerv1?SFN=/castor/cern.ch/cms/store/RelVal/2007/6/23/RelVal-RelVal145QCD_pt50_80-1182605420/0008/C61E69E9-2B23-DC11-B0C2-00304881AEAE.root
  OUTFILE=srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/apana/RelVal145QCD_pt50_80.root


  echo $INFILE
  echo $OUTFILE
  echo ""

  srmcp -debug $INFILE $OUTFILE
  ((ibin += 1))   # let "ibin+=1"
done
