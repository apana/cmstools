#!/usr/bin/python
#

import sys,string,time,os

from optparse import OptionParser

# oldStyle=False

StringToFind="/pnfs/cms/WAX"
ReplacementString="dcap://cmsdca.fnal.gov:24136/pnfs/fnal.gov/usr/cms/WAX"

# StringToFind="/pnfs/cms/WAX/11"
# ReplacementString=""

def usage():
    """ Usage: returndCacheName <FileName>
    use -q to add quotations around filenames
    """
    pass

def getdCacheName(infile):

    indx=infile.find(StringToFind)
    if indx<0:
        print "Problem with input filename"
        sys.exit(1)

    if oldStyle:
        dName=infile.replace(StringToFind, ReplacementString)
    else:
        dName="dcache:" + infile

    if showQuotes:
        dName="\t\"" + dName +"\","

    return dName

if __name__ == '__main__':


    narg=len(sys.argv)
    if narg < 2 :
        print usage.__doc__
        sys.exit(1)

    parser = OptionParser()

    parser.add_option("-q","--quotes",
                      action="store_true", dest="showQuotes", default=False,
                      help="Put quotations around filenames")

    parser.add_option("-o","--oldstyle",
                      action="store_true", dest="oldStyle", default=False,
                      help="Return old style of PFN")
   
    (options, args) = parser.parse_args()

    showQuotes=options.showQuotes
    oldStyle=options.oldStyle
    ARGS=args
    # print ARGS


    FILE=ARGS[0]
    isDIR=os.path.isdir(FILE)

    # print "\n"
    if isDIR:
        files=os.listdir(FILE)
        for file in files:
            inFILE=os.path.join(FILE,file)
            if (inFILE.find(".root") > -1):
                print getdCacheName(inFILE)
    else:
        if os.path.isfile(FILE):
            print getdCacheName(FILE)
        else:
            print "Problem with input"
    
