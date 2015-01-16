#!/usr/bin/python


Lumi=1.41e34 ## instantaneous lumi (Hz/s^2)
Sigma=80. ## inelastic cross section (mb)
freq=11245  ##  revolution frequency (s-1)
nBunches=2508 ## number of bunches

#### conversion factors

CONV=1e-36 #  conversion from pb to cm^2
MicroToPico=1e-6
MilliToPico=1e-9
if __name__ == '__main__':

    Sigma = Sigma*CONV/MilliToPico

    PU=Sigma*Lumi/(freq*nBunches)
    print "Average PU for L= ", Lumi," is: ",PU

    
