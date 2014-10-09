#include "rootfuncs.h"

class SetupHistos
{
public:
  //constructor
  SetupHistos(TString L1Object , TString Dist)
  {
    std::cout << "Setting up comparisions for " << L1Object << std::endl;
    std::cout << "Distribution: " << Dist << std::endl;
    cutString_="";
    L1Collection_="";
    TString var="XXX";
    rebin_=1; xmin_=0.; xmax_=1000.; ymin_=0.1; ymax_=-1; 
    if (L1Object == "CenJet" || L1Object == "Tau" || L1Object == "ForJet"){
      L1Collection_="l1extraL1JetParticles_";
      if (L1Object == "CenJet"){
	var="Central";
      }else if (L1Object == "ForJet"){
	var="Forward";
      }else{
	var =L1Object;
      }
      nbins_=64;
      xmax_=256;
    } else if (L1Object == "NonIsolatedEG" || L1Object == "IsolatedEG"){
      L1Collection_="l1extraL1EmParticles_";
      if (L1Object == "NonIsolatedEG"){
	var="NonIsolated";
      }else{
	var ="Isolated";
      }
      nbins_=64;
      xmax_=64;
      rebin_=4;
    } else if ( L1Object == "MET" || L1Object == "MHT"){ 
      L1Collection_="l1extraL1EtMissParticles_";
      var=L1Object;
      xmax_=460;
      nbins_=100;
      rebin_=5;
    } else if ( L1Object == "SET" || L1Object == "SHT"){ 
      L1Collection_="l1extraL1EtMissParticles_";
      xmax_=1200;
      nbins_=100;
      rebin_=5;
    } else if ( L1Object == "Muon"){
      L1Collection_="l1extraL1MuonParticles_";
      var="";
      xmax_=140;
      nbins_=140;
      rebin_=1;
    }

    if ("eta"==Dist){
      xmin_=-5;
      xmax_=5;
      nbins_=20;
      rebin_=1;
    }

    varString_= var;
    hname1_= L1Object + "_1", hname2_=L1Object +"_2";
    h1_ = new TH1F(hname1_,hname1_,nbins_,xmin_,xmax_);
    h2_ = new TH1F(hname2_,hname2_,nbins_,xmin_,xmax_);
    h1_->Sumw2();  h2_->Sumw2();
 
    h1_->SetLineColor(kRed);
    h2_->SetLineColor(kBlue);

  }
  ~SetupHistos(){}

  int getNbins() const {return nbins_; }
  int getRebin() const {return rebin_; }
  float getYmax() const {return ymax_;}
  float getYmin() const {return ymin_;}
  TString getVarString() const {return varString_; }
  TString getCutString() const {return cutString_; }
  TString getL1Collection() const {return L1Collection_; }
  TH1F *getHist1() {return h1_;}
  TH1F *getHist2() {return h2_;}
private:

  int nbins_, rebin_;
  float xmin_, xmax_;
  float ymin_, ymax_;

  TString hname1_, hname2_, varString_, cutString_, L1Collection_;
  TH1F *h1_,*h2_;

};

