import FWCore.ParameterSet.Config as cms

nevts=-1
processName="HLT"
pathToSkim="HLT_ZeroBias"

inputfile="/store/data/Commissioning10/MinimumBias/RAW/v4/000/133/877/482CE7B7-C04F-DF11-A822-001D09F24682.root"
OutputFile= "/tmp/apana/MBSkim_Run133877_test.root"

process= cms.Process('SKIM')

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.load('FWCore/MessageService/MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(nevts)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(inputfile)
)

import HLTrigger.HLTfilters.hltHighLevel_cfi
process.myHLTFilter = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.myHLTFilter.TriggerResultsTag = cms.InputTag("TriggerResults","",processName)
process.myHLTFilter.andOr = True
# process.myHLTFilter.HLTPaths = ["HLT_MinBiasBSC"]
process.myHLTFilter.HLTPaths = [ pathToSkim ]

process.mySkim = cms.Path(process.myHLTFilter)

process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'mySkim' ) ),
    fileName = cms.untracked.string(OutputFile)
)
process.o = cms.EndPath( process.out )

process.schedule = cms.Schedule(process.mySkim, process.o)

