#!/usr/bin/python
#

import sys,string,math,os,subprocess,socket

EOS = "/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select"

Debug=False
# Debug=True

def listFiles(inDir):

    dirs=[]
    files=getFiles(EOS,"ls",inDir)
    for ifile in files:
        theFile=os.path.join(inDir,ifile)
        isDir=getFileType(EOS,"stat",theFile)
        if isDir:
            print "d: ",theFile
            dirs.append(theFile)
        else:
            pass
            # print "x: ",theFile
    return dirs

def runPopen(command,subcommand,inDir):
    p1 = subprocess.Popen([command, subcommand, inDir], shell=False, stdout=subprocess.PIPE)
    (stdout, stderr)=p1.communicate()
    if stderr is not None:
        print "Trouble executing the srmls command"
        sys.exit(1)

    ## if Debug:
    ##     print "Raw output"
    ##     print stdout
    ##     print "Done\n"

    return (stdout,stderr)

def getFiles(eos,command,inDir):
    
    (stdout, stderr)=runPopen(eos,command,inDir)

    tmpfiles=stdout.split('\n')
    files=[]
    for tfile in tmpfiles:
        if len(tfile)>0:
            files.append(tfile)
            
    if Debug:
        print "\n Number of files in Directory: ",len(files),"\n"
        print files

    return files

def getFileType(eos,command,inDir):

    isDir=False
    
    (stdout, stderr)=runPopen(eos,command,inDir)
    output=stdout.split(' ')
    # if Debug: print len(output),output

    if output[4].find("directory")>-1 and output[3].find("failed")==-1 and output[3].find("log")==-1:
        if Debug: print len(output),output        
        isDir=True
        
    return isDir

if __name__ == '__main__':

    narg=len(sys.argv)
    if narg != 2:
        print "Please specify EOS directory"
        sys.exit(1)
       
    inDir=sys.argv[1]   
    print inDir
        
    while True:
        dirs=listFiles(inDir)
        ## print dirs
        if len(dirs)==0:
            break
        else:
            inDir=os.path.join(inDir,dirs[0])

