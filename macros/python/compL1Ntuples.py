from ROOT import gROOT, gStyle, gSystem, TCanvas, TF1, TFile, TH1F, TColor, TLine, TLegend, TLatex, SetOwnership, TChain
import sys,string,math,os,ROOT

from PhysicsTools.PythonAnalysis import *
from ROOT import *
gSystem.Load("libFWCoreFWLite.so")
AutoLibraryLoader.enable()

sys.path.append(os.path.join(os.environ.get("HOME"),'rootmacros'))
from myPyRootMacros import prepPlot, SetStyle, GetHist, PrepLegend, DrawText, prep1by2Plot, ResetAxisAndLabelSizes
#===============================================================

dist="et"
## dist="phi"
## dist="eta"

## L1Obj        = "Tau"
## L1Obj        = "IsoTau"
L1Obj        = "NonIsolatedEG"
## L1Obj        = "IsolatedEG"
## L1Obj        = "Muon"
## L1Obj        = "CenJet"
## L1Obj        = "ForJet"
## L1Obj        = "SET" ; dist="etTot_" ; ## dist="phi"
## L1Obj        = "SHT" ; dist="etTot_";
## L1Obj        = "ETT" ;
## L1Obj        = "MET" ;
## L1Obj        = "HTT" ;
## L1Obj        = "HTM" ;
## L1Obj        = "HFRings" ; dist="m_ringEtSums"; 

## label1 = "rctReEmul";
## fileNames1=["L1Tree_dropped_rct.root"]

label1 = "ExtendedScaleFactors_EGOnly_V1";
fileNames1=["L1Tree_dropped_newrct.root"]

## label1 = "ExtendedScaleFactors_V4";
## fileNames1=["L1Tree_dropped_newrct_v4.root"]

label2 = "MCRUN2_74_V8";
fileNames2=["L1Tree_dropped.root"]

Rebin=4  ## used to overide default rebin value

# PrintPlot=False
PrintPlot=True

#===============================================================

class SetupHistos():

    def __init__(self, L1Object_="xxx", Dist_="et"):

        self.l1coll="XXX"; self.varString=""; self.cutString=""; self.logy=1; self.ymin=0.1; self.ymax=-1; 
        nbins_=100; xmin_=0; xmax_=1000.; rebin_=1;
 
        if (L1Object_ == "CenJet"):
            self.l1coll="GT.Rankjet";
            self.cutString="GT.Fwdjet==0 && GT.Taujet==0";
            nbins_=64; xmin_=0.; xmax_=64.

            if Dist_ == "eta":
                self.l1coll="GT.Etajet";
            if Dist_ == "phi":
                self.l1coll="GT.Phijet";
                
            rebin_=1;
        elif (L1Object_ == "Tau"):
            self.l1coll="GT.Rankjet";
            self.cutString="GT.Taujet==1";
            nbins_=64; xmin_=0.; xmax_=64.
            rebin_=1;

            if Dist_ == "eta":
                self.l1coll="GT.Etajet";
            if Dist_ == "phi":
                self.l1coll="GT.Phijet";

        elif (L1Object_ == "ForJet"):
            self.l1coll="GT.Rankjet";
            self.cutString="GT.Fwdjet==1";
            nbins_=64; xmin_=0.; xmax_=64.
            rebin_=1;

            if Dist_ == "eta":
                self.l1coll="GT.Etajet";
            if Dist_ == "phi":
                self.l1coll="GT.Phijet";

        elif (L1Object_ == "NonIsolatedEG" or L1Object_ == "IsolatedEG"):
            self.l1coll="GT.Rankel";
            if (L1Object_ == "NonIsolatedEG"):
                self.cutString="GT.Isoel==0";
            else:
                self.cutString="GT.Isoel==1";


            if Dist_ == "eta":
                self.l1coll="GT.Etael";
            if Dist_ == "phi":
                self.l1coll="GT.Phiel";


            nbins_=64;xmax_=64;rebin_=1;

        elif ( L1Object_ == "ETT"):
            self.l1coll="GT.RankETT";
            self.l1obj=L1Object_;
            xmax_=460; nbins_=460; rebin_=5;

        elif ( L1Object_ == "HTT"):
            self.l1coll="GT.RankHTT";
            self.l1obj=L1Object_;
            xmax_=460; nbins_=460; rebin_=5;

        elif ( L1Object_ == "MET"):
            self.l1coll="GT.RankETM";
            self.l1obj=L1Object_;
            xmax_=460; nbins_=460; rebin_=5;

            if Dist_ == "phi":
                self.l1coll="GT.PhiETM";

        elif ( L1Object_ == "MHT"):
            self.l1coll="GT.RankHTM";
            self.l1obj=L1Object_;
            xmax_=460; nbins_=460; rebin_=5;

            if Dist_ == "phi":
                self.l1coll="GT.PhiHTM";

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
            ## xmin_=-5; xmax_=5; nbins_=20; self.logy=0; rebin_=1
            xmin_=0; xmax_=21; nbins_=21; self.logy=0; rebin_=1

        if ("phi"==Dist_):
            xmin_=0; xmax_=18; nbins_=18; self.logy=0; rebin_=1
            if L1Object_ == "MET":
                xmin_=0; xmax_=72; nbins_=72; self.logy=0; rebin_=1


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

