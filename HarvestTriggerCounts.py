#!/usr/bin/env python

import os, string, sys, posix, tokenize, array, getopt, math

ApplyPrescales=True
FirstPath="HLT_Activity_Ecal_SC7_v3"
Index=2

# RUNID=163592
RUNID=163374
TargetLumi=1e33

if RUNID==163592:
    # run 163592
    Lumi=4.43806954425e+32
    HLT_Physics_Prescl=3500.
    totalLumi=(106-2)
elif RUNID==163374:
    # run 163374
    Lumi=3.2154e+32
    HLT_Physics_Prescl=3500.
    totalLumi=(670-2)
else:
    print "Not ready for validating run ",RUNID
    sys.exit(1)

LumiScaleFactor=TargetLumi/Lumi
# LumiScaleFactor=1.

PreList=[1,1,1,1,1,1,1,1,1,1,1]

def main(argv):

    numjobs = 0

    logdir="logs"
    if (len(argv)>1):
        logdir=argv[0]
        hltmenu=argv[1]
    else:
        print "Please supply logdir and hltmenu"
        sys.exit(1)
        
    curdir=os.getcwd()
    dirs = os.listdir(curdir)

    hlttrigreportnames = []
    hlttrigreportcounts = []
    l1trigreportnames = []
    l1trigreportcounts = []
    totalevents = 0
    totalhltrateevents = 0
    MenuName=GetMenuName(hltmenu)
    
    PrescaleDict=GetPrescales(hltmenu)
    
    
    myscale=HLT_Physics_Prescl*LumiScaleFactor/(totalLumi*23.3)

    # scaledtime = 1.0;
    #    scaledtime = (99524.0 / 50000.0);
    #  scaledtime = (1406.25/583.2764); # Roberto - normalized to Mu5, run 161312
    # scaledtime = (1406.25/1160.2764); # Roberto - normalized to Mu5, run 161312
    # scaledtime = (79.646/????); # LA - normalized to IsoMu12, run 161311


    scaledtime=1./myscale

    dirname=os.path.join(curdir,logdir)
    if os.path.isdir(dirname):
        thefiles = os.listdir(dirname)
        for thefile in thefiles:
            if(thefile.endswith("stdout")):
               print "Opening ",thefile
               outfile = open(os.path.join(dirname,thefile))

               startedhlt = False
               finishedhlt = False
               startedl1 = False
               finishedl1 = False
               
               lines = outfile.readlines()
               for line in lines:
                   if(line.find('TrigReport Events total = ') != -1):
                       # print "CCLA Found TrigReport Events total "
                       tempevline1 = (line.split(' = '))[1]
                       tempevline2 = (tempevline1.split('passed')[0]).lstrip().rstrip()
                       totalevents = totalevents + int(tempevline2)
                       tempevline1 = (line.split(' = '))[2]
                       tempevline2 = (tempevline1.split('failed')[0]).lstrip().rstrip()
                       totalhltrateevents = totalhltrateevents + int(tempevline2)
                    
                   # HLT
                   # FirstPath="HLTriggerFirstPath"
                   if(line.find('TrigReport') != -1 and line.find(FirstPath) != -1 and finishedhlt == False):
                       # print "CCLA Started"
                       startedhlt = True
                       finishedhlt = False
                   if(line.find('HLTriggerFinalPath') != -1 and startedhlt == True):
                       startedhlt = False
                       finishedhlt = True
                   if(startedhlt == True and finishedhlt == False and line.find('Summary') == -1):
                       hltreport = line.split()
                       hltrun = hltreport[3]
                       hltpassed = hltreport[4]
                       hltname = hltreport[7]

                       alreadyfound = False
                       hltcount = 0
                       for hlttrig in hlttrigreportnames:
                           if hlttrig == hltname:
                               alreadyfound = True
                               hlttrigreportcounts[hltcount] = hlttrigreportcounts[hltcount] + int(hltpassed)
                           hltcount = hltcount + 1
                            
                       if alreadyfound == False:
                           hlttrigreportnames.append(str(hltname))
                           hlttrigreportcounts.append(int(hltpassed))
                        
               outfile.close()

    for hltreportone in hlttrigreportnames:
        if not PrescaleDict.has_key(hltreportone): PrescaleDict[hltreportone]=PreList
        
    print '\n'
    print '======================================================================================================================================='
    print '\n'

    print 'Run: ',RUNID,'  Lumi: ',Lumi
    print 'Target Lumi: ',TargetLumi
    print 'Menu: ', MenuName
    print 'Using prescale index:',Index,'\n'

    print 'Total number of analyzed events = ' + str(totalevents)
    print "Number of trigger paths: ", len(hlttrigreportnames)
    print '\n'
    print '======================================================================================================================================='
    print str('HLT path').ljust(50) + "\t" + str('Passing events').ljust(30) + "\t" + str('Scaled HLT rate (Hz)').ljust(30)
    print '======================================================================================================================================='

    i = 0
    for hltreportone in hlttrigreportnames:
        hltrate = hlttrigreportcounts[i] / scaledtime
        errRate= math.sqrt(hlttrigreportcounts[i]) / scaledtime
        ljust=50
        if ApplyPrescales:
            chpre="1"
            if PrescaleDict.has_key(hlttrigreportnames[i]):
                thePrescale=int(PrescaleDict[hlttrigreportnames[i]][Index])
                chpre=str(thePrescale)
                # special cases
                if (hlttrigreportnames[i]=="HLT_L1SingleJet16_v2" or hlttrigreportnames[i]=="HLT_L1SingleJet36_v2" or
                    hlttrigreportnames[i]=="HLT_Jet30_v3" or hlttrigreportnames[i]=="HLT_Jet60_v3" or
                    hlttrigreportnames[i]=="HLT_DiJetAve30_v3" or hlttrigreportnames[i]=="HLT_DiJetAve60_v3" or
                    hlttrigreportnames[i]=="HLT_ZeroBias_v3" or hlttrigreportnames[i]=="HLT_L1Tech_BSC_minBias_threshold1_v4" or
                    hlttrigreportnames[i]=="HLT_L1_PreCollisions_v2" or hlttrigreportnames[i]=="HLT_L1_Interbunch_BSC_v2" or
                    hlttrigreportnames[i]=="HLT_BeamGas_HF_v4HLT" or hlttrigreportnames[i]=="HLT_BeamGas_BSC_v3" or 
                    hlttrigreportnames[i]=="HLT_ExclDiJet60_HFOR_v3" or hlttrigreportnames[i]=="HLT_BeamHalo_v3" or
                    hlttrigreportnames[i]=="HLT_Mu3_v5" or hlttrigreportnames[i]=="HLT_Mu3_DiJet30_v1" or
                    hlttrigreportnames[i]=="HLT_Mu3_TriJet30_v1" or hlttrigreportnames[i]=="HLT_Mu3_QuadJet30_v1" or 
                    hlttrigreportnames[i]=="HLT_Mu5_v5" or hlttrigreportnames[i]=="HLT_Mu5_Track2_Jpsi_v3" or
                    hlttrigreportnames[i]=="HLT_Mu8_v3" or hlttrigreportnames[i]=="HLT_Activity_Ecal_SC7_v3" or
                    hlttrigreportnames[i]=="HLT_DoubleEle8_CaloIdT_TrkIdVL_HT150_v2" or hlttrigreportnames[i]=="HLT_DoubleEle8_CaloIdL_TrkIdVL_HT150_v2"
                    ):
                    thePrescale=thePrescale*2
                    chpre=chpre+" * 2"
                elif (hlttrigreportnames[i]=="HLT_Ele8_v4" or hlttrigreportnames[i]=="HLT_Ele8_CaloIdL_TrkIdVL_v4" or
                      hlttrigreportnames[i]=="HLT_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL_v3" or hlttrigreportnames[i]=="HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v1" or
                      hlttrigreportnames[i]=="HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v1" or hlttrigreportnames[i]=="HLT_L1SingleEG5_v2" or
                      hlttrigreportnames[i]=="HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v1" or
                      hlttrigreportnames[i]=="HLT_Ele8_CaloIdL_CaloIsoVL_Jet40_v4" or
                      hlttrigreportnames[i]=="HLT_Ele8_CaloIdL_CaloIsoVL_v4" or
                      hlttrigreportnames[i]=="HLT_Mu5_v5" or hlttrigreportnames[i]=="HLT_L1SingleMuOpen_v2" or
                      hlttrigreportnames[i]=="HLT_L1SingleMuOpen_DT_v2" or hlttrigreportnames[i]=="HLT_L1SingleMuOpen_AntiBPTX_v2"
                      ):
                    thePrescale=thePrescale*350
                    chpre=chpre+" * 350"
                elif (hlttrigreportnames[i]=="HLT_DiJet60_MET45_v3"):
                    thePrescale=thePrescale*20
                    chpre=chpre+" * 20"
                elif (hlttrigreportnames[i]=="HLT_JetE30_NoBPTX_v3" or hlttrigreportnames[i]=="HLT_JetE30_NoBPTX_NoHalo_v5" or
                      hlttrigreportnames[i]=="HLT_JetE30_NoBPTX3BX_NoHalo_v5"):
                    thePrescale=thePrescale*10
                    chpre=chpre+" * 10"
                elif (hlttrigreportnames[i]=="HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v3"):
                    thePrescale=thePrescale*4
                    chpre=chpre+" * 4"
                    
            else: # prescaled 1 in menu need prescale
                print "XXXXXXXXXXXXXXXXXXXXXXXXX You should not see be here XXXXXXXXXXXXXXXXXXXXX"
                sys.exit(1)
                    
            if (thePrescale==0):
                # print "Prescale 0: Skipping: ",hlttrigreportnames[i]
                thePrescale=1
                chpre="0"
            
            hltrate=hltrate/thePrescale
            errRate=errRate/thePrescale
            print str(hlttrigreportnames[i]).ljust(ljust) + "\t" + str(hlttrigreportcounts[i]).rjust(30) + "\t" + str("%.4f +- %.4f" % (hltrate,errRate)).rjust(20) + " (" + chpre + ")"
        else:
            print str(hlttrigreportnames[i]).ljust(ljust) + "\t" + str(hlttrigreportcounts[i]).rjust(30) + "\t" + str("%.4f +- %.4f" % (hltrate,errRate)).rjust(20)
        i = i + 1

    print '\n'
    print '======================================================================================================================================='
    print '\n'

    totalhltrate = totalhltrateevents / scaledtime
    print 'Total HLT rate' + str(" = %.2f" % totalhltrate).rjust(25)

