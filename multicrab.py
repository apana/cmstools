from WMCore.Configuration import Configuration
import datetime,sys,os

config = Configuration()

dryRun=False
RunOnMC = True
useJSON = True
WriteToCERN = True
## WriteToCERN = False

workflow='noRECO'
## workflow='wRECO'
## workflow='l1ACCEPT'

era=2016  ##   switch to 2015 to run on 2015 data
## era=2015

useParent=False
Nunits=5
NJOBS=-1  # used to limit total numbers of events processed. -1 == all events
if era==2015:
  JSON='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Reprocessing/Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON.txt'
else:
  JSON='Cert_271036-277933_13TeV_PromptReco_Collisions16_JSON.txt'

if workflow == 'noRECO':
  pSet = 'l1Ntuple_RAW.py'
  if era==2015: 'l1Ntuple2015reEmul_RAW2DIGI.py'
  ## JOBID = 'Collision2016-noRECO-l1t-integration-v89p20'
  ## JOBID = 'Collision2016-noRECO-l1t-v89p20'
  ## if RunOnMC: pSet = 'l1Ntuple_RAW_MC.py'
  if RunOnMC: pSet = 'l1Ntuple_RAW__HCALTP_MC.py'
  JOBID = 'Collision2016-noRECO-l1t-integration-v89p20_simHCALTP'
elif workflow == 'wRECO':
  pSet = 'l1Ntuple_RAW_wRECO.py'
  ## if RunOnMC: pSet = 'l1Ntuple_RAW_wRECO_MC.py'
  ## JOBID = 'Collision2016-wRECO-l1t-integration-v89p20'
  if RunOnMC: pSet = 'l1Ntuple_RAW_wRECO__HCALTP_MC.py'
  JOBID = 'Collision2016-wRECO-l1t-integration-v89p20_simHCALTP'
elif workflow == 'l1ACCEPT':
  pSet = 'l1Ntuple_L1Accept.py'
  JOBID = 'Collision2016-l1ACCEPT-l1t-integration-v89p20'
else:
  print "Bad Workflow"
  sys.exit(1)

#################################


## useJSON=False ## set to True for 2015 runs (or 2016 runs already certified)
## ## useJSON=True
## ## JSON='run274314.json'
## Nunits=4
## logbase="RunZB"
## myJobs={
## ##   "285090" + "_PAMinimumBias1":["/PAMinimumBias1/PARun2016B-v1/RAW",Nunits,285090],\
## ##   "285090" + "_PAMinimumBias2":["/PAMinimumBias2/PARun2016B-v1/RAW",Nunits,285090],\
## ##   "285090" + "_PAMinimumBias3":["/PAMinimumBias3/PARun2016B-v1/RAW",Nunits,285090],\
## ##   "285090" + "_PAMinimumBias4":["/PAMinimumBias4/PARun2016B-v1/RAW",Nunits,285090],\
## ##   "285090" + "_PAMinimumBias5":["/PAMinimumBias5/PARun2016B-v1/RAW",Nunits,285090],\
## ##   "285090" + "_PAMinimumBias6":["/PAMinimumBias6/PARun2016B-v1/RAW",Nunits,285090],\
## ##   "285090" + "_PAMinimumBias7":["/PAMinimumBias7/PARun2016B-v1/RAW",Nunits,285090],\
## ##   "285090" + "_PAMinimumBias8":["/PAMinimumBias8/PARun2016B-v1/RAW",Nunits,285090],\
## ##   "285216" + "_PAMinimumBias1":["/PAMinimumBias1/PARun2016B-v1/RAW",Nunits,285216],\
## ##   "285216" + "_PAMinimumBias2":["/PAMinimumBias2/PARun2016B-v1/RAW",Nunits,285216],\
## ##   "285216" + "_PAMinimumBias3":["/PAMinimumBias3/PARun2016B-v1/RAW",Nunits,285216],\
## ##   "285216" + "_PAMinimumBias4":["/PAMinimumBias4/PARun2016B-v1/RAW",Nunits,285216],\
## ##   "285216" + "_PAMinimumBias5":["/PAMinimumBias5/PARun2016B-v1/RAW",Nunits,285216],\
## ##   "285216" + "_PAMinimumBias6":["/PAMinimumBias6/PARun2016B-v1/RAW",Nunits,285216],\
## ##   "285216" + "_PAMinimumBias7":["/PAMinimumBias7/PARun2016B-v1/RAW",Nunits,285216],\
## ##   "285216" + "_PAMinimumBias8":["/PAMinimumBias8/PARun2016B-v1/RAW",Nunits,285216],\
## }

