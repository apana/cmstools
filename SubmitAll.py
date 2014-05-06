#! /usr/bin/env python

import os,sys,string

def usage():
    """ Usage: SubmitAll <cfg> <dir>
    dir contains the python cmsRun scripts
    """
    pass

if __name__ == '__main__':

    narg=len(sys.argv)
    if narg < 3 :
        print usage.__doc__
        sys.exit(1)

    cfgFile=sys.argv[1]
    directory=sys.argv[2]
    condorfiles=os.listdir(directory)

    CondorBase="CondorJob_" + cfgFile[0:-3] + "_"
    print CondorBase
    
    for file in condorfiles:
        indx=string.find(file,CondorBase)
        if (indx == 0):

            command =  "condor_submit " + os.path.join(directory,file)
            print command
            # os.system(command)

