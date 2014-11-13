////////////////////////////////////////////////////////////////////////////////////////
//
//  Simple L1 Emulator plotting macro
//
///////////////////////////////////////////////////////////////////////////////////////

// TString rootname = "../../../../L1Trigger/L1TCalorimeter/test/SimL1Emulator_Stage1_PP.root";
TString rootname = "SimL1Emulator_Stage1_PP.root";

TString Var; // Which Distribution to plot

// Var        = "IsolatedEG";
// Var        = "RelaxedEG";
Var        = "IsoTau";
// Var        = "RlxTau";
// Var        = "Jet";
// Var        = "MET";
// Var        = "MHT";
// Var        = "SET";
// Var        = "SHT";
// not available Var        = "HfRingEtSums";


class SetupHistos
{
public:
  //constructor
  SetupHistos(TString Distribution )
  {
    std::cout << "Plotting " << Distribution << " Distribution"<< std::endl;
    cutString_="";
    theObject_="";
    subColl_="";
    rebin_=1; xmin_=0.; xmax_=1000.; ymin_=0.1; ymax_=-1; 
    if (Distribution == "IsoTau" || Distribution == "RlxTau"){
      nbins_=64;
      xmax_=256;
      theObject_="l1tTauBXVector";
      if (Distribution == "IsoTau"){
	subColl_="isoTaus";
      } else{
	subColl_="rlxTaus";
      }
    } else if (Distribution == "RelaxedEG" || Distribution == "IsolatedEG"){
      nbins_=64;
      xmax_=64;
      rebin_=4;
      theObject_="l1tEGammaBXVector";
      if (Distribution == "RelaxedEG"){
	cutString_=theObject_ + "_caloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.hwIso()==0";
      }else{
	cutString_=theObject_ + "_caloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.hwIso()==1";
      }
    } else if ( Distribution == "MET" || Distribution == "MHT" || Distribution == "SET" || Distribution == "SHT"){ 
      theObject_="l1tEtSumBXVector";
      nbins_=201;
      rebin_=5;
      if (Distribution == "MET"){
	xmax_=460;
	cutString_=theObject_ + "_caloStage1FinalDigis__L1TEMULATION.obj.data_.type_==2";
      }else if (Distribution == "MHT") {
	//xmin_=0.0;
	//xmax_=101.;
	xmin_=0.0;
	xmax_=1.01;
	rebin_=1;
	cutString_=theObject_ + "_caloStage1FinalDigis__L1TEMULATION.obj.data_.type_==3";
	// cutString_=cutString_ + " && " + theObject_ + "_caloStage1FinalDigis__L1TEMULATION.obj.data_.hwQual()==1";
      }else if ( Distribution == "SET"){
	xmax_=1200;
	cutString_=theObject_ + "_caloStage1FinalDigis__L1TEMULATION.obj.data_.type_==0";
      }else if (Distribution == "SHT"){ 
	xmax_=1200;
	cutString_=theObject_ + "_caloStage1FinalDigis__L1TEMULATION.obj.data_.type_==1";
      }
    } else if ( Distribution == "Jet"){ 
      xmax_=300;
      nbins_=100;
      rebin_=5;
      theObject_="l1tJetBXVector";
    } else if ( Distribution == "HfRingEtSums"){ 
      xmax_=60;
      nbins_=60;
      rebin_=1;

    }

    nbins_=21;
    xmin_=0;
    xmax_=21.;
    //xmin_=-5.;
    //xmax_=5.;
    varString_= theObject_ + "_caloStage1FinalDigis_"+ subColl_ +"_L1TEMULATION.obj.data_.l1t::L1Candidate.hwEta()";
    cutString_= theObject_ + "_caloStage1FinalDigis_"+ subColl_ +"_L1TEMULATION.obj.data_.l1t::L1Candidate.hwPt()>10.";
    // varString_= theObject_ + "_caloStage1FinalDigis__L1TEMULATION.obj.data_.l1t::L1Candidate.hwPhi()";
    // varString_= theObject_ + "_caloStage1Digis__L1TEMULATION.obj.data_.l1t::L1Candidate.hwPt()";
    // cutString_="l1tTauBXVector_caloStage1FinalDigis_isoTaus_L1TEMULATION.obj.@data_.size()<5";

    hname_= Distribution + "_L1Emu";
    h_ = new TH1F(hname_,hname_,nbins_,xmin_,xmax_);
    h_->Sumw2();
    h_->SetLineColor(kBlue);

    std::cout<< "\tVar: " << varString_ << std::endl;
    std::cout<< "\tCut: " << cutString_ << std::endl;
  }
  ~SetupHistos(){}

  int getNbins() const {return nbins_; }
  int getRebin() const {return rebin_; }
  float getYmax() const {return ymax_;}
  float getYmin() const {return ymin_;}
  TString getVarString() const {return varString_; }
  TString getCutString() const {return cutString_; }
  TH1F *getHist() {return h_;}
private:

  int nbins_, rebin_;
  float xmin_, xmax_;
  float ymin_, ymax_;

  TString hname_, varString_, cutString_, theObject_, subColl_;
  TH1F *h_;

};

void plotL1EmuLeaf(){

  gROOT->LoadMacro("tdrstyle.C");
  setTDRStyle();
  gStyle->SetOptTitle(1);
  gStyle->SetOptStat(1);
  TH1::SetDefaultSumw2();

  TFile *rootfile = new TFile(rootname);if (!rootfile) return;
  //rootfile->GetListOfKeys()->Print();

  TTree *_tree = dynamic_cast<TTree*>(rootfile->Get("Events"));
  if (!_tree) {
    cout << " Events tree " << " not found" << endl;
    return;
  }

  SetupHistos myHists(Var);
  int nbins=myHists.getNbins();
  int rebin=myHists.getRebin();
  TH1F* h=myHists.getHist();
  TString hname=h->GetName();
  TString varString=myHists.getVarString();
  TString cutString=myHists.getCutString();

  _tree->Project(hname,varString,cutString); // fill the histogram
  int nent=_tree->GetEntries();
  cout << "Number of events on tree: " << nent << endl;
  TH1F *h_nent = new TH1F("Nentries","Number of Events processed",1,0.0,1.);
  h_nent->SetBinContent(1,nent);

  TCanvas *c1= new TCanvas("c1","Root Canvas 1");
  c1->SetLogy(true);

  h->Rebin(rebin);
  h->Draw();

  bool SaveOutput=false;
  if (SaveOutput){
    TString OutFile="l1Emulator_" + Var + ".root";
    TFile *of = new TFile(OutFile,"RECREATE");
    h->Write();
    h_nent->Write();
    of->Close();
  }

  //gROOT->Reset();

}