################################

logbase="RunMC_RAW"
Nunits=10
## NJOBS=100  ## should give ~5.5 million events for WJets sample; 5500 evts/file
## NJOBS=250  ## should give ~5. million events for DY sample; 2000 evts/file
## NJOBS=230  ## should give ~5.1 million events for TT sample; 2200 evts/file
## useParent=True
useParent=False
myJobs={
  ## "SingleMu_Pt1To1000"   : ["/SingleMu_Pt1To1000_FlatRandomOneOverPt/RunIISpring16DR80-NoPURAW_NZS_withHLT_80X_mcRun2_asymptotic_v14-v1/GEN-SIM-RAW",Nunits,1],\
  "VBF_HToInvisible_M125"   : ["/VBF_HToInvisible_M125_13TeV_powheg_pythia8/RunIISummer16DR80-FlatPU28to62HcalNZSRAW_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/GEN-SIM-RAW",Nunits,1],\
}


## ###############################
## logbase="RunMC_RECO"
## Nunits=10
## ## NJOBS=XXX  WJets not available jet for Summer16
## ## NJOBS=200  ## DY has ~20M events, 8060 files, 2500 evts/file;  use njobs=200 for ~5million
## ## NJOBS=213  ## TT has ~10M events, 4261 files, 2350 evts/file;  use njobs=213 ~5 million events
## ## NJOBS=200   ## SingleNeutrino had ~10 million events.  Don't specify NJOBS
## ## useParent=True
## useParent=False
## myJobs={# "SingleNeutrino_25nsPU10"   : ["/SingleNeutrino/RunIIFall15DR76-25nsPUfixed10NzshcalRaw_76X_mcRun2_asymptotic_v12-v1/AODSIM",Nunits,1],\
##         # "SingleNeutrino_25nsPU20"   : ["/SingleNeutrino/RunIIFall15DR76-25nsPUfixed20NzshcalRaw_76X_mcRun2_asymptotic_v12-v1/AODSIM",Nunits,1],\
##         # "SingleNeutrino_25nsPU30"   : ["/SingleNeutrino/RunIIFall15DR76-25nsPUfixed30NzshcalRaw_76X_mcRun2_asymptotic_v12-v1/AODSIM",Nunits,1],\
##         #"SingleNeutrino_25nsPU40"   : ["/SingleNeutrino/RunIIFall15DR76-25nsPUfixed40NzshcalRaw_76X_mcRun2_asymptotic_v12-v1/AODSIM",Nunits,1],\
##         #"SingleNeutrino_25nsPU50"   : ["/SingleNeutrino/RunIIFall15DR76-25nsPUfixed50NzshcalRaw_76X_mcRun2_asymptotic_v12-v1/AODSIM",Nunits,1],\
##   ## "RelValSingleElectronPt1000_UP15"   : ["/RelValSingleElectronPt1000_UP15/CMSSW_8_0_10-80X_mcRun2_asymptotic_v14_reHLT-v1/AODSIM",Nunits,1],\
##   ## "SingleNeutrino_FlatPU0to70"   : ["/SingleNeutrino/RunIISummer16DR80-PUFlat0to70HcalNZSRAWAODSIM_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/RAWAODSIM",Nunits,1],\
##   ## "WJetsToLNu": ["/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16DR80-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_v3_ext1-v1/RAWAODSIM",Nunits,1],\
##   ## "DYJetsToLL_M50"   : ["/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80-FlatPU28to62HcalNZSRAWAODSIM_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/RAWAODSIM",Nunits,1],\
##   "VBF_HToInvisible_M125"   : ["/VBF_HToInvisible_M125_13TeV_powheg_pythia8/RunIISpring16DR80-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_v3-v1/RAWAODSIM",Nunits,1],\
##   ## "TT_TuneCUETP8M2T4"   : ["/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16DR80-FlatPU28to62HcalNZSRAWAODSIM_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/RAWAODSIM",Nunits,1],\
## }


