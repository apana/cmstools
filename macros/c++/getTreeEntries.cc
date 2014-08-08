#include "rootfuncs.h"
#
#  usage: root -l -b -q 'getTreeEntries.cc("HLToutput/mc-onsel-120_PU_Photon_Jets_pt_50_80-HLT2_001.root",false)'
#
void getTreeEntries(char* filename, bool fromdCache=false){

  if (fromdCache){
    TFile *rootfile=OpenRootFile(filename); if (!rootfile) return;
  }else{
    TFile *rootfile=OpenDCacheFile(filename); if (!rootfile) return;
  }
  cout << "\n";
  // rootfile->GetListOfKeys()->Print();

  TTree *srctree = dynamic_cast<TTree*>(rootfile->Get("Events")); // TTree name is "Events"
  if (srctree)
    cout << "Number of Events: " << srctree->GetEntries() << endl;
}
