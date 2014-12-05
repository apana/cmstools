#!/bin/bash

echo "XXX"
menu=/dev/CMSSW_4_2_0/GRun/V16
# menu=/dev/CMSSW_4_2_0/GRun/V13
globalTag=GR_H_V16::All
ProcessName=HLTGRun
CfgName=offline_xxx.py

DataOrMC=MC

if [ $DataOrMC == "MC" ]
then
    hltGetConfiguration ${menu} --full --offline --mc --unprescale --globaltag ${globalTag} --process ${ProcessName} > ${CfgName}
else
    hltGetConfiguration ${menu} --full --offline --data --unprescale --globaltag ${globalTag} --process ${ProcessName} > ${CfgName}
fi
