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
    _file0=TFile(rootfile)
    
    treeName="HltTree"
    if narg == 3:
        rootTree=sys.argv[2]
    

    tree = _file0.Get(treeName);
    branches = tree.GetListOfBranches();
    leafEnts=branches.GetSize();
    print "\nNumber of branches: ", leafEnts
    for i in range(0,leafEnts):
        branchName = branches[i].GetName();
        if branchName.find("Prescl")>-1:
            print "\t",branchName,"\t",branches[i].GetEntry(0)
    print "\nNumber of events on tree: ",tree.GetEntries()