#################################

## useJSON=False
## logbase="Run2016B_Express"
## myJobs={
##   "274094" + "_ExpressPhysics":["/ExpressPhysics/Run2016B-Express-v2/FEVT",Nunits, 274094]
## }


###########

## useJSON=True
## logbase="Run2016_Skims"
## Nunits=20
## useParent=False
## myJobs={
##   ##"DoubleEG_ZEle"    : ["/DoubleEG/Run2016B-ZElectron-PromptReco-v2/RAW-RECO", Nunits, -1],\
##   ## "MuonEG_TopMuEg"   : ["/MuonEG/Run2016B-TopMuEG-PromptReco-v1/RAW-RECO", Nunits, -1],\
##   ## "SingleMuon_MuTau" : ["/SingleMuon/Run2016B-MuTau-PromptReco-v2/RAW-RECO", Nunits, -1],\
##   "SingleMuon_ZMu"   : ["/SingleMuon/Run2016E-ZMu-PromptReco-v2/RAW-RECO", Nunits, -1],\
## }

######

## ## useJSON=True
## useJSON=False
## ## logbase="Run2016_PromptReco"
## ## logbase="Run2016_PromptReco_wRECO"
## logbase="Run2016_PromptReco_" + workflow
## Nunits=2
## useParent=True
## myJobs={
##   ## "283171" + "_Commissioning":["/Commissioning/Run2016H-PromptReco-v2/AOD",Nunits,283171],\
## }

## useJSON=False ## set to True for 2015 runs (or 2016 runs already certified)
## ## useJSON=True
## ## JSON='run274314.json'
## Nunits=5
## logbase="RunZB"
## myJobs={
##   ## "279975" + "_ParkingZeroBias0":["/ParkingZeroBias0/Run2016G-v1/RAW",Nunits,279975],\
##   ## "279975" + "_ParkingZeroBias1":["/ParkingZeroBias1/Run2016G-v1/RAW",Nunits,279975],\
##   ## "279975" + "_ParkingZeroBias2":["/ParkingZeroBias2/Run2016G-v1/RAW",Nunits,279975],\
##   ## "279975" + "_ParkingZeroBias3":["/ParkingZeroBias3/Run2016G-v1/RAW",Nunits,279975],\
##   ## "279975" + "_ParkingZeroBias4":["/ParkingZeroBias4/Run2016G-v1/RAW",Nunits,279975],\
##   ## "279975" + "_ParkingZeroBias5":["/ParkingZeroBias5/Run2016G-v1/RAW",Nunits,279975],\
##   ## "279975" + "_ParkingZeroBias6":["/ParkingZeroBias6/Run2016G-v1/RAW",Nunits,279975],\
##   ## "279975" + "_ParkingZeroBias7":["/ParkingZeroBias7/Run2016G-v1/RAW",Nunits,279975],\
##   "279975" + "_ZeroBias":["/ZeroBias/Run2016G-v1/RAW",Nunits,279975],\
##   ## "281639" + "_ZeroBias":["/ZeroBias/Run2016H-v1/RAW",Nunits,281639],\
## }

