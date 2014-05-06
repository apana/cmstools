#! /usr/bin/env python

import os,sys,string

BATCHQUEUE = "cmscaf"
CFGBASE = "HLT_cff_batch_"
SubmitScript="toBatch.sh"

def usage():
    """ Usage: SubmitAll <dir>
    dir contains the python cmsRun scripts
    """
    pass

if __name__ == '__main__':

    narg=len(sys.argv)
    if narg < 2 :
        print usage.__doc__
        sys.exit(1)
    
    directory=sys.argv[1]
    condorfiles=os.listdir(directory)
    
    for file in condorfiles:
        indx=string.find(file,CFGBASE)
        if (indx == 0):

            command =  "bsub -q " + BATCHQUEUE + " SubmitScript " + os.path.join(directory,file)
            print command
            # os.system(command)

