#!/usr/bin/env python

import sys,string,math,os
from ROOT import TF1, TFile, TH1F, TTree, TChain, SetOwnership,TCanvas
from ROOT import gDirectory

def usage():
    """ Usage: checkAnalyzerJobs <Dir>  <skipfilelist>
    
    Check HbbAnalyzer jobs from given input directory
    """
    pass

if __name__ == "__main__":


    narg=len(sys.argv)
    if narg < 2:
        print usage.__doc__
        sys.exit(1)

    indir=sys.argv[1]
    os.chdir(indir)
    filelist=os.listdir(os.path.curdir)

    skiplist=[]
    for i in range(2,narg):
        skiplist.append(sys.argv[i])
    # print skiplist

    for infile in filelist:
        if infile.find(".root")>-1:

            if infile in skiplist:
                continue

            # if infile=="Hbb_Zee__ZZ.root" or infile=="Hbb_Zee__TTJets_Hadronic.root" or \
            #         infile=="Hbb_Zee__DYJetsToLL_pT70-100_bJets.root":
            #    continue

            print "Checking: " + infile
            f=TFile.Open(infile)
            # f.ls()

            hname="NStep1"
            h=f.Get(hname)
            nent=int(h.GetBinContent(1))
            if nent == 0:
                print "\tNStep1 histogram has zero entries -- Trouble"

            