## useJSON=False ## set to True for 2015 runs (or 2016 runs already certified)
## ## useJSON=True
## ## JSON='run274314.json'
## Nunits=2
## useParent=True
## logbase="RunZBBunchTrains_wRECO"
## myJobs={
##   "283171" + "_ZeroBiasBunchTrains0":["/ZeroBiasBunchTrains0/Run2016H-PromptReco-v2/AOD",Nunits,283171],\
##   "283171" + "_ZeroBiasBunchTrains1":["/ZeroBiasBunchTrains1/Run2016H-PromptReco-v2/AOD",Nunits,283171],\
##   "283171" + "_ZeroBiasBunchTrains2":["/ZeroBiasBunchTrains2/Run2016H-PromptReco-v2/AOD",Nunits,283171],\
##   "283171" + "_ZeroBiasBunchTrains3":["/ZeroBiasBunchTrains3/Run2016H-PromptReco-v2/AOD",Nunits,283171],\
##   "283171" + "_ZeroBiasBunchTrains4":["/ZeroBiasBunchTrains4/Run2016H-PromptReco-v2/AOD",Nunits,283171],\
##   "283171" + "_ZeroBiasBunchTrains5":["/ZeroBiasBunchTrains5/Run2016H-PromptReco-v2/AOD",Nunits,283171],\
## }

######################################


## useJSON=False ## set to True for 2015 runs (or 2016 runs already certified)
## ## useJSON=True
## ## JSON='run274314.json'
## Nunits=2
## useParent=True
## logbase="RunZBIsolatedBunch_wRECO"
## myJobs={
##   "283171" + "_ZeroBiasIsolatedBunch0":["/ZeroBiasIsolatedBunch0/Run2016H-PromptReco-v2/AOD",Nunits,283171],\
##   "283171" + "_ZeroBiasIsolatedBunch1":["/ZeroBiasIsolatedBunch1/Run2016H-PromptReco-v2/AOD",Nunits,283171],\
##   "283171" + "_ZeroBiasIsolatedBunch2":["/ZeroBiasIsolatedBunch2/Run2016H-PromptReco-v2/AOD",Nunits,283171],\
##   "283171" + "_ZeroBiasIsolatedBunch3":["/ZeroBiasIsolatedBunch3/Run2016H-PromptReco-v2/AOD",Nunits,283171],\
##   "283171" + "_ZeroBiasIsolatedBunch4":["/ZeroBiasIsolatedBunch4/Run2016H-PromptReco-v2/AOD",Nunits,283171],\
##   "283171" + "_ZeroBiasIsolatedBunch5":["/ZeroBiasIsolatedBunch5/Run2016H-PromptReco-v2/AOD",Nunits,283171],\
## }

######################################################################################

