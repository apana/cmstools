#!/usr/bin/python
#
import sys,string,math,os,subprocess,socket

Debug=False
## Debug=True

def GetFiles(Dir):

    files=[]
    print Dir
    p1 = subprocess.Popen(["srmls", "-2", Dir], shell=False, stdout=subprocess.PIPE)
    (stdout, stderr)=p1.communicate()
    if stderr is not None:
        print "Trouble executing the srmls command"
        sys.exit(1)

    if Debug:
        print "Raw output"
        print stdout
        print "Done\n"

    theOutput=stdout.split('\n')
    # print "\n Number of files to copy: ",len(files),"\n"
    ifile=0
    for l in theOutput:

        ncols=len(l.split())

        if ncols==2:
            cols=l.split()
            size=cols[0]
            f=string.strip(cols[1])
            # print f
        else:
            size="-1"
            f=string.strip(l)

        if len(f)==0:
            break

        if f.find(".root")>-1:
            ifile=ifile+1
            filename=f[f.rfind("/")+1:]
            files.append(filename)

    if Debug:
        print ifile,len(files),files
    return files

def removeDuplicates(inFiles,outFiles):
    foundDup=False

    files=[]
    for inFil in inFiles:
        foundDup=False
        for outFil in outFiles:
            ## print inFil,outFil
            if inFil == outFil: 
                ## print "Found"
                foundDup=True
                break
        if not foundDup: files.append(inFil)
    if Debug:
        print "======================Files to copy================================"
        print files
    return files

if __name__ == '__main__':

    print "\n Machine:", socket.gethostname()
    ## srcSe="srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/arizzi"
    ## dstSe="srm://cmssrm.fnal.gov:8443/srm/managerv2?SFN=/11/store/user/lpchbb/apana"

    ## srcSe="srm://cmseos.fnal.gov:8443/srm/v2/server?SFN=/eos/uscms/store/user/lpctrig/apana/L1Menu_2016/Stage2"
    ## dstSe="srm://srm-eoscms.cern.ch:8443/srm/v2/server?SFN=/eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v2"

    ## srcSe="srm://srm-eoscms.cern.ch:8443/srm/v2/server?SFN=/eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2/l1-tsg-v3"
    ## dstSe="srm://cmseos.fnal.gov:8443/srm/v2/server?SFN=/eos/uscms/store/user/lpctrig/apana/L1Menu_2016/Stage2/l1-tsg-v3"

    ## srcSe="srm://srm-eoscms.cern.ch:8443/srm/v2/server?SFN=/eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/apana"
    ## dstSe="srm://cmseos.fnal.gov:8443/srm/v2/server?SFN=/eos/uscms/store/user/lpctrig/apana"

    ## srcSe="srm://cmseos.fnal.gov:8443/srm/v2/server?SFN=/eos/uscms/store/user/lpctrig/apana/L1Menu_2016/Stage2/l1t-integration-v34p0"    
    ## dstSe="srm://srm-eoscms.cern.ch:8443/srm/v2/server?SFN=/eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu_2016/Stage2/l1t-integration-v34p0"

    srcSe="srm://srm-eoscms.cern.ch:8443/srm/v2/server?SFN=/eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016/Stage2"    
    dstSe="srm://cmseos.fnal.gov:8443/srm/v2/server?SFN=/eos/uscms/store/user/lpctrig/apana/L1Menu_2016/Stage2"
    
    # subDir="Ntuple_Step1V42_Step2Tag_EDMV42_Step2_V4_Data"
    # subDir="Ntuple_Step1V42_Step2Tag_EDMV42_Step2_V4_DataMoreStat"
    # subDir="Ntuple_Step1V42_Step2Tag_EDMV42_Step2_V4a_MC"
    # subDir="ZeroBias/crab_258440_ZeroBias_Run2015D-v1/160212_222241/0000"
    # subDir="ZeroBias/crab_258448_ZeroBias_Run2015D-v1/160212_222149/0000"
    # subDir="ZeroBias/crab_l1-tsg-v3__258448_ZeroBias/160225_181930/0000"
    # subDir="ZeroBias/crab_l1-tsg-v3__258440_ZeroBias/160225_181837/0000"
    # subDir="ZeroBias/crab_l1-tsg-v3__258440_ZeroBias/160225_181837/0000"
    # subDir1="ZeroBias4/crab_l1-tsg-v3__259721_ZeroBias4/160225_181331/0000"
    # subDir2="ZeroBias4/crab_l1-tsg-v3__259721_ZeroBias4/160225_181331/0000"

    # subDir="ZeroBias1/crab_l1-tsg-v3__259626_ZeroBias1/160225_175336/0000"
    # subDir="ZeroBias2/crab_l1-tsg-v3__259626_ZeroBias2/160225_175402/0000/"
    # subDir="ZeroBias3/crab_l1-tsg-v3__259626_ZeroBias3/160225_175428/0000"
    # subDir="ZeroBias4/crab_l1-tsg-v3__259626_ZeroBias4/160225_175458/0000"

    # subDir="uGT-tst"
    # subDir="SingleMuon/crab_l1t-integration-v35p0__SingleMuon_ZMu/160412_235246/0000"
    # subDir="SingleMuon/crab_l1t-integration-v34p0__SingleMuon_ZMu/160412_073128/0000"
    subDir="comp_xmlV5_/ZeroBias1/crab_comp_xmlV5___259721_ZeroBias1/160420_225920/0000"
    
    inDir=os.path.join(srcSe,subDir)
    outDir=os.path.join(dstSe,subDir)

    files=GetFiles(inDir)
    currfiles=GetFiles(outDir) ## find out how many files are there
    if len(currfiles)>0:
        files=removeDuplicates(files,currfiles)

    ifile=0

    print "Number of files to copy: ",len(files)
    for filename in files:

        ifile=ifile+1
        infile=os.path.join(inDir,filename)
        outfile=os.path.join(outDir,filename)

        print "\tCopying file ",ifile,infile
        mycmd="lcg-cp -D srmv2"
        myarg=infile + " " + outfile
        # print mycmd
        # print infile,outfile
        if not Debug:
            print infile
            print outfile
                
            ## p = subprocess.Popen(["lcg-cp","-D","srmv2",infile,outfile], shell=False)  ## doesn't seem to work anymore
            ## p = subprocess.Popen(["srmcp","-2",infile,outfile], shell=False)

            p = subprocess.Popen(["lcg-cp","-b","-D","srmv2",infile,outfile], shell=False)  ## doesn't seem to work anymore
            sts = os.waitpid(p.pid, 0)[1]




    
