#!/usr/bin/python
#

import sys,string,time,os,commands

from myUtils import *

def usage():
    """ Usage: pyRemove listOfFiles <directory>
    
    Removes files from list. If no directory is given, files are assumed to reside in current directory
    """
    pass

if __name__ == '__main__':

    narg=len(sys.argv)
    if narg < 2:
        print usage.__doc__
        sys.exit(1)

    infile=sys.argv[1]
    addDir=False
    Basename="."
    if narg>2:
        addDir=True
        BaseName=sys.argv[2]

    if addDir:
        print "Adding Dir: ",BaseName
        if not os.path.isdir(BaseName):
            print "Requested directory does not exist -- check name"
            sys.exit(1)

    files=getFileList(infile)
    print len(files)
    for ifile in files:
        filename=ifile
        if addDir:
            filename=os.path.join(BaseName,ifile)
        print "removing ",filename
        if os.path.exists(filename):
            os.remove(filename)



