#!/usr/bin/python
#
import sys,string,math,os

def usage():
    """ Usage: mkOpenHLTmenu.py
    Reads in list of HLT paths and output list of paths suitable for RateEff macros
    outfile is optional
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

    pathlist=[]
    while x != "":
        iline+=1
        xx=string.strip(x)
        pathlist.append(xx)
        
        x = infile.readline() 
    CloseFile(infile)
    return pathlist


if __name__ == '__main__':


    narg=len(sys.argv)
    if narg < 2 :
        print usage.__doc__
        sys.exit(1)

    InputFile=sys.argv[1]    
    pathlist=ReadFile(InputFile)
    
    OUTPUTFILE="hltnames.dat"
    ifile=OpenFile(OUTPUTFILE,"w")

    ifile.write(" triggers = (" + "\n")

    
    for path in pathlist:
        print path
        out_string="  (\"" + path 
        out_string=out_string + "\",\t\"OpenL1_ZeroBias" + "\",\t"
        out_string=out_string + "1, 0.15),"
        ifile.write(out_string + "\n")

        
    ifile.write(" );" + "\n")
    CloseFile(ifile)
