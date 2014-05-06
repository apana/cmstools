#!/bin/bash


EXEC="srmcp -2 -debug"


## FILENAME=L1Tree_tst.root
FILENAME=262AA156-744A-E311-9829-002618943945.root

inPREFIX=file:///$PWD  ## LOCAL
## inPREFIX=srm://cmseos.fnal.gov:8443/srm/v2/server?SFN=   ## FNAL
## inPREFIX=srm://srm-eoscms.cern.ch:8443/srm/v2/server?SFN=   ## CERN
inDIR=XXX  ## use XXX if file is in current directory

## FNAL
## outPREFIX=srm://cmseos.fnal.gov:8443/srm/v2/server?SFN=
##  outDIR=/eos/uscms/store/user/lpctrig/apana/v4_62X_40PU_25bx_ReEmul2015

## CERN
outPREFIX=srm://srm-eoscms.cern.ch:8443/srm/v2/server?SFN=
outDIR=/eos/cms/store/group/comm_trigger/L1Trigger/apana

outFILE=$outPREFIX/$outDIR/$FILENAME

## if [[ $inPREFIX = file:///* ]]
if [[ $inDIR = *XXX* ]]
then
    echo -e "\n\tCopying local File\n"
    inFILE=$inPREFIX/$FILENAME
else
    echo -e "\n\tCopying remote File\n"
    inFILE=$inPREFIX/$inDIR/$FILENAME
fi

echo $EXEC $inFILE $outFILE
$EXEC $inFILE $outFILE
echo -e "\n\tDone\n"