## ## useJSON=True
## useJSON=False
## ## logbase="Run2016_PromptReco"
## ## logbase="Run2016_PromptReco_wRECO"
## logbase="Run2016_PromptReco_" + workflow
## Nunits=2
## useParent=True
## myJobs={
## ##  "285090" + "_SingleMuon":["/PASingleMuon/PARun2016B-PromptReco-v1/AOD",Nunits,285090],\
## ##  "285091" + "_SingleMuon":["/PASingleMuon/PARun2016B-PromptReco-v1/AOD",Nunits,285091],\
## ##  "285216" + "_SingleMuon":["/PASingleMuon/PARun2016B-PromptReco-v1/AOD",Nunits,285216],\
## ##  "285244" + "_SingleMuon":["/PASingleMuon/PARun2016B-PromptReco-v1/AOD",Nunits,285244],\
## ##  "285368" + "_SingleMuon":["/PASingleMuon/PARun2016B-PromptReco-v1/AOD",Nunits,285368],\
## ##  "285369" + "_SingleMuon":["/PASingleMuon/PARun2016B-PromptReco-v1/AOD",Nunits,285369],\
## ##  "285371" + "_SingleMuon":["/PASingleMuon/PARun2016B-PromptReco-v1/AOD",Nunits,285371],\
## ##  "285374" + "_SingleMuon":["/PASingleMuon/PARun2016B-PromptReco-v1/AOD",Nunits,285374],\
## ##  "285383" + "_SingleMuon":["/PASingleMuon/PARun2016B-PromptReco-v1/AOD",Nunits,285383],\
## ##  "285479" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285479],\
## ##  "285480" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285480],\
## ##  "285505" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285505],\
## ##  "285517" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285517],\
## ##  "285530" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285530],\
## ##  "285537" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285537],\
## ##  "285538" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285538],\
## ##  "285539" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285539],\
## ##  "285549" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285549],\
## ##  "285684" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285684],\
## ##  "285718" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285718],\
## ##  "285726" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285726],\
## ##  "285749" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285749],\
## ##  "285750" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285750],\
## ##  "285759" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285759],\
## ##  "285952" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285952],\
## ##  "285975" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285975],\
## ##  "285993" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285993],\
## ##  "285994" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285994],\
## ##  "285995" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285995],\
## ##  "286009" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286009],\
##   ## "285953" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285953],\
##   ## "285954" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285954],\
##   ## "285955" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285955],\
##   ## "285956" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,285956],\
##   ## "286010" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286010],\
##   ## "286023" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286023],\
##   ## "286031" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286031],\
##   ## "286033" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286033],\
##   ## "286034" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286034],\
##   ## "286051" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286051],\
##   ## "286054" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286054],\
##   ## "286069" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286069],\
##   ## "286070" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286070],\
##   ## "286178" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286178],\
##   ## "286200" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286200],\
##   ## "286201" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286201],\
##   ## "286288" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286288],\
##   ## "286301" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286301],\
##   ## "286302" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286302],\
##   ## "286309" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286309],\
##   ## "286314" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286314],\
##   ## "286327" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286327],\
##   ## "286329" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286329],\
##   ## "286365" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286365],\
##   ## "286420" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286420],\
##   ## "286422" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286422],\
##   ## "286424" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286424],\
##   ## "286425" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286425],\
##   ## "286441" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286441],\
##   ## "286442" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286442],\
##   ## "286450" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286450],\
##   ## "286471" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286471],\
##   ## "286496" + "_SingleMuon":["/PASingleMuon/PARun2016C-PromptReco-v1/AOD",Nunits,286496],\
## ##  "286513" + "_SingleMuon":["/PASingleMuon/PARun2016D-PromptReco-v1/AOD",Nunits,286513],\
## ##  "286514" + "_SingleMuon":["/PASingleMuon/PARun2016D-PromptReco-v1/AOD",Nunits,286514],\
## ##  "286516" + "_SingleMuon":["/PASingleMuon/PARun2016D-PromptReco-v1/AOD",Nunits,286516],\
## ##  "286517" + "_SingleMuon":["/PASingleMuon/PARun2016D-PromptReco-v1/AOD",Nunits,286517],\
## ##  "286518" + "_SingleMuon":["/PASingleMuon/PARun2016D-PromptReco-v1/AOD",Nunits,286518],\
## ##  "286519" + "_SingleMuon":["/PASingleMuon/PARun2016D-PromptReco-v1/AOD",Nunits,286519],\
## ##  "286520" + "_SingleMuon":["/PASingleMuon/PARun2016D-PromptReco-v1/AOD",Nunits,286520],\
## ##  "285090" + "_EGJet1":["/PAEGJet1/PARun2016B-PromptReco-v1/AOD",Nunits,285090],\
## ##  "285091" + "_EGJet1":["/PAEGJet1/PARun2016B-PromptReco-v1/AOD",Nunits,285091],\
## ##  "285216" + "_EGJet1":["/PAEGJet1/PARun2016B-PromptReco-v1/AOD",Nunits,285216],\
## ##  "285244" + "_EGJet1":["/PAEGJet1/PARun2016B-PromptReco-v1/AOD",Nunits,285244],\
## ##  "285368" + "_EGJet1":["/PAEGJet1/PARun2016B-PromptReco-v1/AOD",Nunits,285368],\
## ##  "285369" + "_EGJet1":["/PAEGJet1/PARun2016B-PromptReco-v1/AOD",Nunits,285369],\
## ##  "285371" + "_EGJet1":["/PAEGJet1/PARun2016B-PromptReco-v1/AOD",Nunits,285371],\
## ##  "285374" + "_EGJet1":["/PAEGJet1/PARun2016B-PromptReco-v1/AOD",Nunits,285374],\
## ##  "285383" + "_EGJet1":["/PAEGJet1/PARun2016B-PromptReco-v1/AOD",Nunits,285383],\
##   "279975" + "_SingleMuon":["/SingleMuon/Run2016G-PromptReco-v1/AOD",Nunits,279975],\
## }

################################

