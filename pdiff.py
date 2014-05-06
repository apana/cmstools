#!/usr/bin/env python

import string,sys,math

if __name__ == "__main__":

    narg=len(sys.argv)
    print narg
    if narg != 3 and narg !=5 :
        print "Please supply 2 ( a and b) or 4 ( a +- da, b+- db) numbers"
        sys.exit(1)

    if (narg == 2):
        a =float(sys.argv[1])
        b =float(sys.argv[2])
    else:
        a =float(sys.argv[1])
        da=float(sys.argv[2])

        b =float(sys.argv[3])
        db=float(sys.argv[4])

    d=(b-a)/a
    dd=d*math.sqrt( math.pow(da/a,2) + math.pow(db/b,2) )
    
    d=d*100.
    dd=dd*100.
    begstring=str(a) + " " + str(b) + "  diff: "
    outstring1=begstring + "%.2f +- %.2f" % (d, dd)
    outstring2=begstring + "%.1f +- %.1f" % (d, dd)
    print outstring1
    print outstring2

        

