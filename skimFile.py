import FWCore.ParameterSet.Config as cms

SKIMPATH="HLT_Physics_v1"

InputFile="/store/data/Run2011A/MinimumBias/RAW/v1/000/161/310/E8F97EA7-9C55-E011-AA3C-001D09F25109.root"
OutputFile="Skim_" + SKIMPATH +".root"
nevts=-1



process = cms.Process("HLTSkim")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(InputFile),
    skipBadFiles = cms.untracked.bool(True)                  
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( nevts )
)

import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
#

process.myFilter = hlt.hltHighLevel.clone(
    HLTPaths = [ SKIMPATH],
    throw = False
    )

process.FilterPath = cms.Path( process.myFilter )

process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'FilterPath') ), 
    fileName = cms.untracked.string(OutputFile)
)

process.o = cms.EndPath( process.out )
# process.schedule = cms.Schedule(process.o)
