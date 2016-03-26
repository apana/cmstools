from ROOT import gROOT, gStyle, gSystem, TCanvas, TF1, TFile, TH1F, TColor, TLine, TLegend, TLatex, SetOwnership, TChain
import sys,string,math,os,ROOT, datetime

from PhysicsTools.PythonAnalysis import *
from ROOT import *
gSystem.Load("libFWCoreFWLite.so")
AutoLibraryLoader.enable()

sys.path.append(os.path.join(os.environ.get("HOME"),'rootmacros'))
from myPyRootMacros import prepPlot, SetStyle, GetHist, PrepLegend, DrawText, prep1by2Plot, ResetAxisAndLabelSizes
#===============================================================

## ScaleToNumberOfEntries=False
ScaleToNumberOfEntries=True
Rebin=-1  ## used to overide default rebin value

PrintPlot=False
## PrintPlot=True
outdir="compNT_" + str(datetime.date.today())  ## output directory for plots

## Dists=["et","eta","phi"]
Dists=["et"]
## L1Objs=["Jet","CenJet","Muon","ETT","HTT","ETM","HTM","EG","IsoEG","NonIsoEG","Tau","IsoTau","NonIsoTau"]
L1Objs=["Muon","EG","IsoEG","NonIsoEG","Tau","IsoTau","NonIsoTau","ETT","HTT","ETM","HTM",]

## Dists=["et"]
## L1Objs=["HTT","ETT","ETM","HTM"]

## Dists=["et","eta","phi"]
## L1Objs=["Muon"]

## Dists=["eta"]
## L1Objs=["Jet","Tau","EG","Muon"]

label1 = "l1t-tsg-v3";
treeName1="l1UpgradeEmuTree/L1UpgradeTree"
## fileNames1=["L1Ntuple.root"]
## label1 = "l1t-integration-v13.1";
## treeName1="l1UpgradeEmuTree/L1UpgradeTree"
## fileNames1=["/afs/cern.ch/work/a/apana/L1Upgrade/Stage2/l1t-integration-v13.1/CMSSW_8_0_2/src/L1Ntuple.root"]
# fileNames1=["/afs/cern.ch/work/a/apana/L1Upgrade/Stage2/l1t-integration-v2/CMSSW_8_0_0_pre6/src/L1Ntuple.root"]
fileNames1=[
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_1.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_10.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_11.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_12.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_13.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_14.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_15.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_17.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_18.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_2.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_20.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_21.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_23.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_3.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_31.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_32.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_34.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_39.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_4.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_42.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_43.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_44.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_46.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_47.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_48.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_49.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_5.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_50.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_51.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_54.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_55.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_56.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_57.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_58.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_59.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_6.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_60.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_61.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_62.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_63.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_64.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_65.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_66.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_67.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_68.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_69.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_7.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_70.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_8.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3/ZeroBias3/crab_l1-tsg-v3__259721_ZeroBias3/160225_181422/0000/L1Ntuple_9.root",
## SingleNeutrino_25nsPU30/160228_150657/0000/L1Ntuple_9.root",
## SingleNeutrino_25nsPU30/160228_150657/0000/L1Ntuple_90.root",
## SingleNeutrino_25nsPU30/160228_150657/0000/L1Ntuple_91.root",
## SingleNeutrino_25nsPU30/160228_150657/0000/L1Ntuple_92.root",
]

label2 = "l1t-tsg-v4";
treeName2="l1UpgradeEmuTree/L1UpgradeTree"
## fileNames2=["L1Trigger/L1TCommon/test/l1t_stage2.root"]
## fileNames2=["/afs/cern.ch/work/a/apana/L1Upgrade/Stage2/l1t-tsg-v2-patch1/CMSSW_8_0_0_pre6/src/L1Ntuple.root"]
## fileNames2=["/afs/cern.ch/work/a/apana/L1Upgrade/Stage2/l1t-tsg-v4/CMSSW_8_0_2/src/L1Ntuple.root"]
fileNames2=[
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_1.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_10.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_11.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_12.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_13.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_14.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_15.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_17.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_18.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_19.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_2.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_20.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_21.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_22.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_23.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_24.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_25.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_26.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_27.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_28.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_29.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_3.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_30.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_31.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_32.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_33.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_34.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_4.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_5.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_6.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_7.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_8.root",
"root://eoscms//eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v4/ZeroBias3/crab_l1-tsg-v4__259721_ZeroBias3/160315_144943/0000/L1Ntuple_9.root",
]

