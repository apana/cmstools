import FWCore.ParameterSet.Config as cms

# InputFile="file:ZH_ZToLL_HToBB_M-120_7TeV-powheg-herwigpp_Summer11-PU_S4_START42_V11-v1_2_1_1JZ.root"
InputFile="dcap://cmsdca.fnal.gov:24136/pnfs/fnal.gov/usr/cms/WAX/11/store/user/apana/Higgs/Summer11/copyJob/ZH_ZToLL_HToBB_M-120_7TeV-powheg-herwigpp_Summer11-PU_S4_START42_V11-v1_7_1_quo.root"
OutputFile="Skim_Higgs_pT300.root"
nevts=-1


process = cms.Process("MySkim")

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

import Analysis.SkimMCGen.SkimMCGen_cfi as skimMCGen
#

process.myHiggsFilter = skimMCGen.skim.clone(
    # genpart=cms.int32(23), # Z's
    genpart=cms.int32(25), # h's
    daughters=cms.int32(5), # b's
    genpt=cms.double(300.)
    )

process.myZFilter = skimMCGen.skim.clone(
    genpart=cms.int32(23), # Z's
    daughters=cms.int32(13), # b's
    genpt=cms.double(250.)
    )

process.FilterPath = cms.Path( process.myHiggsFilter * process.myZFilter)

process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'FilterPath') ), 
    fileName = cms.untracked.string(OutputFile)
)

process.o = cms.EndPath( process.out )
# process.schedule = cms.Schedule(process.o)
