import sys,string,os.path
from ROOT import gROOT, gStyle, gSystem, TCanvas, TF1, TFile, TH1F

def usage():
    """ Usage: printLeaves <rootFile> <treeName>
    
 Printout the leaves on <rootfile>
    """
    pass


if __name__ == '__main__':

    narg=len(sys.argv)
    if narg < 2 :
        print usage.__doc__
        sys.exit(1)
        
    rootfile=sys.argv[1]
    print "Rootfile: ",rootfile
    _file0=TFile.Open(rootfile)

    # print _file0

    ## treeName="HltTree"
    treeName="Events"
    if narg == 3:
        treeName=sys.argv[2]
    
    print "Tree name: :",treeName
    ## _file0.ls()
    tree = _file0.Get(treeName);
    leaves = tree.GetListOfBranches();
    # leafEnts=leaves.GetSize();
    leafEnts=leaves.GetEntries();
    print "\nNumber of leaves: ", leafEnts
    for i in range(0,leafEnts):
        leafName = leaves[i].GetName();
        print "\t",leafName
    print "\nNumber of events on tree: ",tree.GetEntries()
