from WMCore.Configuration import Configuration
import datetime

config = Configuration()

JOBID   = 'l1-tsg-v3'
RunOnMC = False
WriteToCERN = True

pSet = 'l1NtupleRECO_RAW2DIGI.py'
# pSet = 'l1NtupleRECO_RAW2DIGI_ht.py'
# pSet = 'l1NtupleStg1_RAW2DIGI.py'
useParent = False
## runid = '259626'  ## use '-1' for all runs
## runid = '259721'  ## use '-1' for all runs
## runid = '258440'  ## use '-1' for all runs
runid = '258448'  ## use '-1' for all runs

JSON='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Reprocessing/Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON.txt'

#################################

Nunits=5
useParent=True
logbase="Run" + runid

if int(runid)==258440 or int(runid)==258448:
    myJobs={runid + "_ZeroBias":["/ZeroBias/Run2015D-16Dec2015-v1/RECO",Nunits]
    }
else:
    myJobs={runid + "_ZeroBias1":["/ZeroBias1/Run2015D-16Dec2015-v1/RECO",Nunits],\
            runid + "_ZeroBias2":["/ZeroBias2/Run2015D-16Dec2015-v1/RECO",Nunits],\
            runid + "_ZeroBias3":["/ZeroBias3/Run2015D-16Dec2015-v1/RECO",Nunits],\
            runid + "_ZeroBias4":["/ZeroBias4/Run2015D-16Dec2015-v1/RECO",Nunits]
    }

#################################

## logbase="RECOskims"
## Nunits=200
## runid = '-1'  ## use '-1' for all runs
## myJobs={"DoubleEG_ZEle"   :["/DoubleEG/Run2015D-ZElectron-16Dec2015-v2/RAW-RECO",Nunits],\
##         ## "MuonEG_TopMuEg"  :["/MuonEG/Run2015D-TopMuEG-16Dec2015-v1/RAW-RECO"    ,Nunits],\
##         "SingleMuon_MuTau":["/SingleMuon/Run2015D-MuTau-16Dec2015-v1/RAW-RECO"  ,Nunits],\
##         "SingleMuon_ZMu"  :["/SingleMuon/Run2015D-ZMu-16Dec2015-v1/RAW-RECO"    ,Nunits],\
## }

#################################

## Nunits=20
## RunOnMC = True
## pSet='xxx'
## myJobs={"SingleNeutrino_25nsPU10"   : ["/SingleNeutrino/RunIIFall15DR76-25nsPUfixed10NzshcalRaw_76X_mcRun2_asymptotic_v12-v1/AODSIM",Nunits],\
##         #"SingleNeutrino_25nsPU20"   : ["/SingleNeutrino/RunIIFall15DR76-25nsPUfixed20NzshcalRaw_76X_mcRun2_asymptotic_v12-v1/AODSIM",Nunits],\
##         #"SingleNeutrino_25nsPU30"   : ["/SingleNeutrino/RunIIFall15DR76-25nsPUfixed30NzshcalRaw_76X_mcRun2_asymptotic_v12-v1/AODSIM",Nunits],\
##         #"SingleNeutrino_25nsPU40"   : ["/SingleNeutrino/RunIIFall15DR76-25nsPUfixed40NzshcalRaw_76X_mcRun2_asymptotic_v12-v1/AODSIM",Nunits],\
##         #"SingleNeutrino_25nsPU50"   : ["/SingleNeutrino/RunIIFall15DR76-25nsPUfixed50NzshcalRaw_76X_mcRun2_asymptotic_v12-v1/AODSIM",Nunits],\
## }

###
splitting   = 'LumiBased'
if RunOnMC :
    splitting   = 'FileBased'

if WriteToCERN:
    StorageSite = 'T2_CH_CERN'
    output      = '/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/' + JOBID 
else:
    StorageSite = 'T3_US_FNALLPC'    
    output      = '/store/group/lpctrig/apana/L1Menu_2016/Stage2/' + JOBID

#############################################
### common for all jobs  ####################
#############################################
config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.workArea = logbase + '_' + str(datetime.date.today())

config.section_('JobType')
config.JobType.psetName = pSet
config.JobType.pluginName = 'Analysis'
config.JobType.maxMemoryMB = 2500
config.JobType.outputFiles = ['L1Ntuple.root']
## config.JobType.inputFiles = ['../../data/Jet_Stage1_2015_v2.txt']

config.section_('Data')
config.Data.inputDBS = 'global'
config.Data.splitting = splitting
config.Data.unitsPerJob = 10
## config.Data.totalUnits = 1
config.Data.useParent = useParent
config.Data.outLFNDirBase = output
if not(RunOnMC) :
    config.Data.lumiMask = JSON
    if runid != '-1':
        config.Data.runRange = runid
    
config.section_('Site')
config.Site.storageSite = StorageSite

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException
    from multiprocessing import Process

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    for job in myJobs.keys():

        jobPars=myJobs[job]
        print job, jobPars        
        config.General.requestName = JOBID + "__" + job
        config.Data.inputDataset = jobPars[0]
        config.Data.unitsPerJob = jobPars[1]
        
        # print config
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()