void compL1Extra(){

  gROOT->Reset();
  gStyle->SetOptTitle(1);
  gStyle->SetOptStat(110);
  //gStyle->SetTitleOffset(0.8,"y");
  gStyle->SetOptLogy(1);
  gStyle->SetOptTitle(0);
  gROOT->ForceStyle();

 
  // TString rootname1 = "L1Extra_noEmul.root";  TString label1 = "HLT";  TString process1 = "_HLT";  TString module1="l1extraParticles_";
  // TString rootname2 = "L1Extra_noEmul.root";  TString label2 = "HLT";  TString process2 = "_HLT"; TString module2="hltL1extraParticles_";
  // TString rootname2 = "L1Extra_noEmul.root";  TString label2 = "L1NT"; TString process2 = "_L1NTUPLE"; TString module2="l1extraParticles_";

  // TString rootname1 = "outputA_legacy.root";  TString label1 = "Legacy"; TString process1 = "_TEST"; TString module1 = "hltL1extraParticles_";
  TString rootname1 = "outputA_ZZZ.root";  TString label1 = "Stage1 rpc"; TString process1 = "_TEST"; TString module1 = "hltL1extraParticles_";
  //TString rootname2 = "outputA_stage1.root";  TString label2 = "Stage1"; TString process2 = "_TEST"; TString module2="hltL1extraParticles_";
  TString rootname2 = "../../push/CMSSW_7_2_0_pre7/src/outputA.root";  TString label2 = "Stage1"; TString process2 = "_TEST"; TString module2="hltL1extraParticles_";

  TString treename  = "Events";
  
  TString L1Obj, dist;

  dist="et";
  // dist="eta";
  // L1Obj        = "Tau";
  // L1Obj        = "NonIsolatedEG";
  // L1Obj        = "IsolatedEG";
  // L1Obj        = "Muon";
  L1Obj        = "CenJet";
  // L1Obj        = "ForJet";
  //L1Obj        = "SET";
  //L1Obj        = "SHT";

 
  TFile *root1=OpenRootFile(rootname1); if (!root1) return;
  TFile *root2=OpenRootFile(rootname2); if (!root2) return;
  //rootUCT->GetListOfKeys()->Print();

  SetupHistos myHists(L1Obj,dist);
  int nbins=myHists.getNbins();
  int rebin=myHists.getRebin();

  TH1F* h1=myHists.getHist1();
  TH1F* h2=myHists.getHist2();
  TString hname1=h1->GetName();
  TString hname2=h2->GetName();
  TString varString=myHists.getVarString();
  TString cutString=myHists.getCutString();
  TString l1coll=myHists.getL1Collection();

  // TTree *_tree1 = dynamic_cast<TTree*>(root1->Get(treename));
  TTree* _tree1 = (TTree*)root1->Get(treename);
  if (! _tree1) {
    cout << " Treename " << treename << " not found" << endl;
    return;
  }

  // TTree *_tree2 = dynamic_cast<TTree*>(root2->Get(treename));
  TTree* _tree2 = (TTree*)root2->Get(treename);
  if (!_tree2) {
    cout << " Treename " << treename << " not found" << endl;
    return;
  }

  TString branch1=l1coll+module1+varString+process1+".obj."+dist+"()";  TString cut1="";
  TString branch2=l1coll+module2+varString+process2+".obj."+dist+"()";  TString cut2="";
  
  if (dist=="eta"){
  cut1=l1coll+module1+varString+process1+".obj.et()>20";
  cut2=l1coll+module2+varString+process2+".obj.et()>20";

  }
  cout << "branch1: " << branch1 << " Cut1: "<< cut1 << endl;
  cout << "branch2: " << branch2 << " Cut2: "<< cut2 << endl;

  _tree1->Project(hname1,branch1,cut1);
  _tree2->Project(hname2,branch2,cut2);

  TCanvas *c1= new TCanvas("c1","Root Canvas 1");

  if (myHists.getYmax() > 0.){
    h1->GetYaxis()->SetRangeUser(myHists.getYmin(),myHists.getYmax());
    h2->GetYaxis()->SetRangeUser(myHists.getYmin(),myHists.getYmax());
  }
  h1->Rebin(rebin);
  h2->Rebin(rebin);
  h1->Draw();
  h2->Draw("sames");
  // hL1T->Draw();
 
  Double_t xl1=.2, yl1=0.16, xl2=xl1+.2, yl2=yl1+.1;
  TLegend *leg = new TLegend(xl1,yl1,xl2,yl2);

  leg->SetTextSize(.03);
  leg->AddEntry(h1,label1,"pl");   // h1 and h2 are histogram pointers
  leg->AddEntry(h2,label2,"pl");
  leg->Draw();

  TLatex *t = new TLatex();
  Int_t txtalign=13;
  Float_t xtxt=.605, ytxt=.8;
  t->SetNDC();
  t->SetTextAlign(txtalign);
  //t->SetTextFont(txtfnt);
  //t->SetTextSizePixels(txtsize);
  t->DrawLatex(xtxt,ytxt,L1Obj);

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
 
    // cout << " x1: " << x1 << " x2:" << x2 << endl;
    // cout << " y1: " << y1 << " y2:" << y2 << endl;
 
    tt1->SetY2NDC(y2);        tt1->SetX2NDC(x2);
    tt1->SetY1NDC(y2-dy);     tt1->SetX1NDC(x2-dx);
 
    tt2->SetY2NDC(y2);      tt2->SetX2NDC(x2-dx);
    tt2->SetY1NDC(y2-dy);   tt2->SetX1NDC(x2-2*dx);
    gPad->Modified();   
  }// modify statboxes 
 
 
 //gROOT->Reset();

}