if __name__ == '__main__':

    SetStyle()
    gStyle.SetOptStat(110);
#===============================================================


    ## print "\n",fileName1
    ## print fileName2,"\n"
    ## f1 = ROOT.TFile.Open(fileName1);  tree1=ROOT.gDirectory.Get("Events")
    ## f2 = ROOT.TFile.Open(fileName2);  tree2=ROOT.gDirectory.Get("Events")

    tree1=TChain("l1NtupleProducer/L1Tree");
    i=0
    for f in fileNames1:
        i=i+1
        print i,f
        tree1.Add(f);

    print "\n"

    tree2=TChain("l1NtupleProducer/L1Tree");
    i=0
    for f in fileNames2:
        i=i+1
        print i,f
        tree2.Add(f)

    histos=SetupHistos(L1Obj,dist)

    branch1=histos.l1coll;   cut1=histos.cutString;
    branch2=histos.l1coll;   cut2=histos.cutString;

    ymax=-1;
    xmax=-1;
    ## if L1Obj == "CenJet":
    ##     cut2="GT.Fwdjet==0"
    ##     # ymax=1e6;

    if L1Obj == "ForJet":
        xmax=25;

    print "\nL1Obj= ",L1Obj,"\n"
    print branch1,cut1
    print branch2,cut2

    h1=histos.h1;h2=histos.h2
    tree1.Project(h1.GetName(),branch1,cut1)
    tree2.Project(h2.GetName(),branch2,cut2)

    if (histos.ymax > 0.):
        h1.GetYaxis().SetRangeUser(histos.ymin,histos.ymax);
        h2.GetYaxis().SetRangeUser(histos.ymin,histos.ymax);

    print "h1: ",h1.GetEntries()
    print "h2: ",h2.GetEntries()

    if ymax>0:
        h1.GetYaxis().SetRangeUser(0.2,ymax);

    if xmax>0:
        h1.GetXaxis().SetRangeUser(0,xmax);


    xlabel="xxx"
    if dist == 'et':
        xlabel="E_{T}"
    elif dist == 'phi':
        xlabel="Phi"
    elif dist == 'eta':
        xlabel="Eta"

    h1.GetXaxis().SetTitle(xlabel)

    # h1.Scale(1./h1.GetEntries())
    # h2.Scale(1./h2.GetEntries())

    ## c1=prepPlot("c1","L1Extra")
    ## c1.SetLogy(histos.logy)
    c1,p1,p2 = prep1by2Plot("c1","L1Extra",500)
    p1.Draw(); p2.Draw()

    p1.cd()
    p1.SetLogy(histos.logy)

    h1.SetLabelOffset(0.1, "X");
    ## h2.Scale(0.5)
    h1.Draw()
    h2.Draw("sames")

    xinit=0.2
    if L1Obj == "IsolatedEG" and dist=="et":
        xinit=0.6

    xl1=xinit; yl1=0.1; xl2=xl1+.2; yl2=yl1+.1;
    leg0=PrepLegend(xl1,yl1,xl2,yl2,0.03)
    leg0.AddEntry(h1,label1,"pl")
    leg0.AddEntry(h2,label2,"pl")
    leg0.Draw();

    DrawText(0.525,0.8,L1Obj,0.04)
    DrawText(0.525,0.75,xlabel,0.04)
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

    if xmax>0:
        hRat.GetXaxis().SetRangeUser(0,xmax);

    ## hRat.GetXaxis().SetTitle(xlabel)
    min=0.5; max=1.5
    hRat.SetMaximum(2.5)
    hRat.SetMinimum(0.0)
    hRat.Draw()

    xl1=0.6; yl1=.3;
    DrawText(xl1,yl1,label2+"/"+label1,0.075)

    gPad.Update();

    if (PrintPlot):
        psname="comp_run251718_" + L1Obj + "_" + dist
        c1.Print(psname + ".gif")

#===============================================================
    if os.getenv("FROMGUI") == None:
        print "Not from GUI"
        raw_input('\npress return to end the program...')
