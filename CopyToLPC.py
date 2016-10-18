#!/usr/bin/env python
# encoding: utf-8

# File        : CopyToLPC.py
# Author      : Ben Wu
# Contact     : benwu@fnal.gov
# Date        : 2016 Apr 11
#
# Description :


import subprocess
import subprocess
from multiprocessing import Pool


# filename = "r275059_itgv63p1.list"
# filename = "r275064_itgv63p1.list"
# filename = "r279931_v86SK.list"
filename = "279931_ParkingZeroBias.list"
# filename = "testing.list"

newfile=filename + ".new"

def fwork(cmd):
    return subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    p = Pool(8)
    cmdlist = []
    # f = open("r259721_itgv46p0_local.list", "w")
    # with open("r259721_itgv46p0.list") as file:
    f = open(newfile, "w")
    with open("%s" % filename) as file:
        for line_ in file.readlines():
            line =line_.strip()
            print line
            ##newloc = line.replace("eoscms.cern.ch", "cmseos.fnal.gov")
            ##newloc = newloc.replace("dpg_trigger", "lpctrig")
            newloc = line.replace("cmseos.fnal.gov//eos/uscms","eoscms.cern.ch//eos/cms")
            newloc = newloc.replace("user/lpctrig/apana/L1Menu_2016","group/dpg_trigger/comm_trigger/L1Trigger/L1Menu2016")
            f.write(newloc+"\n")
            print newloc,"\n"
            cmdlist.append("xrdcp %s %s" % ( line, newloc ))
    f.close()
    ## print cmdlist
    print p.map(fwork, cmdlist)

