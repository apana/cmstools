#!/usr/bin/python
#
import sys,string,math,os


WorkFlows=['RAW']
## WorkFlows=['l1Accept']
## WorkFlows=['reEmuSimTP']

addRECO=False
## addRECO=True

## DataTypes=["data"]
DataTypes=["mc"]
## DataTypes=["data","mc"]

## HeavyIon=True
HeavyIon=False

################### Common settings #######

ERA="Run2_2016"
if HeavyIon:
    ERA="Run2_2016_PA"
    
NEVT="100"
STEP="RAW2DIGI"

###########################################

GlobalTags_data={
    "RECO":["80X_dataRun2_Prompt_v14","XXX"],\
    "RAW":["80X_dataRun2_HLT_v12","80X_dataRun2_pA_HLT_v0"],\
    }

GlobalTags_MC={
    "RECO":["80X_mcRun2_asymptotic_2016_miniAODv2_v1","XXX"],\
    "RAW":["80X_mcRun2_asymptotic_2016_v3","XXX"],\
    ## "RAW":["80X_mcRun2_asymptotic_RealisticBS_25ns_13TeV2016_v1_mc","XXX"],\
    }

ExtraOptions=[]
## ExtraOptions=["L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloStage2Params_v3_2"]
## ExtraOptions=["L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloStage2Params_v2_2"]

if __name__ == '__main__':

    for workflow in WorkFlows:
        for DataOrMC in DataTypes:
            if DataOrMC == "data":
                INFILE="/store/data/Run2016G/ZeroBias/RAW/v1/000/279/975/00000/BECFAD0B-8672-E611-9652-02163E0119C7.root"
                if workflow == 'l1Accept':
                    INFILE="/store/data/Run2016H/L1Accept/RAW/v1/000/283/171/00000/1CBA2564-F391-E611-BC17-02163E014626.root"
                if addRECO:
                    INFILE="/store/data/Run2016F/SingleMuon/RAW-RECO/ZMu-PromptReco-v1/000/277/933/00000/12AB6E9A-2059-E611-85A8-FA163E3B8FC0.root"
                GlobalTags=GlobalTags_data
                endName=".py"
            else:
                ## INFILE="/store/mc/RunIISpring16DR80/TT_TuneCUETP8M1_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU20to70HcalNZSRAW_withHLT_80X_mcRun2_asymptotic_v14_ext3-v1/50000/CE22C0CB-9965-E611-9101-0025905C4262.root"
                INFILE="file:/afs/cern.ch/user/j/jalimena/public/Stage2DigiHlt80X/mchamp600/hist_0.root"
                GlobalTags=GlobalTags_MC
                endName="_MC.py"

            if addRECO:
                GT=GlobalTags["RECO"]
                CFG=workflow + "_wRECO"
            else:
                GT=GlobalTags["RAW"]
                CFG=workflow                

            GlobalTag=GT[0]
            if HeavyIon:
                GlobalTag=GT[1]

            theSTEP=STEP
            if workflow == 'l1Accept':
                theSTEP = "NONE"
                
            pSet="l1Ntuple_" + CFG + endName            
            driverOptions="l1Ntuple -s " + theSTEP + " --python_filename=" + pSet + \
                " -n " + NEVT + " --no_output --no_exec --era=" + ERA + " --" + DataOrMC + \
                " --conditions=" + GlobalTag + \
                " --filein=" + INFILE

            customOptions=[]
            if workflow == 'RAW':
                customOptions=["L1Trigger/Configuration/customiseReEmul.L1TReEmulFromRAW"]
                if addRECO:
                    customOptions.append("L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleAODRAWEMU")
                else:
                    customOptions.append("L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleRAWEMU")
            elif workflow == 'l1Accept':
                customOptions=["L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleRAW"]                
                if addRECO:
                    customOptions=["L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleAODRAW"]
                    
                if DataOrMC=="mc": continue
            elif workflow == 'reEmuSimTP':
                customOptions=["L1Trigger/Configuration/customiseReEmul.L1TReEmulFromRAWsimTP"]
                if addRECO:
                    customOptions.append("L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleAODRAWEMU")
                else:
                    customOptions.append("L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleRAWEMU")
            else:
                print "Bad Workflow"
                sys.exit(1)

            for extraOpt in ExtraOptions:
                customOptions.append(extraOpt)

            for custom in customOptions:
                driverOptions = driverOptions + " --customise=" + custom
                
            print workflow, DataOrMC, pSet, GlobalTag
            print driverOptions + "\n"
            os.system("cmsDriver.py " + driverOptions)

