#!/bin/bash

nargs=$#


# file=$1
# dir=$2
# cd data

# for file in DiJetPt_DoubleElectron_Run2012C-PromptReco-v2_HBB_EDMNtupleV42_ProcV1_Vpt95Skim.root
for file in DiJetPt_DYJetsToLL_PtZ-100_TuneZ2star_8TeV-madgraph_lheVpt-100To180.root
# for file in `ls *.root`

do

    if [ ! -f "$file" ]
    then
	echo "File \"$file\" does not exist."
	exit $E_NOFILE
    fi

    infile=file:///$PWD/$file
    # outfile=srm://cmssrm.fnal.gov:8443/srm/managerv2?SFN=/11/store/user/lpchbb/apana/dev/Skim_pT300/Step1/$file
    # outfile=srm://cmssrm.fnal.gov:8443/srm/managerv2?SFN=/11/store/user/lpchbb/apana/Ntuple_Step1V42_Step2Tag_EDMV42_Step2_V4a_Data/Vpt95Skim/$file
    outfile=srm://cmssrm.fnal.gov:8443/srm/managerv2?SFN=/11/store/user/lpchbb/apana/Ntuple_Step1V42_Step2Tag_EDMV42_Step2_V4a_MC/$file

    echo $infile 
    echo $outfile
    lcg-cp -b -D srmv2 $infile $outfile
done




