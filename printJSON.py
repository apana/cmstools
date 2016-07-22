#!/usr/bin/python
#
#------------JSON-------------
title = 'printJSON'

import os, string,sys, json
import pprint

debug=False

def usage():
    """ Usage: printJSON file
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

    inputJSON=sys.argv[1]
    infile=OpenFile(inputJSON,'r')

    data = json.load(infile)
    if debug:
        print(json.dumps(data, sort_keys=True, indent=4))

    runs=[]
    for idat in data:
        if debug:
            print idat,type(idat)
        
        runnumber=int(idat.encode("ascii"))
        runs.append(runnumber)

    sortedruns=sorted(runs)
    print "\nNumber of runs in JSON file: ",len(runs)
    # print runs

    if debug:
        print sortedruns
        
    outstring="Runs: "
    for irun in sortedruns:
        outstring =outstring + str(irun) + ", "

    print outstring[:-2]
    ## print data.keys()
    
    ## pprint(data)
    
    ## CloseFile(infile)
   
