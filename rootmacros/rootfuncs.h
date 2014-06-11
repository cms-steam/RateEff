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

TFile* OpenDCacheFile(const TString& rootfile) {

  cout << "Rootfile: " << rootfile << endl;

  TFile *file;
  if( gSystem->AccessPathName(rootfile) ){
    cout << endl << "File: " << rootfile << " not there!!!" << endl << endl;
    file=0;
  }
  else
    file = new TDCacheFile(rootfile,"READ","Demo ROOT file with histograms",0);

  return file;
}

bool hExist(TFile *file,const TString& hname){

  bool retval=true;

  TKey *key = file->FindKey(hname);
  if (key ==0){
    cout << "!!Histogram " << hname << " does not exist!!" << endl;
    retval=false;
  }
  return retval;
}

TH1F* GetHist(TFile* file,const TString& hname){

  TH1F* h=0;
  if (hExist(file,hname)){
    h=(TH1F*)file->Get(hname);
  }

  return h;
}

TH2* GetHist2D(TFile* file,const TString& hname){

  TH2* h=0;
  if (hExist(file,hname)){
    h=(TH2F*)file->Get(hname);
  }

  return h;
}

TH2* get2DHist(TFile* file, const TString& subdir,const TString& hname, bool listDir=false){

  //cout << "Subdirectory " << subdir << endl;
  //gDirectory->pwd();
  file->cd(subdir);
  if (listDir)
    gDirectory->ls();


  TH2F *h; 
  gDirectory->GetObject(hname,h);
  
  if (!h) {
    cout << "Histogram with name " << hname << " not found" << endl;
  }
  return h;

}

TH1* get1DHist(TFile* file, const TString& subdir,const TString& hname, bool listDir=false){

  //cout << "Subdirectory " << subdir << endl;
  //gDirectory->pwd();
  file->cd(subdir);

  if (listDir)
    gDirectory->ls();

  TH1F *h; 
  gDirectory->GetObject(hname,h);

  if (!h) {
    cout << "Histogram with name " << hname << " not found" << endl;
  }
  return h;

}

void mySetup(int ilogy=0){
  gROOT->Reset();
  gStyle->SetOptTitle(0);
  gStyle->SetOptStat(0);
  gStyle->SetTitleOffset(1.1,"y");
  
  gStyle->SetHistLineWidth(2);
  
  //gStyle->SetTitleSize(0.05,"y");
  //gStyle->SetTitleSize(0.05,"x");
  
  //gStyle->SetLabelSize(0.04,"y");
  //gStyle->SetLabelSize(0.045,"x");
  
  gStyle->SetHistFillColor(kYellow);
  gStyle->SetOptLogy(ilogy);
  gROOT->ForceStyle();

  return;

}

void divideByBinWidth(TH1* h){

  Int_t nbins=h->GetNbinsX();
  //cout << "Number of bins: " << nbins << endl;

  for (Int_t ibin=0; ibin<nbins; ++ibin){

     Float_t cont=h->GetBinContent(ibin+1);
     Float_t err =h->GetBinError(ibin+1);
     Float_t bw  =h->GetBinWidth(ibin+1);

     cont=cont/bw;
     err=err/bw;

     h->SetBinContent(ibin+1,cont);
     h->SetBinError(ibin+1,err);
  }
}

void scaleErrors(TH1* h, const double fact){

  Int_t nbins=h->GetNbinsX();
  //cout << "Number of bins: " << nbins << endl;
  cout << "Scale Factor: " << fact << endl;
  for (Int_t ibin=0; ibin<nbins; ++ibin){

     Float_t err =h->GetBinError(ibin+1);
     err=err*fact;

     h->SetBinError(ibin+1,err);
  }
}


void printLeaves(const TString& rootname="xxx.root", const TString& treename="HltTree" ){

  //rootfile=OpenRootFile(rootname); if (!rootfile) return;
  TFile *_file0=TFile::Open(rootname);
  // _file0->GetListOfKeys()->Print();
  
  TTree *_tree = dynamic_cast<TTree*>(_file0->Get(treename));
  TObjArray *leaves = _tree->GetListOfBranches();
  Int_t leafEnts=leaves->GetSize();

  cout << "Number of leaves: " << leafEnts << endl;

  for(Int_t i = 0; i < leafEnts; i++){
    std::string leafName = leaves->At(i)->GetName(); 
    cout << "\t" <<leafName << "\n";
  }  

  cout << "\nDone" << endl;
}

TString chInt(const int& value){
  TString conv="xxx";

  ostringstream ch_val("");
  
  ch_val << value;
  conv=ch_val.str();

  return conv;
}
