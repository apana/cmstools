#!/bin/python

MYEXEC = 'hadd'
import sys,string,math,os, commands
if __name__ == '__main__':


    NFIL=32
    run="r124230"

    # indir="/castor/cern.ch/user/a/apana/OpenHLT/"
    # indir = "/castor/cern.ch/cms/store/caf/user/apana/user/a/apana/"    
    indir="/castor/cern.ch/cms/store/caf/user/apana/"

    # outbase="openhlt_redoL1_" + run + "_MinimumBiasDS.root"
    outbase="openhlt_jetid_" + run + "_MinimumBiasDS.root"
    # outbase="L1Tree_" + run + "_MinimumBiasDS.root"
    
    outfile1=os.path.join("/tmp/apana",outbase)
    outfile2=os.path.join("/castor/cern.ch/user/a/apana/OpenHLT",outbase)

    sourcedir=os.path.join(indir,run)
    targetdir=os.path.join("/tmp/apana",run)
    if not os.path.exists(targetdir):
        os.mkdir(targetdir)

    a=1
    ngood=0
    while a < NFIL+1:
        
        rootfile="openhlt_mb_jetid_" +str(a) + ".root"
        # rootfile="openhlt_mb_redoL1_" +str(a) + ".root"

        sourcefile=os.path.join(sourcedir,rootfile)
        targetfile=os.path.join(targetdir,rootfile)
        
        xx=commands.getstatusoutput("rfdir " + sourcefile)
        returnVal= xx[0]
        # if returnVal==0 all is OK

        if (returnVal==0):
            ngood+=1
            print sourcefile
            myargs=string.join(["rfcp",sourcefile,targetfile])
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

        myargs=string.join(["rfcp",outfile1,outfile2])
        print "Executing: ",myargs
        os.system(myargs)
    else:
        print "Problems"
    print "\n"
