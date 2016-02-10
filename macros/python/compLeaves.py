import sys,string,math,os,ROOT
from ROOT import *

sys.path.append(os.path.join(os.environ.get("HOME"),'rootmacros'))
from myPyRootMacros  import *


## from PhysicsTools.PythonAnalysis import *
## from ROOT import *
## gSystem.Load("libFWCoreFWLite.so")
## AutoLibraryLoader.enable()

#===============================================================

logy=False

dist="et"; logy=True
## dist="phi"
## dist="eta"

nbins=25; xmin=0.0; xmax=2500.; ymax=0; ymin=0;

label1 = "file1";  object1="recoGenJets_"; module1="ak4GenJets_"; process1 = "_GEN";
label2 = "file2";  object2="recoGenJets_"; module2="ak4GenJets_"; process2 = "_GEN";

## fileNames1=["root://eoscms//eos/cms/store/cmst3/user/hinzmann/dijet_angular/jobtmp_pythia8_ci_m4300_13000_50000_1_0_0_13TeV_Oct1-1.root"]
## fileNames2=["root://eoscms//eos/cms/store/cmst3/user/hinzmann/dijet_angular/jobtmp_pythia8_ci_m4300_13000_50000_1_0_0_13TeV_Oct1-2.root"]

fileNames1=["root://eoscms//eos/cms/store/cmst3/user/hinzmann/dijet_angular/jobtmp_herwigpp_qcd_m4300_13000___Oct1-93.root"]
fileNames2=["root://eoscms//eos/cms/store/cmst3/user/hinzmann/dijet_angular/jobtmp_herwigpp_qcd_m4300_13000___Oct1-94.root"]


PrintPlot=False
# PrintPlot=True

#===============================================================

if __name__ == '__main__':

    SetStyle()
    gStyle.SetOptStat(110);
#===============================================================

    tree1=TChain("Events");
    i=0
    for f in fileNames1:
        i=i+1
        print i,f
        tree1.Add(f);

    print "\n"

    tree2=TChain("Events");
    i=0
    for f in fileNames2:
        i=i+1
        print i,f
        tree2.Add(f)


    branch1=object1+module1+process1+".obj."+dist+"()";   cut1="";
    branch2=object2+module2+process2+".obj."+dist+"()";   cut2="";

    print branch1
    print branch2

    h1 = TH1F("h1","h1",nbins,xmin,xmax);
    h2 = TH1F("h2","h2",nbins,xmin,xmax);
    
    tree1.Project(h1.GetName(),branch1)
    tree2.Project(h2.GetName(),branch2)

    if (ymax > 0.):
        h1.GetYaxis().SetRangeUser(ymin,ymax);
        h2.GetYaxis().SetRangeUser(ymin,ymax);

    print "h1: ",h1.GetEntries()
    print "h2: ",h2.GetEntries()

    # h1.Scale(1./h1.GetEntries())
    # h2.Scale(1./h2.GetEntries())

    c1,p1,p2 = prep1by2Plot("c1","c1",500)
    p1.Draw(); p2.Draw()

    p1.cd()
    p1.SetLogy(logy)

    SetHistColorAndMarker(h2,ROOT.kRed,20)    
    h1.SetLabelOffset(0.1, "X");
    ## h2.Scale(0.5)
    h1.Draw()
    h2.Draw("e,sames")

    xl1=.2; yl1=0.16; xl2=xl1+.2; yl2=yl1+.1;
    leg0=PrepLegend(xl1,yl1,xl2,yl2,0.03)
    leg0.AddEntry(h1,label1,"pl")
    leg0.AddEntry(h2,label2,"pl")
    leg0.Draw();

    DrawText(0.6,0.8,dist,0.04)
    gPad.Update();
    print h1.GetListOfFunctions()
    print h1.GetListOfFunctions().FindObject("stats")
    tt1=h1.GetFunction("stats");
    tt1.SetTextColor(h1.GetLineColor());
    tt2=h2.GetFunction("stats");
    tt2.SetTextColor(h2.GetLineColor());
    x1 = tt1.GetX1NDC();    y1 = tt1.GetY1NDC();
    x2 = tt1.GetX2NDC();    y2 = tt1.GetY2NDC();
    ## dx = x2-x1;             dy = y2-y1;
    dy = 0.105;
    dx = 0.20;
    tt1.SetY2NDC(y2);        tt1.SetX2NDC(x2);
    tt1.SetY1NDC(y2-dy);     tt1.SetX1NDC(x2-dx);
    tt2.SetY2NDC(y2-dy);     tt2.SetX2NDC(x2);
    tt2.SetY1NDC(y2-2*dy);   tt2.SetX1NDC(x2-dx);
    gPad.Modified();
    gPad.Update();

    hRat= h2.Clone()
    hRat.SetName("Ratio")
    hRat.Divide(h2,h1,1.,1.,"");

    hRat.SetStats(0)
    ResetAxisAndLabelSizes(hRat,0.065,0.01)
    cname="Ratio"
    ## c2 = prepPlot("c2",cname,250,120,500,500)
    ## c2.SetLogy(0);
    p2.cd()

    min=0.5; max=1.5
    hRat.SetMaximum(1.8)
    hRat.SetMinimum(0.2)
    hRat.Draw()

    xl1=0.6; yl1=.3;
    DrawText(xl1,yl1,label2+"/"+label1,0.075)

    gPad.Update();

    if (PrintPlot):
        psname="comp_" + dist
        c1.Print(psname + ".gif")

#===============================================================
    if os.getenv("FROMGUI") == None:
        print "Not from GUI"
        raw_input('\npress return to end the program...')
