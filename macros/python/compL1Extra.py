from ROOT import gROOT, gStyle, gSystem, TCanvas, TF1, TFile, TH1F, TColor, TLine, TLegend, TLatex, SetOwnership
import sys,string,math,os,ROOT

from PhysicsTools.PythonAnalysis import *
from ROOT import *
gSystem.Load("libFWCoreFWLite.so")
AutoLibraryLoader.enable()

sys.path.append(os.path.join(os.environ.get("HOME"),'rootmacros'))
from myPyRootMacros import prepPlot, SetStyle, GetHist, PrepLegend, DrawText
#===============================================================

dist="et"
## dist="eta"
## L1Obj        = "Tau"
L1Obj        = "IsoTau"
## L1Obj        = "NonIsolatedEG"
## L1Obj        = "IsolatedEG"
## L1Obj        = "Muon"
## L1Obj        = "CenJet"
## L1Obj        = "ForJet"
##L1Obj        = "SET"
##L1Obj        = "SHT"

fileName1 = "SimL1Emulator_Stage1_PP.root";   label1 = "Old";  process1 = "_L1TEMULATION";  module1="l1ExtraLayer2_";
fileName2 = "/afs/cern.ch/work/a/apana/L1Upgrade/Emulator/tau/test/CMSSW_7_2_0_pre8/src/L1Trigger/L1TCalorimeter/test/SimL1Emulator_Stage1_PP.root";              label2 = "New";  process2 = "_L1TEMULATION";  module2="l1ExtraLayer2_";

#===============================================================

class SetupHistos():

    def __init__(self, L1Object_="xxx", Dist_="et"):

        self.l1coll="XXX"; self.varString=""; self.cutString=""; self.logy=1; self.ymin=0.1; self.ymax=-1; 
        nbins_=100; xmin_=0; xmax_=1000.; rebin_=1;

        if (L1Object_ == "CenJet" or L1Object_ == "Tau" or L1Object_ == "IsoTau" or L1Object_ == "ForJet"):
            self.l1coll="l1extraL1JetParticles_";
            if L1Object_ == "CenJet":
                self.l1obj= "Central";
            elif L1Object_ == "ForJet":
                self.l1obj= "Forward"
            else:
                self.l1obj = L1Object_
            nbins_=64; xmin_=0.; xmax_=256.

        elif (L1Object_ == "NonIsolatedEG" or L1Object_ == "IsolatedEG"):
            self.l1coll="l1extraL1EmParticles_";
            if (L1Object_ == "NonIsolatedEG"):
                self.l1obj="NonIsolated";
            else:
                self.l1obj ="Isolated";
            nbins_=64;xmax_=64;rebin_=4;
        elif ( L1Object_ == "MET" or L1Object_ == "MHT"):
            self.l1coll="l1extraL1EtMissParticles_";
            self.l1obj=L1Object_;
            xmax_=460; nbins_=100; rebin_=5;
        elif ( L1Object_ == "SET" or L1Object_ == "SHT"):
            self.l1coll="l1extraL1EtMissParticles_";
            xmax_=1200; nbins_=100; rebin_=5;
        elif ( L1Object_ == "Muon"):
            self.l1coll="l1extraL1MuonParticles_";
            self.l1obj="";
            xmax_=140; nbins_=140; rebin_=1;

        if ("eta"==Dist_):
            xmin_=-5; xmax_=5; nbins_=20; self.logy=0;


        hname1_= L1Object_ + "_1"; hname2_=L1Object_ +"_2";
        h1_ = TH1F(hname1_,hname1_,nbins_,xmin_,xmax_);
        h2_ = TH1F(hname2_,hname2_,nbins_,xmin_,xmax_);

        h1_.Sumw2();  h2_.Sumw2();
        h1_.SetLineColor(ROOT.kRed); h2_.SetLineColor(kBlue);
        h1_.Rebin(rebin_);           h2_.Rebin(rebin_);
        self.h1=h1_
        self.h2=h2_


class HistAttr:
    def __init__(self, histName_, label_, nbins_, xmin_, xmax_, color_):
        self.histName = histName_
        self.label = label_
        self.color = color_
        self.nbins = nbins_
        self.xmin  = xmin_
        self.xmax  = xmax_

if __name__ == '__main__':

    SetStyle()
    gStyle.SetOptStat(110);
#===============================================================


    print "\n",fileName1
    print fileName2,"\n"
    f1 = ROOT.TFile.Open(fileName1);  tree1=ROOT.gDirectory.Get("Events")
    f2 = ROOT.TFile.Open(fileName2);  tree2=ROOT.gDirectory.Get("Events")

    histos=SetupHistos(L1Obj,dist)

    branch1=histos.l1coll+module1+histos.l1obj+process1+".obj."+dist+"()";   cut1="";
    branch2=histos.l1coll+module2+histos.l1obj+process2+".obj."+dist+"()";   cut2="";

    ## branch2="l1extraL1JetParticles_l1ExtraLayer2_IsoTau_L1TEMULATION.obj.et()";
    print branch1
    print branch2

    h1=histos.h1;h2=histos.h2
    tree1.Project(h1.GetName(),branch1)
    tree2.Project(h2.GetName(),branch2)

    if (histos.ymax > 0.):
        h1.GetYaxis().SetRangeUser(histos.ymin,histos.ymax);
        h2.GetYaxis().SetRangeUser(histos.ymin,histos.ymax);

    c1=prepPlot("c1","L1Extra")
    c1.SetLogy(histos.logy)
    ## h2.Scale(0.5)
    h1.Draw()
    h2.Draw("sames")

    xl1=.2; yl1=0.16; xl2=xl1+.2; yl2=yl1+.1;
    leg0=PrepLegend(xl1,yl1,xl2,yl2,0.03)
    leg0.AddEntry(h1,label1,"pl")
    leg0.AddEntry(h2,label2,"pl")
    leg0.Draw();

    DrawText(0.6,0.8,L1Obj,0.04)
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

#===============================================================
    if os.getenv("FROMGUI") == None:
        print "Not from GUI"
        raw_input('\npress return to end the program...')
