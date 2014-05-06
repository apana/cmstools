#!/bin/python

MYEXEC = 'hadd'

CopyCommand="dccp" # dccp (dCache) or cp

import sys,string,math,os, commands
if __name__ == '__main__':


    NFIL=50
    run="r135149"

    ds="MB"
    if (ds =="MB"):
        dataset="MinimumBiasDS"
    elif (ds == "ZB"):
        dataset="ZeroBiasDS"
    else:
        dataset="xxxDS"

    if (CopyCommand == "dccp"):
        inbase="/pnfs/cms/WAX/resilient/apana/OpenHLT"
    else:
        inbase="/uscmst1b_scratch/lpc1/lpctrig/apana/data/rerunHLT/Macbeth"
        
    rundir=run+ "_" + ds
    indir=os.path.join(inbase,rundir)
    
    outbase="openhlt_" + run + "_" + dataset + ".root"
    
    outfile1=os.path.join("/uscmst1b_scratch/lpc1/lpctrig/apana/data/tmp",outbase)
    outfile2=os.path.join("/uscmst1b_scratch/lpc1/lpctrig/apana/data/OpenHLT",outbase)

    sourcedir=indir
    targetdir=os.path.join("/uscmst1b_scratch/lpc1/lpctrig/apana/data/tmp",rundir)
    if not os.path.exists(targetdir):
        os.mkdir(targetdir)

    a=1
    ngood=0
    while a < NFIL+1:
        
        rootfile="openhlt_" +str(a) + "_1.root"

        sourcefile=os.path.join(sourcedir,rootfile)
        targetfile=os.path.join(targetdir,rootfile)
        # print sourcefile
        xx=commands.getstatusoutput("ls " + sourcefile)
        returnVal= xx[0]
        # if returnVal==0 all is OK

        if (returnVal==0):
            ngood+=1
            # print sourcefile
            myargs=string.join([CopyCommand,sourcefile,targetfile])
            print myargs
            os.system(myargs)
            
        a+=1

    print ""
    print "Number of files found: ", ngood
    print "Number of files requested: ", NFIL
    print ""

    if ngood > 0:
        myargs=string.join([MYEXEC,outfile1,"*"])
        os.chdir(targetdir)
        print "Executing: ",myargs
        os.system(myargs)

        myargs=string.join(["cp",outfile1,outfile2])
        print "Executing: ",myargs
        os.system(myargs)
    else:
        print "Problems"
    print "\n"
