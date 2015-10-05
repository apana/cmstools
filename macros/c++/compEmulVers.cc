//#include "rootfuncs.h"

TFile* OpenRootFile(const TString& rootfile) {

  cout << "Rootfile: " << rootfile << endl;

  TFile *file;
  if( gSystem->AccessPathName(rootfile) ){
    cout << endl << "File: " << rootfile << " not there!!!" << endl << endl;
    file=0;
  }
  else
    file = new TFile(rootfile);

  return file;
}

void compEmulVers(){

 gROOT->Reset();
 gStyle->SetOptTitle(1);
 gStyle->SetOptStat(1);
 //gStyle->SetTitleOffset(0.8,"y");
 gStyle->SetOptLogy(0);

 //gStyle->SetTitleSize(0.05,"y");
 //gStyle->SetTitleSize(0.05,"x");

 //gStyle->SetLabelSize(0.04,"y");
 //gStyle->SetLabelSize(0.045,"x");

 gStyle->SetOptLogy(1);
 gStyle->SetOptTitle(0);
 gROOT->ForceStyle();

 TString rootname1 = "SimL1Emulator_Stage1_PP_org.root";
 TString rootname2 = "SimL1Emulator_Stage1_PP_new.root";

 TString Vers1 ="OLD";
 TString Vers2 ="NEW";

 TFile* root1= OpenRootFile(rootname1); if (!root1) return;
 TFile* root2= OpenRootFile(rootname2); if (!root2) return;

 TString treename  = "Events";
 TTree* _tree1 = dynamic_cast<TTree*>(root1->Get(treename));
 if (!_tree1) {
    cout << " Treename " << treename << " not found" << endl;
    return;
 }

 TTree* _tree2 = dynamic_cast<TTree*>(root2->Get(treename));
 if (!_tree2) {
   cout << " Treename " << treename << " not found" << endl;
   return;
 }

 // initialization
 TString Cut(""), Var("XXX");
 int nbins(100), rebin(1);
 float min(0.),max(1000.),ymin(0.9),ymax(-600000.);

 // string myVar        = "IsolatedEG";
 // string myVar        = "RelaxedEG";
 // string myVar        = "RelaxedTau";
 // string myVar        = "IsolatedTau";
 string myVar        = "Jet";

 if (myVar == "IsolatedEG" || myVar == "RelaxedEG"){

   TString Iso("-999");
   if (myVar == "IsolatedEG") Iso = "==1";

   Var     = "l1tEGammaBXVector_simCaloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.et()";
   // Var     = "l1tEGammaBXVector_simCaloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.hwPt()";
   Cut     = "l1tEGammaBXVector_simCaloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.hwIso()" + Iso;

   nbins=64;
   min=0., max=64;

   rebin=1;
 }else if (myVar == "MET" || myVar == "MHT" || myVar == "SET" || myVar == "SHT"){
   // *************  MET and friends  *************************** //
   TString Itype("-999");
   if (myVar == "MET"){
     Itype = "2"; max=400; ymax=500.;
   }else if (myVar == "MHT"){
     Itype = "3"; max=460; ymax=500.;
   }else if (myVar == "SET"){
     Itype = "0"; max=1000; ymax=500.;
   }else if (myVar == "SHT"){
     Itype = "1"; max=1500; ymax=500.;
   }
 
   // Var     = "l1tEtSumBXVector_simCaloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.et()";
   // Cut = "l1tEtSumBXVector_simCaloStage1FinalDigis__L1TEMULATION.obj.data_.type_==" + Itype;
 
   Var     = "l1tEtSumBXVector_simCaloStage1Digis__L1TEMULATION.obj.data_.l1t::L1Candidate.hwPt()";
   Cut = "l1tEtSumBXVector_simCaloStage1Digis__L1TEMULATION.obj.data_.type_==" + Itype;
 
   nbins=100;
   rebin=5;
   min=-0;
   ymin=1.;

 }else if (myVar == "Jet"){

   Var     = "l1tJetBXVector_simCaloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.et()";
   Cut     = "";
   nbins=256;
   rebin=8;
   min=-0, max=256;
   ymin=0.1, ymax=5500.;

 }else if (myVar == "RelaxedTau" || myVar == "IsolatedTau"){
   Cut="";
   TString TauColl("isoTaus");
   if (myVar == "RelaxedTau") TauColl="rlxTaus";

   // Var     = "l1tTauBXVector_simCaloStage1FinalDigis_"+TauColl+"_L1TEMULATION.obj.data_.l1t::L1Candidate.hwPt()";
   Var     = "l1tTauBXVector_simCaloStage1FinalDigis_"+TauColl+"_L1TEMULATION.obj.data_.l1t::L1Candidate.et()"; 
   nbins=256;
   rebin=8;
   min=-0, max=256;
   ymin=0.1, ymax=5500.;
 }

 //rootUCT->GetListOfKeys()->Print();
 
 cout << "\nRootFile1: " << rootname1 << std::endl;
 cout << "RootFile2: " << rootname2 << std::endl;

 cout << "\nVar: " << Var << endl;
 cout << "Cut: " << Cut << endl;

 string hname1= myVar + "_1", hname2=myVar +"_2";
 TH1F *h1 = new TH1F(hname1.c_str(),hname1.c_str(),nbins,min,max);
 TH1F *h2 = new TH1F(hname2.c_str(),hname2.c_str(),nbins,min,max);
 h1->Sumw2();  h2->Sumw2();
 
 h1->SetLineColor(kRed);
 h2->SetLineColor(kBlue);
 if (ymax>0)
   h1->GetYaxis()->SetRangeUser(ymin,ymax);

 _tree1->Project(hname1.c_str(),Var,Cut);
 _tree2->Project(hname2.c_str(),Var,Cut);

 TCanvas *c1= new TCanvas("c1","Root Canvas 1");

 h1->Rebin(rebin);
 h2->Rebin(rebin);
 h1->Draw();
 // h2->Scale(0.8);
 h2->Draw("sames");
 // h2->Draw();

 Double_t xl1=.26, yl1=0.16, xl2=xl1+.3, yl2=yl1+.125;
 TLegend *leg = new TLegend(xl1,yl1,xl2,yl2);
 leg->AddEntry(h2,Vers2,"pl");
 leg->AddEntry(h1,Vers1,"pl");   // h1 and h2 are histogram pointers
 leg->Draw();

  if( !c1->IsZombie() ) {
    gPad->Update();
    TPaveStats *tt1 = (TPaveStats*)h1->GetFunction("stats");
    tt1->SetTextColor(h1->GetLineColor());
    TPaveStats *tt2 = (TPaveStats*)h2->GetFunction("stats");
    tt2->SetTextColor(h2->GetLineColor());
    double x1 = tt1->GetX1NDC();    double y1 = tt1->GetY1NDC();
    double x2 = tt1->GetX2NDC();    double y2 = tt1->GetY2NDC();
    //double dx = x2-x1;              double dy = y2-y1;
    double dy = 0.15;
    double dx = 0.20;

    // //set stat boxes one on top of the other
    // tt1->SetY2NDC(y2);        tt1->SetX2NDC(x2);
    // tt1->SetY1NDC(y2-dy);     tt1->SetX1NDC(x2-dx);
    // tt2->SetY2NDC(y2-dy);     tt2->SetX2NDC(x2);
    // tt2->SetY1NDC(y2-2*dy);   tt2->SetX1NDC(x2-dx);

    cout << " x1: " << x1 << " x2:" << x2 << endl;
    cout << " y1: " << y1 << " y2:" << y2 << endl;

    tt1->SetY2NDC(y2);        tt1->SetX2NDC(x2);
    tt1->SetY1NDC(y2-dy);     tt1->SetX1NDC(x2-dx);

    tt2->SetY2NDC(y2);      tt2->SetX2NDC(x2-dx);
    tt2->SetY1NDC(y2-dy);   tt2->SetX1NDC(x2-2*dx);
    gPad->Modified();   
  }// modify statboxes 


  TLatex *t = new TLatex();
    // Int_t txtsize=17;
  // Int_t txtfnt=63;
  Int_t txtalign=13;
  Float_t xtxt=.625, ytxt=.8;
  t->SetNDC();
  t->SetTextAlign(txtalign);
  //t->SetTextFont(txtfnt);
  //t->SetTextSizePixels(txtsize);
  t->DrawLatex(xtxt,ytxt,myVar.c_str());
  // t->DrawLatex(xtxt,ytxt-0.05,"Fully Corrected");
  // t->DrawLatex(xtxt,ytxt-0.05,"No PileUp");
  //t->DrawLatex(xtxt,ytxt-2*0.05,"No JEC");

  gPad->Update();

  //gROOT->Reset();

  // bool writeIt=false;
  bool writeIt=true;
  if (writeIt){
    string outname="comp_"+myVar+".gif";
    cout << "Saving canvas to: " << outname << endl;
    c1->Print(outname.c_str());
  }
}
