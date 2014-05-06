#!/usr/bin/python
#

import sys,string,time,os

istart=0
# NFILES=81
NFILES=23
INPUTSTARTSWITH="INPUTFILELIST="
COMMENTLINE="#"

searchInput="xxx"

OUTPUTSTARTSWITH="OUTPUTHIST="
searchOutput=".root"

def usage():
    """ Usage: CreateCFGS <cmsCFGFile> <outputDir>
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

def createNewFile(i,orgFile,basename,dir):

    newFile=basename + "_" + str(i) + ".py"
    newFile=os.path.join(dir,newFile)
    print newFile
    outFile = open(newFile,'w')
    
    for iline in orgFile:
        if len(iline)>0  and iline[0]!=COMMENTLINE:            
            indx=string.find(iline,INPUTSTARTSWITH)
            if (indx == 0):
                indx2=string.find(iline,searchInput)
                if (indx2 < 0):
                    print "Problem finding line beginning with: ", INPUTSTARTSWITH
                    sys.exit(1)
                else:
                    iline=string.replace(iline,searchInput,str(i))

            indx=string.find(iline,OUTPUTSTARTSWITH)
            if (indx == 0):
                indx2=string.find(iline,searchOutput)
                if (indx2 < 0):
                    print "Problem"
                    sys.exit(1)
                else:
                    replString="_" + str(i) + searchOutput
                    iline=string.replace(iline,searchOutput,replString)

        outFile.write(iline + "\n")
    CloseFile(outFile)
    
    return

def ReadFile(file):
    
    infile=OpenFile(file,'r')
    iline=0
    
    x = infile.readline()

    file=[]
    while x != "":
        iline+=1
        xx=string.rstrip(x)
        file.append(xx)        
        x = infile.readline()
        
    CloseFile(infile)

    return file

    
if __name__ == '__main__':


    narg=len(sys.argv)
    if narg < 3 :
        print usage.__doc__
        sys.exit(1)


    InputFile=sys.argv[1]
    basename=string.replace(InputFile,".py","")
    
    OutputDir=sys.argv[2]
    if not os.path.exists(OutputDir):
        os.mkdir(OutputDir)
                
    infile=ReadFile(InputFile)

    for i in range(istart,istart+NFILES):
        # print i
        createNewFile(i,infile,basename,OutputDir)
        
