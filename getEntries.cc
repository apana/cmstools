#include "rootfuncs.h"

void getEntries(char* filename){


  TFile *rootfile=OpenRootFile(filename); if (!rootfile) return;
  // TFile *rootfile=OpenDCacheFile(filename); if (!rootfile) return;
  cout << "\n";
  // rootfile->GetListOfKeys()->Print();
  TString hname="Nevents"; // From list of keys
  TH1F *h = (TH1F*)rootfile->Get(hname);
  if (h)
    cout << "\t" << filename << " Number of events processed: "<< h->GetBinContent(1) << endl;
}
