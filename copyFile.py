import FWCore.ParameterSet.Config as cms

InputFile="/store/mc/Summer09/MinBias900GeV/GEN-SIM-RAW/MC_31X_V3_preproduction_312-v1/0009/8249DD53-C17A-DE11-AC8C-00E08134420C.root"
OutputFile="copy.root"
nevts=10


process = cms.Process("COPY")

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
 
process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('keep *'),
    fileName = cms.untracked.string(OutputFile)
)

process.o = cms.EndPath( process.out )
process.schedule = cms.Schedule(process.o)
