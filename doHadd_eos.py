#!/usr/bin/python
#
import sys,string,math,os,subprocess,socket

Location="FNAL"

Debug=False
## Debug=True

SUFFIX=".root"

def usage():
    """ Usage: python doHadd <Target> <SourceDir>
    hadd all files in eos directory <SourceDir> with suffix .root
    """
    pass

def GetFiles(Dir):

    return

if __name__ == '__main__':

    narg=len(sys.argv)
    if narg < 3 :
        print usage.__doc__
        sys.exit(1)

    cwd=os.getcwd()
    
    print "\n Machine:", socket.gethostname(),"\tCurrent directory: ",cwd

    TARGET=sys.argv[1]
    INDIR=sys.argv[2]
    os.chdir(INDIR)

    dir="."
    filelist=os.listdir(dir)
    rootlist=[]
    for rfile in filelist:
        indx=string.find(rfile,SUFFIX)
        if indx>-1:
            if Location == 'FNAL':
                Prepend="root://cmsxrootd.fnal.gov/"
                theFile=os.path.join(INDIR,rfile)
                theFile=theFile.replace("/eos/uscms",Prepend)
            else:
                print "Not yet setup for this location"
                sys.exit(1)
                
            rootlist.append(theFile)

    # print rootlist
    infiles=''
    for ifile in rootlist:
        infiles=infiles + " " + ifile
    ## print infiles
    os.chdir(cwd)

    ##p = subprocess.Popen(["hadd",target,infiles], shell=False)  ## doesn't seem to work anymore
    ##sts = os.waitpid(p.pid, 0)[1]
    
    myargs=string.join(["hadd",TARGET])
    myargs=string.join([myargs,infiles])
    print myargs
    os.system(myargs)
    
    

    

    
    
