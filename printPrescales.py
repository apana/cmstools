#!/usr/bin/python
#

import sys,string

FLAG="TRIGGER NAME"

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

if __name__ == "__main__":

    narg=len(sys.argv)
    if narg < 2 :
        print usage.__doc__
        sys.exit(1)

    file1=sys.argv[1]

    ifile=OpenFile(file1,'r')
    contents = ifile.readlines()
    ifile.close()
    count=0
    iline=-1
    for line in contents:
        iline=iline+1
        l=line.strip()
        # print l
        indx=string.find(l,FLAG)
        if (indx>-1): count=count+1
        if (count == 2): break
    prescaleLine=contents[iline+2]
    xx=string.split(prescaleLine)
    print xx[1],xx[3]
    
    
    

    
