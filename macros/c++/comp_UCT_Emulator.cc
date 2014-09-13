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

void comp_UCT_Emulator(){

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

 TString rootnameUCT = "L1Trigger/UCT2015/test/out.root";
 TString rootnameL1T = "L1Trigger/L1TCalorimeter/test/SimL1Emulator_Stage1_PP.root";


 TFile* rootUCT= OpenRootFile(rootnameUCT); if (!rootUCT) return;
 TFile* rootL1T= OpenRootFile(rootnameL1T); if (!rootL1T) return;

 TString treename  = "Events";
 TTree* _treeUCT = dynamic_cast<TTree*>(rootUCT->Get(treename));
 if (!_treeUCT) {
    cout << " Treename " << treename << " not found" << endl;
    return;
 }

 TTree* _treeL1T = dynamic_cast<TTree*>(rootL1T->Get(treename));
 if (!_treeL1T) {
   cout << " Treename " << treename << " not found" << endl;
   return;
 }

 bool plotCentralJets=false;
 bool plotForwardJets=false;


 TString CutUCT        = "", CutL1T = "", Itype = "", Iso="<2";
 TString Var        = "RelaxedEG";
 // TString Var        = "IsolatedEG";
 if (Var == "IsolatedEG") Iso = "==1";

 TString VarUCT     = "UCTCandidates_UCT2015Producer_" + Var + "Unpacked_ReRunningL1.obj.pt()";
 // TString VarUCT     = "UCTCandidates_UCT2015Producer_IsolatedEGUnpacked_ReRunningL1.obj.pt()";
 // TString VarL1T     = "l1tEGammaBXVector_caloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.et()";
 TString VarL1T     = "l1tEGammaBXVector_caloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.hwPt()";
 TString CutL1T     = "l1tEGammaBXVector_caloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.hwIso()" + Iso;


 int nbins=64;
 float min=0., max=64;
 float ymin=0.9, ymax=-600000.;
 if (Var == "GT.Taujet"){
   ymax=600000;
   ymin=1000.;
   nbins=5;
   min=0; max=5.;
 }

 int rebin=1;

 // *************  MET and friends  *************************** //
 Var        = "MET"; Itype = "2"; max=400; ymax=500.;
 Var        = "MHT"; Itype = "3"; max=460; ymax=500.;
 Var        = "SET"; Itype = "0"; max=1000; ymax=500.;
 Var        = "SHT"; Itype = "1"; max=1500; ymax=500.;
 VarUCT     = "UCTCandidates_UCT2015Producer_" +Var+"Unpacked_ReRunningL1.obj.pt()";
 VarL1T     = "l1tEtSumBXVector_caloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.et()";
 CutL1T = "l1tEtSumBXVector_caloStage1FinalDigis__L1TEMULATION.obj.data_.type_==" + Itype;
 
 nbins=100;
 int rebin=5;
 float min=-0;
 float ymin=1.;


 // Var        = "IsolatedTau";
 // // Var        = "RelaxedTau";
 // VarUCT     = "UCTCandidates_UCT2015Producer_"+Var+"Unpacked_ReRunningL1.obj.pt()";
 // VarL1T     = "l1tTauBXVector_caloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.et()";
 // // VarL1T     = "l1tTauBXVector_caloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.hwPt()";
 // if (Var == "RelaxedTau"){
 //   // CutL1T = "l1tTauBXVector_caloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.hwIso()==0";
 //   CutL1T="";
 // }else{
 //   CutL1T = "l1tTauBXVector_caloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.hwIso()==1";
 // }
 // 
 // nbins=256;
 // int rebin=8;
 // float min=-0, max=256;
 // float ymin=0.1, ymax=5500.;


 //rootUCT->GetListOfKeys()->Print();
 

 string hname1= Var + "_UCT", hname2=Var +"_L1T";
 TH1F *hUCT = new TH1F(hname1.c_str(),hname1.c_str(),nbins,min,max);
 TH1F *hL1T = new TH1F(hname2.c_str(),hname2.c_str(),nbins,min,max);
 hUCT->Sumw2();  hL1T->Sumw2();
 
 hUCT->SetLineColor(kRed);
 hL1T->SetLineColor(kBlue);
 if (ymax>0)
   hUCT->GetYaxis()->SetRangeUser(ymin,ymax);


 // TString VarUCT(Var), VarL1T(Var);

 _treeUCT->Project(hname1.c_str(),VarUCT,CutUCT);
 _treeL1T->Project(hname2.c_str(),VarL1T,CutL1T);

 TCanvas *c1= new TCanvas("c1","Root Canvas 1");

 hUCT->Rebin(rebin);
 hL1T->Rebin(rebin);
 hUCT->Draw();
 // hL1T->Scale(0.5);
 hL1T->Draw("sames");
 // hL1T->Draw();

 Double_t xl1=.16, yl1=0.16, xl2=xl1+.3, yl2=yl1+.125;
 TLegend *leg = new TLegend(xl1,yl1,xl2,yl2);
 leg->AddEntry(hL1T,"L1Emulator","pl");
 leg->AddEntry(hUCT,"UCT2015","pl");   // h1 and h2 are histogram pointers
 leg->Draw();

  if( !c1->IsZombie() ) {
    gPad->Update();
    TPaveStats *tt1 = (TPaveStats*)hUCT->GetFunction("stats");
    tt1->SetTextColor(hUCT->GetLineColor());
    TPaveStats *tt2 = (TPaveStats*)hL1T->GetFunction("stats");
    tt2->SetTextColor(hL1T->GetLineColor());
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

  if (plotCentralJets){
    Var="Central"+Var;
  }else if (plotForwardJets){
    Var="Forward"+Var;
  }
  TLatex *t = new TLatex();
    // Int_t txtsize=17;
  // Int_t txtfnt=63;
  Int_t txtalign=13;
  Float_t xtxt=.625, ytxt=.8;
  t->SetNDC();
  t->SetTextAlign(txtalign);
  //t->SetTextFont(txtfnt);
  //t->SetTextSizePixels(txtsize);
  t->DrawLatex(xtxt,ytxt,Var);
  t->DrawLatex(xtxt,ytxt-0.05,"Fully Corrected");
  // t->DrawLatex(xtxt,ytxt-0.05,"No PileUp");
  //t->DrawLatex(xtxt,ytxt-2*0.05,"No JEC");

  gPad->Update();

  //gROOT->Reset();

  bool writeIt=false;
  if (writeIt){
    TString outname="comp_"+Var+".gif";
    cout << "Saving canvas to: " << outname << endl;
    c1->Print(outname);
  }
}
