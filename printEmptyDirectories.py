#!/usr/bin/python
#

import sys,string,time,os,commands

from myUtils import *

def usage():
    """ Usage: pyRemove listOfFiles <directory>
    
    Removes files from list. If no directory is given, files are assumed to reside in current directory
    """
    pass

def getFileList(infile):

    import string

    filelist=[]
    ifile=OpenFile(infile,"r")
    x = ifile.readline()
    while x != "":
        xx=string.rstrip(x)

        z=string.split(xx)
        if len(z) != 2:
            print z
        else:
            fsize=int(z[0])
            if fsize<10:
                filelist.append(z[1])
                
        x = ifile.readline()            

    CloseFile(ifile)
    return filelist

if __name__ == '__main__':

    narg=len(sys.argv)
    if narg < 2:
        print usage.__doc__
        sys.exit(1)

    infile=sys.argv[1]

    files=getFileList(infile)
    print len(files)

    for ifile in files:
        filename=os.path.join("/pnfs/cms/WAX/11/store/user/lpchbb/apana",ifile)
        if not os.path.exists(filename):
            print filename
        
        os.rmdir(filename)



