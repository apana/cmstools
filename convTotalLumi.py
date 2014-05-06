#!/usr/bin/python
#


CONV=1e-36 #  conversion from pb to cm^2
## MicroToPico=1e-6
LumiLength=23.3

if __name__ == "__main__":

    xsval=0.
    print "Enter Lumi in micro barns"
    # totalLumi=float(raw_input("\t   Enter total Lumi in microbarns: "))
    totalLumi=float(raw_input("\t   Enter total Lumi in picobarns: "))
    
    beginLumi = int(raw_input("Please enter first lumi section: "))
    endLumi = int(raw_input("Please enter first last section: "))
    
    nLumi=endLumi-beginLumi+1
    # instLumi=totalLumi*MicroToPico/(CONV*nLumi*LumiLength)
    instLumi=totalLumi/(CONV*nLumi*LumiLength)
    print "\nAverage instantaneous luminosity over ",nLumi," lumisections is: ", instLumi, " cm**2/s"
    print "\n"

