#!/usr/bin/python
#


CONV=1e-36 #  conversion from pb to cm^2
MicroToPico=1e-6
LumiLength=23.3

if __name__ == "__main__":

    xsval=0.
    OrgL1  = float(raw_input("\t   Enter original L1 PS: "))
    NewL1  = float(raw_input("\t   Enter new L1 PS: "))
    #OrgL1=600
    #NewL1=2400
    #print "\nOriginal L1: ", OrgL1, "\tNew L1: ",NewL1
    
    OrgHLT = float(raw_input("\t   Enter original HLT PS: "))
    

    
    NewHLT = OrgL1*OrgHLT/NewL1

    print "\nOriginal L1: ", OrgL1
    print "Original HLT: ", OrgHLT
    
    print "\nNew HLT PS is: ", NewHLT
    print "\n"
