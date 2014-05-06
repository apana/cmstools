import FWCore.ParameterSet.Config as cms

InputFile="dcap://cmsdca1.fnal.gov:24139/pnfs/fnal.gov/usr/cms/WAX/11/store/relval/CMSSW_2_2_4/RelValZMM/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V8_v1/0000/0621AFE7-69F3-DD11-8E0F-001D09F23A07.root"
OutputFile="dropped.root"
nevts=100


process = cms.Process("DROP")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(InputFile )
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( nevts )
)
 
process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring(
        'keep *',
        'drop *_simGtDigis_*_*',
        'drop *_simGmtDigis_*_*',
        'drop *_sim*Digis_*_*'
    ),
    fileName = cms.untracked.string(OutputFile)
)

process.o = cms.EndPath( process.out )
process.schedule = cms.Schedule(process.o)
