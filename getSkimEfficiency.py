#!/usr/bin/python
#
import sys,string,math,os,commands
from optparse import OptionParser

GREP="grep"
searchString="skimL1Algos"
logfiles="*.stdout"

def usage():
    """
 Get the skim Efficiency from the logfiles created during a crab job.
 Program parses the *.stdout files in <logDirectory> to extract the totals
 Type -h to get full options
    """
    pass

def getCount(input,iele):

    xx=string.rstrip(input)
    inputLine=xx.split()    
    return int(inputLine[iele])
        
if __name__ == '__main__':


    narg=len(sys.argv)
    if narg < 2 :
        print usage.__doc__
        sys.exit(1)

    usage = "usage: %prog [options] <logDirectory>" + "\n" + usage.__doc__
    verbose=False
    parser = OptionParser(usage=usage)
    parser.add_option("-v","--verbose",
                      action="store_true",dest="verbose",default=False,
                      help="be verbose, default=false")

    (options, args) = parser.parse_args()
    # searchDirectory=sys.argv[1]
    searchDirectory=args[0]
    verbose=options.verbose

    logfiles=os.path.join(searchDirectory,logfiles)
    grepArgs=string.join([searchString,logfiles])
    grepArgs=string.join([grepArgs," | grep -v TimeReport"])
    grepArgs=string.join([grepArgs," | grep -v Modules"])
    myargs=string.join([GREP,grepArgs])
    print "\n",myargs
    xx=commands.getoutput(myargs)
    # print xx

    TotalSkimEvents=0
    TotalEvents=0
    skimCounts=xx.split("\n")
    if skimCounts[0].find("No such file or directory")>-1:
        print "\nTrouble with grep command. Check input directory"
        sys.exit(1)
    # print "xxx ",len(skimCounts),skimCounts

    for Counts in skimCounts:
        if (verbose): print Counts

       # iele=4  # Number of skimmed events
       # iele=3  # Total Number of events
        skimmedEvents=getCount(Counts,4)
        Events=getCount(Counts,3)
        if (verbose):
            print skimmedEvents, Events
        TotalSkimEvents=TotalSkimEvents+skimmedEvents
        TotalEvents=TotalEvents+Events

    print "\n"
    print "Total number of Skimmed Events:  ", TotalSkimEvents
    print "Total number of Events Processed: ", TotalEvents
    print "\n"
    print "Skim Efficiency: ", float(TotalSkimEvents)/TotalEvents
