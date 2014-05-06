#!/usr/bin/python
#

import sys,string,time,os,math


def usage():
    """ Usage: ptMapping <corrPt>
    """
    pass

def Response(x):

    a=0.976811
    b=14.2444
    c=4.47607
    d=18.482
    e=0.717231
    
    val=a-b/(math.pow(math.log10(x),c)+d)+e/x
    
    return val

if __name__ == '__main__':


    narg=len(sys.argv)
    if narg < 2 :
        print usage.__doc__
        sys.exit(1)

    corPt=float(sys.argv[1])
    #print corPt
    r=Response(corPt)
    Pt=corPt*r
    #print Pt

    print "Corrected jet Pt = ", corPt," GeV, Response = ",r,", Uncorrected jet Pt = ",Pt," GeV"
