import ROOT
from ROOT import gROOT, gStyle, gSystem, TCanvas, TF1, TFile, TH1F
from ROOT import TColor, TLine, TLegend, TLatex, TObjArray
from ROOT import SetOwnership

from ROOT import gDirectory, gPad

import sys,string,math,os

# import myPyRootSettings
sys.path.append(os.path.join(os.environ.get("HOME"),'rootmacros'))
from myPyRootMacros import prepPlot

if __name__ == '__main__':

    gROOT.Reset()
    gROOT.SetStyle("MyStyle");    
    # gStyle.SetOptLogy(0);
    gStyle.SetPalette(1);
    gStyle.SetOptTitle(0);
    gStyle.SetOptStat(0);
    gStyle.SetPadTopMargin(0.02);
    gStyle.SetPadTickX(1);

    gStyle.SetLabelSize(0.045, "XYZ");
    gStyle.SetLabelSize(0.04, "Y");
    gStyle.SetTitleSize(0.05, "XYZ");

    RootDir="."

    ptmin=0; ptmax=254;
    # ptmin=80; ptmax=100;
    # ptmin=200; ptmax=250;

    HistFile1="triggerEff_257487_HLTPhysicsDS_HLT_ZeroBias_v2_pfjet_JECv3_cleaned_yall.root"
    HistFile2="triggerEff_256675_HLTPhysicsDS_HLT_ZeroBias_v2_pfjet_JECv3_cleaned_ally.root"

    f1 = TFile(HistFile1)
    f2 = TFile(HistFile2)
    # f1.ls()
    # f1.cd("pf")

    hname="hL1CenJetPt"
    hNum = f1.Get(hname)
    hDen = f2.Get(hname)

    hNum.Scale(1./hNum.GetEntries())
    hDen.Scale(1./hDen.GetEntries())
    
    hRat= hNum.Clone()
    hRat.SetName("Ratio")
    hRat.Divide(hNum,hDen,1.,1.,"");
    Hlist=TObjArray()
    Hlist.Add(hRat);

    cname="pT"
    c1 = prepPlot("c1",cname,700,20,500,500)
    c1.SetLogy(1);    

    # i1=90; i2=110
    i1=0; i2=500
    hNum.GetXaxis().SetRange(i1,i2)
    hDen.SetLineColor(ROOT.kRed)
    hNum.Draw()
    hDen.Draw("same")

    cname="Ratio"
    c2 = prepPlot("c2",cname,950,120,500,500)
    c2.SetLogy(0);    

    ymin=0.; ymax=1.24

    hRat.SetMaximum(ymax)
    hRat.SetMinimum(ymin)
    hRat.Draw()


    # f2=TFile(OutFile,"RECREATE")
    # f2.cd()
    # hRat.Write()
    # f2.Close()


#===============================================================
    if os.getenv("FROMGUI") == None:
        print "Not from GUI"
        raw_input('\npress return to end the program...')
