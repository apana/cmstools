import FWCore.ParameterSet.Config as cms

process = cms.Process('L1TUNPACK')

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.Geometry.GeometryIdeal_cff')
process.load("Configuration.StandardSequences.RawToDigi_cff")

# Select the Message Logger output you would like to see:
process.load('FWCore.MessageService.MessageLogger_cfi')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
    )

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring("/store/data/Run2015D/SingleMuon/RAW/v1/000/256/675/00000/1C374320-EC5C-E511-A843-02163E0142A8.root")
    )


process.output = cms.OutputModule(
    "PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('keep *'),
#    outputCommands = cms.untracked.vstring('drop *',
#                                           'keep *_*_*_L1TEMULATION'),
    fileName = cms.untracked.string('unpack.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    )
                                           )
process.options = cms.untracked.PSet()

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag.globaltag = '74X_dataRun2_Prompt_v1'

from EventFilter.L1TRawToDigi.caloStage1Digis_cfi import caloStage1Digis
process.caloStage1Digis = caloStage1Digis.clone()

import EventFilter.GctRawToDigi.l1GctHwDigis_cfi
process.gctDigis = EventFilter.GctRawToDigi.l1GctHwDigis_cfi.l1GctHwDigis.clone()

process.p1 = cms.Path(
    process.caloStage1Digis +
    process.gctDigis
    )

process.output_step = cms.EndPath(process.output)

process.schedule = cms.Schedule(
    process.p1, process.output_step
    )


processDumpFile = open('unpack.dump', 'w')
print >> processDumpFile, process.dumpPython()
