from ROOT import gROOT, gStyle, gSystem, TCanvas, TF1, TFile, TH1F, TColor, TLine, TLegend, TLatex, SetOwnership, TChain
import sys,string,math,os,ROOT

from PhysicsTools.PythonAnalysis import *
from ROOT import *
gSystem.Load("libFWCoreFWLite.so")
AutoLibraryLoader.enable()

sys.path.append(os.path.join(os.environ.get("HOME"),'rootmacros'))
from myPyRootMacros import prepPlot, SetStyle, GetHist, PrepLegend, DrawText, prep1by2Plot, ResetAxisAndLabelSizes
#===============================================================

label1 = "750pre1";  process1 = "_L1TEMULATION";  module1="l1ExtraLayer2_";
fileNames1=["SimL1Emulator_Stage1_PP_Default.root"]

label2 = "740";  process2 = "_L1TEMULATION";  module2="l1ExtraLayer2_";
fileNames2=["/afs/cern.ch/user/a/apana/work/L1Upgrade/Emulator/Validate/CMSSW_7_4_0_pre8/src/L1Trigger/L1TCalorimeter/test/SimL1Emulator_Stage1_PP.root"]

Rebin=-1  ## used to overide default rebin value

PrintPlot=False
# PrintPlot=True

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
            rebin_=4;
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
            if L1Object_ == "SET":
                self.l1obj="MET";
                xmax_=1200; nbins_=120; rebin_=5;
                if ("et"==Dist_):
                    xmax_=500; nbins_=50; rebin_=2;
            else:
                self.l1obj="MHT";
                xmax_=1.; nbins_=100; rebin_=5;
                if ("etTot_" == Dist_):
                    xmax_=1200; nbins_=120; rebin_=5;
        elif ( L1Object_ == "Muon"):
            self.l1coll="l1extraL1MuonParticles_";
            self.l1obj="";
            xmax_=140; nbins_=140; rebin_=1;
        elif ( L1Object_ == "HFRings"):
            self.l1coll="l1extraL1HFRingss_";
            self.l1obj="";
            xmin_=0; xmax_=50; nbins_=50; rebin_=1;

        if ("eta"==Dist_):
            xmin_=-5; xmax_=5; nbins_=20; self.logy=0; rebin_=1
            ## xmin_=0; xmax_=21; nbins_=21; self.logy=0; rebin_=1

        if ("phi"==Dist_):
            xmin_=-3.15; xmax_=3.15; nbins_=20; self.logy=0; rebin_=1


        if Rebin > 0: rebin_=Rebin

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

def CompL1Extra(L1Obj="xxx",dist="xxx"):

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

    histos=SetupHistos(L1Obj,dist)

    branch1=histos.l1coll+module1+histos.l1obj+process1+".obj."+dist+"()";   cut1="";
    branch2=histos.l1coll+module2+histos.l1obj+process2+".obj."+dist+"()";   cut2="";
    if dist == "etTot_" or dist == "m_ringEtSums":
        print "XXXXXXXXXXXXXXXXX"
        branch1=histos.l1coll+module1+histos.l1obj+process1+".obj."+dist;   cut1="";
        branch2=histos.l1coll+module2+histos.l1obj+process2+".obj."+dist;   cut2="";

    print branch1
    print branch2

    h1=histos.h1;h2=histos.h2
    tree1.Project(h1.GetName(),branch1)
    tree2.Project(h2.GetName(),branch2)

    if (histos.ymax > 0.):
        h1.GetYaxis().SetRangeUser(histos.ymin,histos.ymax);
        h2.GetYaxis().SetRangeUser(histos.ymin,histos.ymax);

    print "h1: ",h1.GetEntries()
    print "h2: ",h2.GetEntries()

    # h1.Scale(1./h1.GetEntries())
    # h2.Scale(1./h2.GetEntries())

    ## c1=prepPlot("c1","L1Extra")
    ## c1.SetLogy(histos.logy)
    c1,p1,p2 = prep1by2Plot("c1","L1Extra",500)
    p1.Draw(); p2.Draw()

    p1.cd()
    p1.SetLogy(histos.logy)

    h1.SetLabelOffset(0.1, "X");
    ## h2.Scale(0.9)
    h1.Draw()
    h2.Draw("sames")

    xl1=.2; yl1=0.16; xl2=xl1+.2; yl2=yl1+.1;
    leg0=PrepLegend(xl1,yl1,xl2,yl2,0.03)
    leg0.AddEntry(h1,label1,"pl")
    leg0.AddEntry(h2,label2,"pl")
    leg0.Draw();

    DrawText(0.6,0.7,L1Obj,0.04)
    gPad.Update();
    # print h1.GetListOfFunctions()
    # print h1.GetListOfFunctions().FindObject("stats")
    # print h1.FindObject("stats")
    ## tt1=h1.GetFunction("stats");
    tt1=h1.FindObject("stats");
    tt1.SetTextColor(h1.GetLineColor());
    ## tt2=h2.GetFunction("stats");
    tt2=h2.FindObject("stats");
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
    hRat.GetXaxis().SetTitle(dist);

    hRat.Divide(h2,h1,1.,1.,"");

    hRat.SetStats(0)
    ResetAxisAndLabelSizes(hRat,0.07,0.01)
    hRat.SetTitleSize( 0.1, "X" ); hRat.SetTitleOffset(0.8, "X");
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
        psname="comp_" + L1Obj + "_" + dist
        c1.Print(psname + ".gif")


#===============================================================
    if os.getenv("FROMGUI") == None:
        print "Not from GUI"
        ans=raw_input('\npress return to continue, \"e\" to exit...')
        # print "ans= ",ans
        if len(ans)>0:
            return 1


    return 0

if __name__ == '__main__':

    SetStyle()
    gStyle.SetOptStat(110);

    L1Objs=["NonIsolatedEG","IsolatedEG","CenJet","ForJet","Tau","IsoTau","SET","SHT","HFRings"]
    # L1Objs=["NonIsolatedEG","IsolatedEG","CenJet","ForJet","Tau","IsoTau"]
    # L1Objs=["SET","SHT","HFRings"]

    for L1Obj in L1Objs:
        dist="et"
        # dist="eta"
        # dist="phi"
        if "et"==dist and (L1Obj=="SET" or L1Obj=="SHT"):
            dist="etTot_"
        elif "et"==dist and L1Obj=="HFRings": 
            dist="m_ringEtSums"
        elif "eta"==dist and (L1Obj=="SET" or L1Obj=="SHT" or L1Obj=="HFRings" or L1Obj=="MET" or L1Obj=="MHT"):
            continue
        elif ("eta"==dist or "phi"==dist) and L1Obj=="HFRings":
            continue

        print "Comparing ",L1Obj,dist
        go=CompL1Extra(L1Obj,dist)
        if go == 1:
            break

