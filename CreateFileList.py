#!/usr/bin/python
#

import sys,string,time,os

MAXFILES=-1
FilesPerCfg=12
# CFGBASE="MinBias_StartupV5_GENSIMRAW_212_"
# CFGBASE="Monitor_Commissioning09-v1_RAW_Run82548_"
CFGBASE="ZeroBiasSkim_beginLS"

# fix for dealing with dCache files
stringtoReplace   = "/pnfs/cms/WAX/"
replacementString = "dcap://cmsdca.fnal.gov:24136/pnfs/fnal.gov/usr/cms/WAX/"


def usage():
    """ Usage: CreateFileList <FileList> <OutputDir>
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

def ReadFile(file):

    
    infile=OpenFile(file,'r')
    iline=0

    x = infile.readline()

    files=[]
    while x != "":
        iline+=1
        xx=string.strip(x)
        if (len(xx)>0):
            files.append(xx)
                    
        x = infile.readline() 
    CloseFile(infile)

    return files

def createCFG(i,filelist, CFGBASE):

    # add underscore if missing
    if CFGBASE[len(CFGBASE)-1] != "_":
        CFGBASE = CFGBASE + "_"  
    
    CFGFILE=CFGBASE + str(i) +".py"
    print i, CFGFILE
    file = open(CFGFILE,'w')
    file.write("import FWCore.ParameterSet.Config as cms \n")
    file.write("\n")
    file.write("maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )\n")
    file.write("readFiles = cms.untracked.vstring()\n")
    file.write("secFiles = cms.untracked.vstring()\n")        
    file.write("source = cms.Source (\"PoolSource\",fileNames = readFiles, secondaryFileNames = secFiles)\n")        
    file.write("readFiles.extend( [\n")
    
    i=0
    for infile in filelist:
       i=i+1

       if infile.find(stringtoReplace) >-1:
           infile=infile.replace(stringtoReplace,replacementString)
           
       if i<len(filelist):
           endstr="',"
       else:
           endstr="' ]);"
       outstring="    " + "'" + infile + endstr
       file.write(outstring + "\n")

    file.write("\n")            
    file.write("secFiles.extend( [ ])\n")        
    CloseFile(file)
    
if __name__ == '__main__':


    narg=len(sys.argv)
    if narg < 3 :
        print usage.__doc__
        sys.exit(1)


    InputFile=sys.argv[1]
    OutputDir=sys.argv[2]
    if not os.path.exists(OutputDir):
        print "Output directory does not exist. Creating: ", OutputDir
        os.mkdir(OutputDir)
        
    
    filelist = ReadFile(InputFile)
    print "\nNumber of input files: ", len(filelist)
    if ( MAXFILES>0 ): print "\n processing first ", MAXFILES, " in list"
    print "Creating filelists with ", FilesPerCfg, "files per filelist\n"

    os.chdir(OutputDir)
    
    i=0
    ibatch=0
    cfglist=[]
    if (MAXFILES < 0): MAXFILES=100000
    for ifile in filelist:
        i=i+1
        if (i>MAXFILES): break
        filename=ifile
        cfglist.append(filename)
        if i%FilesPerCfg == 0:
            createCFG(ibatch,cfglist,CFGBASE)
            ibatch=ibatch+1
            cfglist=[]
        if (i == len(filelist) and len(cfglist)>0): # get the last batch
            createCFG(ibatch,cfglist)
        #print i%FilesPerCfg, i, filename

    print "\n"
