import FWCore.ParameterSet.Config as cms
import sys

CRAB=False

if CRAB:
    InputFile="XXX"
else:
    narg=len(sys.argv)
    # print narg
    if (narg < 3 ):
        print "please specify an input file"
        sys.exit()
    InputFile=sys.argv[2]


process = cms.Process("GetContent")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(InputFile)
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32( 1 ) )

# import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
process.load("FWCore.Modules.printContent_cfi")

process.p = cms.Path( process.printContent )
