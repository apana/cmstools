#!/bin/python

EDMCONFIG="edmConfigFromDB --runNumber"

import sys,string,math,os, commands

def usage():
    """ Usage: getHLTMenu <run>
    print HLT menu corresponding to a given run number
    """
    pass

if __name__ == '__main__':

    narg=len(sys.argv)
    if narg < 2 :
        print usage.__doc__
        sys.exit(1)

    run=sys.argv[1]

    myargs=string.join([EDMCONFIG,run,"| head -1"])
    # print myargs
    xx=commands.getstatusoutput(myargs)
    
    returnVal= xx[0]
    # if returnVal==0 all is OK

    if (returnVal==0):
        returnString=xx[1]
        vals=returnString.split()
        print "\nHLT menu for run %s: %s\n" %(run,vals[1])
    else:
        print "Problem extracting menu for run ", run
        print "Is CMSSW setup?"
    