#===============================================================

class SetupHistos():

    def setPlotAttributes(self,h1,h2,l1coll,varString,cutString,logy,ymin,ymax,xmin,xmax):
        self.h1=h1
        self.h2=h2
        self.l1coll=l1coll
        self.varString=varString
        self.cutString=cutString
        self.logy=logy
        self.ymin=ymin
        self.ymax=ymax
        self.xmin=xmin
        self.xmax=xmax 
    
    def __init__(self, L1Object="xxx", Dist="et"):

        ### Energy Sum indices ###  Base on "DataFormats/L1Trigger/interface/EtSum.h"
        ETT = 0; HTT = 1; ETM = 2; HTM = 3
        
        l1coll="XXX"; varString=""; cutString=""; logy=1; ymin=0.1; ymax=-1; xmin=0.; xmax=-1; nbins=100; rebin=1;
        self.setPlotAttributes(ROOT.nullptr,ROOT.nullptr,l1coll,varString,cutString,logy,ymin,ymax,xmin,xmax)
        
        if (L1Object == "Jet" or L1Object == "CenJet"):
            nbins=50; xmin=0.; xmax=250.

            l1coll="L1Upgrade.jetEt";
            cutString = "L1Upgrade.jetBx==0"            
            if L1Object == "CenJet":
                cutString = cutString + " && L1Upgrade.jetEta>-3. && L1Upgrade.jetEta<3.";

            if Dist == "eta":
                l1coll="L1Upgrade.jetEta";
                cutString = cutString + " && L1Upgrade.jetEt>30."
            if Dist == "phi":
                l1coll="L1Upgrade.jetPhi";

        elif (L1Object == "Tau" or L1Object == "NonIsoTau"  or L1Object == "IsoTau"):
            nbins=16; xmin=0.; xmax=64.
            
            l1coll="L1Upgrade.tauEt";
            cutString="L1Upgrade.tauBx==0";
            
            if (L1Object == "NonIsoTau"):
                cutString=cutString + " && L1Upgrade.tauIso==0";    
            if (L1Object == "IsoTau"):
                cutString=cutString + " && L1Upgrade.tauIso==1";
                
            if Dist == "eta":
                l1coll="L1Upgrade.tauEta";
                cutString = cutString + " && L1Upgrade.tauEt>30."
            if Dist == "phi":
                l1coll="L1Upgrade.tauPhi";
            
        elif (L1Object == "EG" or L1Object == "NonIsoEG" or L1Object == "IsoEG"):
            nbins=64;xmax=64;rebin=4;

            l1coll="L1Upgrade.egEt";
            cutString = "L1Upgrade.egBx==0"            
            if (L1Object == "NonIsoEG"):
                cutString=cutString + " && L1Upgrade.egIso==0";
            elif (L1Object == "IsoEG"):
                cutString=cutString + " && L1Upgrade.egIso==1";


            if Dist == "eta":
                l1coll="L1Upgrade.egEta";
                cutString = cutString + " && L1Upgrade.egEt>10."                
            if Dist == "phi":
                l1coll="L1Upgrade.egPhi";


        elif ( L1Object == "ETT" or L1Object == "HTT" or L1Object == "ETM" or L1Object == "HTM"):
            xmax=460; nbins=460; rebin=5;
            
            if L1Object == "ETT":
                sumIndx= ETT
            elif L1Object == "HTT":
                sumIndx= HTT
            elif L1Object == "HTM":
                sumIndx= HTM
            elif L1Object == "ETM":
                sumIndx= ETM
     
            l1coll="L1Upgrade.sumEt[" + str(sumIndx) + "]"
            if Dist == "phi":
                l1coll="L1Upgrade.sumPhi[" + str(sumIndx) + "]"
            
            ## cutString="L1Upgrade.sumType==" + str(sumIndx) + " && L1Upgrade.sumBx[" + str(sumIndx) + "]==0"
            cutString="L1Upgrade.sumBx[" + str(sumIndx) + "]==0"


        elif ( L1Object == "Muon"):
            xmax=30; nbins=30; rebin=1;

            l1coll="L1Upgrade.muonEt";
            cutString = "L1Upgrade.muonBx==0 && L1Upgrade.muonQual>=12"
            
            if Dist == "eta":
                l1coll="L1Upgrade.muonEta";
                cutString = cutString + " && L1Upgrade.muonEt>0."
            if Dist == "phi":
                l1coll="L1Upgrade.muonPhi";

            
        if ("eta"==Dist):
            xmin=-5; xmax=5; nbins=230; logy=0; rebin=5
            ##if L1Object.find("EG") > -1 or L1Object.find("Muon") > -1:
            ##    xmin=-3; xmax=3; nbins=230; logy=0; rebin=1
        if ("phi"==Dist):
            xmin=-3.14159; xmax=3.14159; nbins=144; logy=0; rebin=4


        if Rebin > 0: rebin=Rebin

        hname1= L1Object + "_" + Dist + "_1"; hname2=L1Object + "_" + Dist +"_2";
        h1 = TH1F(hname1,hname1,nbins,xmin,xmax);
        h2 = TH1F(hname2,hname2,nbins,xmin,xmax);

        h1.Sumw2();  h2.Sumw2();
        h1.SetLineColor(ROOT.kRed); h2.SetLineColor(kBlue);
        h1.Rebin(rebin);           h2.Rebin(rebin);

        self.setPlotAttributes(h1,h2,l1coll,varString,cutString,logy,ymin,ymax,xmin,xmax)
        
