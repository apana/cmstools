#!/usr/bin/python
#

import sys,string,time,os,subprocess


def usage():
    """ Usage: CreateFileList <InputDir>
    InputDir is directory containing root files. Script searches for .root files in directory
    """
    pass

def OpenFile(file_in,iodir):
    """  file_in -- Input file name
         iodir   -- 'r' readonly  'r+' read+write """
    try:
        ifile=open(file_in, iodir)
        # print "Opened file: ",file_in," iodir ",iodir
    except:
        print "Could not open file: ",file_in
        sys.exit(1)
    return ifile

def CloseFile(ifile):
    ifile.close()

def getFileList(Dir):

    filelist=[]

    if not os.path.isdir(Dir):
        print "Invalid input directory"
        sys.exit()
    localfiles=os.listdir(Dir)
    for f in localfiles:
        if f.find(".root")>-1:
            filelist.append(f)

    return filelist

def getFileListFromCastor(Dir):

    filelist=[]

    p1 = subprocess.Popen(["rfdir", Dir], shell=False, stdout=subprocess.PIPE)
    (stdout, stderr)=p1.communicate()
    if stderr is not None:
        print "Trouble listind directory"
        sys.exit(1)
    
    # print stdout
    files=stdout.split()
    # print "\n Number of files to copy: ",len(files),"\n"

    for f in files:
        if f.find(".root")>-1:
            filelist.append(f)

    return filelist

if __name__ == '__main__':


    narg=len(sys.argv)
    if narg < 2:
        print usage.__doc__
        sys.exit(1)


    InputDir=sys.argv[1]
    if InputDir.find("/castor")==0:
        filelist=getFileListFromCastor(InputDir)
    else:
        filelist=getFileList(InputDir)


    if len(filelist)==0:
        print "No root files found"
    else:
        print "inputFiles=["
        for f in filelist:
            outfile=os.path.join(InputDir,f)
            if outfile.find("/pnfs")==0:
                outfile="dcache:"+outfile
            elif outfile.find("/castor")==0:
                outfile="rfio:"+outfile
            outstring="\t\"" + outfile + "\","
            if f==filelist[len(filelist)-1]:
                outstring=outstring[:-1]
            print outstring
        print "]"