def GetMenuName(hlt):

    thefile=hlt

    MenuName="xxx"
    infile = open(thefile)
    x = infile.readline()
    infile.close()

    Line1=x.split()
    # print len(Line1),Line1
    if len(Line1)==3:
        MenuName=Line1[1]
    else:
        print "Problem extracting menu name"
    return MenuName

def GetPrescales(hlt):

    thefile=hlt

    outfile = open(thefile)

    startedhlt = False
    finishedhlt = False
    
    lines = outfile.readlines()
    PrescaleDict={}
    hltname="xxx"
    for line in lines:
        if(line.find('prescaleTable = cms.VPSet(') != -1):
            # print "CCLA Found Beginning "
            startedhlt = True
        if(line.find('process.UpdaterService') != -1 and startedhlt == True):
            startedhlt = False
            finishedhlt = True
            # print "CCLA Found End "
        if(startedhlt == True and finishedhlt == False and line.find('cms.PSet(  pathName = ') != -1):
            i1=line.find("\"")
            i2=line.rfind("\"")
            hltname=line[i1+1:i2]
            # print hltname
        if(startedhlt == True and finishedhlt == False and line.find('prescales = cms.vuint32') != -1):
            i1=line.find("(")
            i2=line.find(")")
            prescales=line[i1+1:i2].split(",")
            # print prescales[3]
            PrescaleDict [hltname] = prescales
    outfile.close()

    # print PrescaleDict.keys
    # theKeys = PrescaleDict.keys ()
    # for i in range (len (theKeys) ):
    #     print theKeys[i], PrescaleDict[ theKeys[i] ]
        
    return PrescaleDict

if __name__ == "__main__":
    main(sys.argv[1:])
    