def plotDist(L1Obj,dist,Rebin,outdir):

    histos=SetupHistos(L1Obj,dist)

    branch1=histos.l1coll;   cut1=histos.cutString;
    branch2=histos.l1coll;   cut2=histos.cutString;

    xmax=histos.xmax
    ymax=histos.ymax

    nEntTree1=tree1.GetEntries()
    nEntTree2=tree2.GetEntries()    
    print "Number of Events on tree1: ", nEntTree1
    print "Number of Events on tree2: ", nEntTree2
    
    print "\nL1Obj= ",L1Obj,"\n"
    print branch1,cut1
    print branch2,cut2

    h1=histos.h1;h2=histos.h2
    tree1.Project(h1.GetName(),branch1,cut1)
    tree2.Project(h2.GetName(),branch2,cut2)

    if (histos.ymax > 0.):
        h1.GetYaxis().SetRangeUser(histos.ymin,histos.ymax);
        h2.GetYaxis().SetRangeUser(histos.ymin,histos.ymax);
        
    print "h1: ",h1.GetEntries()
    print "h2: ",h2.GetEntries()

    if ymax>0:
        h1.GetYaxis().SetRangeUser(0.2,ymax);

    if L1Obj.find("Jet")==-1 and dist == 'eta':
        h1.GetXaxis().SetRangeUser(-3,3);
        h2.GetXaxis().SetRangeUser(-3,3);        

    #if xmax>0:
    #    h1.GetXaxis().SetRangeUser(0,xmax);
    ##h1.GetXaxis().SetRangeUser(10,25);


    xlabel="xxx"
    if dist == 'et':
        xlabel="E_{T}"
    elif dist == 'phi':
        xlabel="Phi"
    elif dist == 'eta':
        xlabel="Eta"

    h1.GetXaxis().SetTitle(xlabel)

    nent1=h1.GetEntries()
    nent2=h2.GetEntries()

    if ScaleToNumberOfEntries:
        fact=float(nEntTree1)/float(nEntTree2)
        print " !!!Scaling tree2 histogram to number of events on tree1.  Scale factor: ", fact
        h2.Scale(fact)
    
    # h1.Scale(1./h1.GetEntries())
    # h2.Scale(1./h2.GetEntries())

    ## c1=prepPlot("c1","L1Extra")
    ## c1.SetLogy(histos.logy)
    c1,p1,p2 = prep1by2Plot("c1","L1Upgrade",500)
    p1.Draw(); p2.Draw()

    p1.cd()
    p1.SetLogy(histos.logy)

    h1.SetLabelOffset(0.1, "X");
    ## h2.Scale(0.5)
    h1.Draw()
    h2.Draw("sames")

    xinit=0.2
    if L1Obj == "IsolatedEG" and dist=="et":
        xinit=0.6

    xl1=xinit; yl1=0.1; xl2=xl1+.2; yl2=yl1+.1;
    leg0=PrepLegend(xl1,yl1,xl2,yl2,0.03)
    leg0.AddEntry(h1,label1,"pl")
    leg0.AddEntry(h2,label2,"pl")
    leg0.Draw();

    DrawText(0.525,0.8,L1Obj,0.04)
    DrawText(0.525,0.75,xlabel,0.04)
    gPad.Update();
    ## print h1.GetListOfFunctions()
    ## print h1.GetListOfFunctions().FindObject("stats")
    tt1=h1.GetListOfFunctions().FindObject("stats")
    tt1.SetTextColor(h1.GetLineColor());
    tt2=h2.GetListOfFunctions().FindObject("stats")
    tt2.SetTextColor(h2.GetLineColor());
    x1 = tt1.GetX1NDC();    y1 = tt1.GetY1NDC();
    x2 = tt1.GetX2NDC();    y2 = tt1.GetY2NDC();
    ## dx = x2-x1;             dy = y2-y1;
    dy = 0.105;
    dx = 0.20;
    tt1.SetY2NDC(y2);        tt1.SetX2NDC(x2);
    tt1.SetY1NDC(y2-dy);     tt1.SetX1NDC(x2-dx);
    tt2.SetY2NDC(y2-dy);     tt2.SetX2NDC(x2);
    tt2.SetY1NDC(y2-2*dy);   tt2.SetX1NDC(x2-dx);
    gPad.Modified();
    gPad.Update();

    hRat= h2.Clone()
    hRat.SetName("Ratio")
    hRat.Divide(h2,h1,1.,1.,"");

    hRat.SetStats(0)
    ResetAxisAndLabelSizes(hRat,0.065,0.01)
    cname="Ratio"

    p2.cd()

    ## hRat.GetXaxis().SetRangeUser(10,25);

    ## hRat.GetXaxis().SetTitle(xlabel)
    min=0.5; max=1.5
    hRat.SetMaximum(2.5)
    hRat.SetMinimum(0.0)
    hRat.Draw()

    xl1=0.6; yl1=.3;
    DrawText(xl1,yl1,label2+"/"+label1,0.075)

    gPad.Update();

    if (PrintPlot):
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        psname=os.path.join(outdir,"comp_" + L1Obj + "_" + dist)
        c1.Print(psname + ".gif")

    cont=""
    cont=raw_input('\npress return to continue... anything else to quit...')
    if 0 < len(cont):
        sys.exit(0)

def ReadChain(treeName,fileNames):

    theTree=TChain(treeName)
    
    i=0
    for f in fileNames:
        i=i+1
        if f.find("/eos/cms")==0:
            f="root://eoscms/" + f
        print i,f
        theTree.Add(f)

    print "\n"
    return theTree

if __name__ == '__main__':

    SetStyle()
    gStyle.SetOptStat(110);
#===============================================================

    tree1=ReadChain(treeName1,fileNames1);
    tree2=ReadChain(treeName2,fileNames2);
    
    for L1Obj in L1Objs:
        for dist in Dists:
            if dist == "eta" and (L1Obj == "ETT" or  L1Obj == "HTT" or  L1Obj == "ETM" or  L1Obj == "HTM"):
                pass
            elif dist == "phi" and (L1Obj == "ETT" or  L1Obj == "HTT"):
                pass
            else:
                plotDist(L1Obj,dist,Rebin,outdir)
        
    
#===============================================================
#    if os.getenv("FROMGUI") == None:
#        print "Not from GUI"
#        raw_input('\npress return to end the program...')
