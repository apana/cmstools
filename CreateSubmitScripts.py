#!/usr/bin/python
#

import sys,string,time,os,getpass

def usage():
    """ Usage: CreateSubmitScripts <cfg> <dir>
    dir contains the python cmsRun scripts
    """
    pass

def createRunScript(absDir,absLogs,file):

    outScript="run" + string.replace(file,".py",".csh")
    outLog="run" + string.replace(file,".py",".log")

    inScript=os.path.join(absDir,file)
    outScript=os.path.join(absDir,outScript)
    outLog=os.path.join(absLogs,outLog)

    oFile = open(outScript,'w')
    oFile.write("#!/bin/tcsh" + "\n")
    oFile.write("\n")    
    oFile.write("source /uscmst1/prod/sw/cms/setup/cshrc prod" + "\n")
    oFile.write("cd " + absDir + "\n")
    oFile.write("eval `scram runtime -csh`" +  "\n")
    oFile.write("\n")
    oFile.write("cmsRun " + inScript + " >& "  + outLog + "\n")    
    oFile.write("date" + "\n")
    
    oFile.close()

    condorOutScript="CondorJob_" + string.replace(file,".py","")
    condorLogs=string.replace(file,".py","_")
    
    condorOutScript=os.path.join(absDir,condorOutScript)
    condorLogs=os.path.join(absLogs,condorLogs)
    
    oFile = open(condorOutScript,'w')
    
    oFile.write("universe = vanilla" + "\n")
    oFile.write("Executable = " + outScript + "\n")
    oFile.write("Requirements = Memory >= 199 &&OpSys == \"LINUX\"&& (Arch != \"DUMMY\" )" + "\n")
    oFile.write("Should_Transfer_Files = YES" + "\n")
    oFile.write("WhenTOTransferOutput  = ON_EXIT" + "\n")
    oFile.write("Output = " + condorLogs + "$(Cluster).stdout" + "\n")
    oFile.write("Error =" + condorLogs + "$(Cluster).stderr" + "\n")
    oFile.write("Log = " + condorLogs + "$(Cluster).condorlog" + "\n")
    mailAddress=getpass.getuser()+ "@FNAL.GOV"
    oFile.write("notify_user = " + mailAddress  + "\n")
    oFile.write("Queue 1" + "\n")

    oFile.close()
    

    
    return

if __name__ == '__main__':

    narg=len(sys.argv)
    if narg < 3 :
        print usage.__doc__
        sys.exit(1)

    cfgFile=sys.argv[1]
    directory=sys.argv[2]
    
    absDir= os.path.abspath(directory)
    if not os.path.exists(absDir):
        os.mkdir(absDir)

    absLogs=absDir

    cfgBase=cfgFile[0:-3] + "_"
    # print cfgBase

    cfgfiles=os.listdir(directory)
    for file in cfgfiles:
        indx=string.find(file,cfgBase)
        if (indx == 0):
            createRunScript(absDir,absLogs,file)

        
