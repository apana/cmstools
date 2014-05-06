#!/usr/bin/python
#
#------------JSON-------------
title = 'pyJSON'

import os, string,sys


def usage():
    """ Usage: pyJSON file
    Reads in JSON file and writes sorted run list to output
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

if __name__ == "__main__":

    narg=len(sys.argv)
    if narg < 2 :
        print usage.__doc__
        sys.exit(1)

    file1=sys.argv[1]

    infile=OpenFile(file1,'r')
    x = infile.readline()
    runs=[]
    nruns=0
    while x != "":
        xx=string.rstrip(x)
        # print xx
        fields=string.split(xx)
        # print fields, len(fields)
        for field in fields:
            if string.find(field,":")>-1:
                nruns=nruns+1
                # print field[:-1]
                if (nruns==1):
                    irun=int(field[2:-2])
                else:
                    irun=int(field[1:-2])
                # print irun
                runs.append(irun)
                
        x = infile.readline()
    CloseFile(infile)

    print "Number of Runs: ",nruns
    # runs=runs.sort()
    print "Sorted run list: ", sorted(runs)

    i=0
    run1=0
    run2=1000000
    for run in sorted(runs):
        if int(run)>=run1 and int(run)<=run2:
            i=i+1
            print i,run

