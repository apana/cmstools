#!/usr/bin/python
#
import sys,string,math,os,subprocess

Debug=True
PrintOnlyRootFiles=False
ShowFileSize=True

# remoteDir="srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/arizzi/Step1V33_Step2_finalData"

# remoteDir="srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/arizzi/Ntuple_Step1V42_Step2Tag_EDMV42_Step2_V4a_Data"
# remoteDir="srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/arizzi/Ntuple_Step1V42_Step2Tag_EDMV42_Step2_V4_DataMoreStat"
# remoteDir="srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/arizzi/Ntuple_Step1V42_Step2Tag_EDMV42_Step2_V4a_MC"

# remoteDir="srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/arizzi/Ntuple_Step1V42_Step2Tag_EDMV42_Step2_V6_MC"

remoteDir="srm://dcache-se-desy.desy.de:8443/srm/managerv2?SFN=/nfs"

if __name__ == '__main__':


    p1 = subprocess.Popen(["srmls", "-2", remoteDir], shell=False, stdout=subprocess.PIPE)
    (stdout, stderr)=p1.communicate()
    if stderr is not None:
        print "Trouble executing the srmls command"
        sys.exit(1)
    
    if Debug:
        print "Raw output"
        print stdout
        print "Done\n"

    files=stdout.split('\n')
    # print "\n Number of files in directory: ",len(files),"\n"
    print "\n"

    nfiles=0
    for l in files:
        ncols=len(l.split())
        # print ncols
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

        if PrintOnlyRootFiles and f.find(".root")==-1:
            pass
        else:
            filename=f[f.rfind("/")+1:]
            # filename=f
            if ShowFileSize:
                print size,"\t", filename
            else:
                print filename
            nfiles+=1

    print "\n Number of files in directory: ",nfiles,"\n"


    
