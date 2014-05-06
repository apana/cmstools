#!/usr/bin/python
#


XS_7TeV_MinBias=7.126E10  # from Summer09 production
XS_10TeV_MinBias=7.528E10
XS_14TeV_MinBias=7.98E10
XS_900GeV_MinBias=5.241E10
XS_2TeV_MinBias=5.996E10

CONV=1e-36 #  conversion from pb to cm^2

if __name__ == "__main__":

    xsval=0.
    print "Enter input XS from list below"
    print "\t 1: pp @ 900 GeV"
    print "\t 2: pp @   2 TeV"
    print "\t 3: pp @   7 TeV"
    print "\t 4: pp @  14 TeV"
    print "\t 5: other\n"
    
    choice = int(raw_input("Please enter a number: "))
    if (choice == 1):
        xsval=XS_900GeV_MinBias
    elif (choice == 2):
        xsval=XS_2TeV_MinBias
    elif (choice == 3):
        xsval=XS_7TeV_MinBias
    elif (choice == 4):
        xsval=XS_14TeV_MinBias
    elif (choice == 5):
        print "\t  Enter XS in picobarns"
        xsval=float(raw_input("\t   Enter XS in picobarns: "))
        
    print "\tInput xs for choice ",choice,": ",xsval," pb\n"

    lumi = float(raw_input("Please enter luminosity (cm**2/s): "))
    print "\tInput lumiosity is: ", lumi
    
    rate=lumi*CONV*xsval
    print "\nInteraction rate is: ", rate, " Hz"
    print "\n"

