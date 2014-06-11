// #include "rootfuncs.h"

// root -b -q 'printLeaves.cc("xxx.root","HltTree")'

void printEvents(const TString& rootfile="xxx.root", TString& treename="HltTree"){

  // cout << "\n Rootfile: " << rootfile << endl;
  // cout << " Treename: " << treename << endl;

  if( gSystem->AccessPathName(rootfile) ){
    cout << endl << " File: " << rootfile << " not found!!!" << endl << endl;
    return;
  }
  TFile *_file0=TFile::Open(rootfile);

  // _file0->GetListOfKeys()->Print();
  
  TTree *_tree = dynamic_cast<TTree*>(_file0->Get(treename));
  if (!_tree) {
    cout << " Treename " << treename << " not found" << endl;
    return;
  }

  cout << "Rootfile: " << rootfile << "  Events: " << _tree->GetEntries() << endl;
}

