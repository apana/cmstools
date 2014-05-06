import FWCore.ParameterSet.Config as cms

##################################################################

NEVTS=-1
ProcessName="TEST"

##################################################################
process = cms.Process("TRIGREPORT")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.MessageLogger.categories.append('HLTrigReport')

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(False)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    'dcap://cmsdca.fnal.gov:24136/pnfs/fnal.gov/usr/cms/WAX/resilient/apana/week11/r130910_V2/outputA_1.root',
    'dcap://cmsdca.fnal.gov:24136/pnfs/fnal.gov/usr/cms/WAX/resilient/apana/week11/r130910_V2/outputA_2.root',
    'dcap://cmsdca.fnal.gov:24136/pnfs/fnal.gov/usr/cms/WAX/resilient/apana/week11/r130910_V2/outputA_3.root',
    'dcap://cmsdca.fnal.gov:24136/pnfs/fnal.gov/usr/cms/WAX/resilient/apana/week11/r130910_V2/outputA_4.root',
    'dcap://cmsdca.fnal.gov:24136/pnfs/fnal.gov/usr/cms/WAX/resilient/apana/week11/r130910_V2/outputA_5.root',
    'dcap://cmsdca.fnal.gov:24136/pnfs/fnal.gov/usr/cms/WAX/resilient/apana/week11/r130910_V2/outputA_6.root',
    'dcap://cmsdca.fnal.gov:24136/pnfs/fnal.gov/usr/cms/WAX/resilient/apana/week11/r130910_V2/outputA_7.root',
    'dcap://cmsdca.fnal.gov:24136/pnfs/fnal.gov/usr/cms/WAX/resilient/apana/week11/r130910_V2/outputA_8.root',
    'dcap://cmsdca.fnal.gov:24136/pnfs/fnal.gov/usr/cms/WAX/resilient/apana/week11/r130910_V2/outputA_9.root',
    'dcap://cmsdca.fnal.gov:24136/pnfs/fnal.gov/usr/cms/WAX/resilient/apana/week11/r130910_V2/outputA_10.root',
    'dcap://cmsdca.fnal.gov:24136/pnfs/fnal.gov/usr/cms/WAX/resilient/apana/week11/r130910_V2/outputA_11.root',
    'dcap://cmsdca.fnal.gov:24136/pnfs/fnal.gov/usr/cms/WAX/resilient/apana/week11/r130910_V2/outputA_12.root',
    'dcap://cmsdca.fnal.gov:24136/pnfs/fnal.gov/usr/cms/WAX/resilient/apana/week11/r130910_V2/outputA_13.root',
    'dcap://cmsdca.fnal.gov:24136/pnfs/fnal.gov/usr/cms/WAX/resilient/apana/week11/r130910_V2/outputA_14.root',
    'dcap://cmsdca.fnal.gov:24136/pnfs/fnal.gov/usr/cms/WAX/resilient/apana/week11/r130910_V2/outputA_15.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( NEVTS ),
    skipBadFiles = cms.bool(True)
    )

process.load("HLTrigger.HLTanalyzers.hlTrigReport_cfi")
process.hlTrigReport.HLTriggerResults = cms.InputTag("TriggerResults","",ProcessName)

process.printReport = cms.Path( process.hlTrigReport )

process.schedule = cms.Schedule(process.printReport)


