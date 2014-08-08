#include "rootfuncs.h"

void plotL1EmuLeaf(){

 gROOT->Reset();
 gStyle->SetOptTitle(1);
 gStyle->SetOptStat(1);
 //gStyle->SetTitleOffset(0.8,"y");
 gStyle->SetOptLogy(0);

 //gStyle->SetTitleSize(0.05,"y");
 //gStyle->SetTitleSize(0.05,"x");

 //gStyle->SetLabelSize(0.04,"y");
 //gStyle->SetLabelSize(0.045,"x");

 //gStyle->SetHistFillColor(kYellow);
 gStyle->SetOptLogy(1);
 gROOT->ForceStyle();

 // TString myVar     = "l1tEGammaBXVector_caloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.et()";

 TString myCut     = "l1tEtSumBXVector_caloStage1FinalDigis__L1TEMULATION.obj.data_.type_==2";
 TString myVar     = "l1tEtSumBXVector_caloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.et()";
 // TString myVar     = "l1tEtSumBXVector_caloStage1FinalDigis__L1TEMULATION.obj.data_.type_";

 myCut=myCut + " && l1tEtSumBXVector_caloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.et()>49.9"; 
 TString treename  = "Events";
 TString rootname = "L1Trigger/L1TCalorimeter/test/SimL1Emulator_Stage1_PP.root";

 TFile *rootfile=OpenRootFile(rootname); if (!rootfile) return;
 //rootfile->GetListOfKeys()->Print();
 
 int nbins=400;
 float min=-0, max=400.;

 string hname1= myVar + "_1", hname2=myVar +"_2";
 TH1F *h1 = new TH1F("leaf1",hname1.c_str(),nbins,min,max);
 h1->Sumw2();
 
 TTree *_tree = dynamic_cast<TTree*>(rootfile->Get(treename));
 if (!_tree) {
    cout << " Treename " << treename << " not found" << endl;
    return;
  }

 _tree->Project("leaf1",myVar,myCut);

 TCanvas *c1= new TCanvas("c1","Root Canvas 1");

 h1->Rebin(1);
 h1->Draw();



 //gROOT->Reset();

}
