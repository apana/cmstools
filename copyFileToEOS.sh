#!/bin/bash


# EXEC=srmcp
EXEC="lcg-cp -b -D srmv2"

EOS="/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select"

## subDir=251718_ExpressFEVT
subDir=251781_NanoDST


## inFiles=``
## FILENAME=SimL1Emulator_Stage1_PP_1_1_rTd.root

inPREFIX=file:///$PWD  ## LOCAL
## inPREFIX=srm://cmseos.fnal.gov:8443/srm/v2/server?SFN=   ## FNAL
## inDIR=/eos/uscms/store/user/lpctrig/apana
## inPREFIX=srm://srm-eoscms.cern.ch:8443/srm/v2/server?SFN=   ## CERN
## inDIR=/eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/Data/Collisions/${subDir}
inDIR=XXX  ## use XXX if file is in current directory

## FNAL
outPREFIX=srm://cmseos.fnal.gov:8443/srm/v2/server?SFN=
outDIR=/eos/uscms/store/user/lpctrig/apana/Collisions2015/${subDir}

## CERN
## outPREFIX=srm://srm-eoscms.cern.ch:8443/srm/v2/server?SFN=
## outDIR=/eos/cms/store/caf/user/apana/L1Tutorial/Neutrino/results

for FILENAME in L1Tree_NanoDST_r251781.root;
## for FILENAME in `$EOS ls /eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/Data/Collisions/${subDir}`;

#  RelValTTbar_13_PU25ns_RAWplusRECO_2_1_bq4.root RelValTTbar_13_PU25ns_RAWplusRECO_3_1_Z1v.root RelValTTbar_13_PU25ns_RAWplusRECO_4_1_KTB.root RelValTTbar_13_PU25ns_RAWplusRECO_5_1_gFl.root RelValTTbar_13_PU25ns_RAWplusRECO_6_1_dv4.root RelValTTbar_13_PU25ns_RAWplusRECO_7_1_eBe.root RelValTTbar_13_PU25ns_RAWplusRECO_8_1_ATz.root RelValTTbar_13_PU25ns_RAWplusRECO_9_1_teD.root RelValTTbar_13_PU25ns_RAWplusRECO_10_1_WCN.root;
do

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
done