## useJSON=False
## logbase="RunL1Accept"
## myJobs={
##   "273450" + "_L1Accept":["/L1Accept/Run2016B-v2/RAW",Nunits,273450]
## }

###########

## ## useJSON=True
## useJSON=False
## logbase="Run2016_Skims"
## Nunits=20
## useParent=False
## myJobs={
##   ## "DoubleEG_ZEle"    : ["/DoubleEG/Run2016B-ZElectron-PromptReco-v2/RAW-RECO", Nunits, -1],\
##   ## "MuonEG_TopMuEg"   : ["/MuonEG/Run2016B-TopMuEG-PromptReco-v1/RAW-RECO", Nunits, -1],\
##   ## "SingleMuon_MuTau" : ["/SingleMuon/Run2016B-MuTau-PromptReco-v2/RAW-RECO", Nunits, -1],\
##   ## "SingleMuon_ZMu"   : ["/SingleMuon/Run2016B-ZMu-PromptReco-v2/RAW-RECO", Nunits, -1],\
##   "SingleMuon_ZMu"   : ["/SingleMuon/Run2016G-ZMu-23Sep2016-v1/RAW-RECO", Nunits, -1],\
##   ## "279975_SingleMuon_ZMu"   : ["/SingleMuon/Run2016G-ZMu-23Sep2016-v1/RAW-RECO", Nunits, 279975],\
## }


####################################

splitting   = 'LumiBased'
theSample = "Data"
if RunOnMC :
    splitting   = 'FileBased'
    theSample = "MC"

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
#config.General.workArea = logbase + '_' + str(datetime.date.today())
config.General.workArea = logbase + '_' + str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

config.section_('JobType')
config.JobType.psetName = pSet
config.JobType.pluginName = 'Analysis'
config.JobType.maxMemoryMB = 2500
config.JobType.outputFiles = ['L1Ntuple.root']
## config.JobType.inputFiles = ['../../data/Jet_Stage1_2015_v2.txt']

config.section_('Data')

## ccla
# Set to True to allow the jobs to run at any site. Suggested by Lucia if we want to runon data at CERN pre-publication on DAS.
config.Data.ignoreLocality = True

config.Data.inputDBS = 'global'
config.Data.splitting = splitting
config.Data.unitsPerJob = 10
## config.Data.totalUnits = 1
config.Data.useParent = useParent
config.Data.outLFNDirBase = output
config.Data.runRange = ''

if (RunOnMC): useJSON=False

if useJSON :
  print "------------  USING JSON  -------------"
  config.Data.lumiMask = JSON

config.section_('Site')
config.Site.storageSite = StorageSite

## ccla
#config.Site.whitelist = ["T2_CH*"]

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

    if not os.path.exists(pSet):
      print "\nConfiguration file ",pSet,"does not exist.  Aborting..."
      sys.exit(1)

    if useJSON and (not os.path.exists(JSON)):
      print "\nJSON file ",JSON,"does not exist.  Aborting..."
      sys.exit(1)

    print "\n"
    print "About to submit a multicrab job for the following workflow:\n"
    print "\tConfig file:\t",pSet,"\tWorkflow:\t",workflow
    print "\tData or MC:\t",theSample
    print "\tStorage site:\t",StorageSite
    print "\tOutput dir:\t",output,"\n"

    for job in myJobs.keys():
        jobPars=myJobs[job]
        print "\t",job, jobPars
    print "\n"

    cont=raw_input('Press return to continue. Any other key to abort...\n')
    if 0 < len(cont):
        sys.exit(1)

    i=0
    for job in myJobs.keys():

        jobPars=myJobs[job]
        i=i+1
        print "\nSubmitting job ",i," of ",len(myJobs.keys()),":\t",job, jobPars

        config.General.requestName = JOBID + "__" + job
        config.Data.inputDataset = jobPars[0]
        config.Data.unitsPerJob = jobPars[1]
        if NJOBS>0 :
          config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

        if jobPars[2] != -1:
            config.Data.runRange = str(jobPars[2])

        print config
        if not dryRun:
          p = Process(target=submit, args=(config,))
          p.start()
          p.join()
