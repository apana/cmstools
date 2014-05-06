#!/usr/bin/python
#
import sys,string,math,os,subprocess,socket

Debug=False
# Debug=True

if __name__ == '__main__':

    print "\n Machine:", socket.gethostname()
    srcSe="srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/arizzi"
    dstSe="srm://cmssrm.fnal.gov:8443/srm/managerv2?SFN=/11/store/user/lpchbb/apana"
    dstSe2="/pnfs/cms/WAX/11/store/user/lpchbb/apana"

    # subDir="Ntuple_Step1V42_Step2Tag_EDMV42_Step2_V4_Data"
    # subDir="Ntuple_Step1V42_Step2Tag_EDMV42_Step2_V4_DataMoreStat"
    # subDir="Ntuple_Step1V42_Step2Tag_EDMV42_Step2_V4a_MC"
    subDir="Ntuple_Step1V42_Step2Tag_EDMV42_Step2_V4a_MCMoreStat"

    inDir=os.path.join(srcSe,subDir)
    outDir=os.path.join(dstSe,subDir)
    outDir2=os.path.join(dstSe2,subDir)

    p1 = subprocess.Popen(["srmls", "-2", inDir], shell=False, stdout=subprocess.PIPE)
    (stdout, stderr)=p1.communicate()
    if stderr is not None:
        print "Trouble executing the srmls command"
        sys.exit(1)

    if Debug:
        print "Raw output"
        print stdout
        print "Done\n"

    files=stdout.split('\n')
    # print "\n Number of files to copy: ",len(files),"\n"

    ifile=0

    for l in files:

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


            infile=os.path.join(inDir,filename)
            outfile=os.path.join(outDir,filename)
            outfile2=os.path.join(outDir2,filename)

            print "\tCopying file ",ifile
            mycmd="lcg-cp -D srmv2"
            myarg=infile + " " + outfile
            # print mycmd
            # print infile,outfile
            if not Debug:
                
                # check if file already exists at destination
                if os.path.exists(outfile2):
                    print "file already exists at destination"
                else:
                    ## p = subprocess.Popen(["lcg-cp","-D","srmv2",infile,outfile], shell=False)  ## doesn't seem to work anymore
                    ## p = subprocess.Popen(["lcg-cp","-b","-D","srmv2",infile,outfile], shell=False)  ## doesn't seem to work anymore
                    p = subprocess.Popen(["srmcp","-2",infile,outfile], shell=False)
                    sts = os.waitpid(p.pid, 0)[1]
            print infile
            print outfile




    
