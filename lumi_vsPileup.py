#!/usr/bin/python


PU=40.0
Sigma=80. ## inelastic cross section (mb)
## Sigma=69.3
freq=11245  ##  revolution frequency (s-1)
## nBunches=2508 ## number of bunches expected for 25nb bunch spacing
nBunches=1368

#### conversion factors

CONV=1e-36 #  conversion from pb to cm^2
MicroToPico=1e-6
MilliToPico=1e-9

if __name__ == '__main__':

    Sigma = Sigma*CONV/MilliToPico

    Lumi=PU*freq*nBunches/Sigma

    print "Instantanous lumi for PU= ", PU," is: ",Lumi

    
