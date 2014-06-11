#include "rootfuncs.h"

TH1F* makeEff(TFile* rootfile,const TString& TrigDir,const TString& num,const TString& den, const double& xmin=0, const double& xmax=0, const double& ymin=0., const double& ymax=1000., const int& irebin=1){


  cout << "Numerator:   " << num << endl;
  cout << "Denominator: " << den << endl;

  TString subdir=TrigDir;

  bool listdir=false;
  TH1F *hnum= get1DHist(rootfile,subdir,num,listdir);
  TH1F *hden= get1DHist(rootfile,subdir,den,listdir);

  TH1F *h1 = (TH1F*)hnum->Clone();
  TH1F *h2 = (TH1F*)hden->Clone();

  int n1=h1->GetEntries();
  int n2=h2->GetEntries();
  if (n1 == 0) cout << "Problem! Number of Entries in Num: " << n1 << endl;
  if (n2 == 0) cout << "Problem! Number of Entries in Den: " << n2 << endl;

  if (irebin > 1){
    h1->Rebin(irebin);
    h2->Rebin(irebin);
  }

  h1->Sumw2(); h2->Sumw2();


  TH1F *eff = (TH1F*)h1->Clone(); eff->SetName("TriggerEff");
  eff->Divide(h1,h2,1.,1.,"B");  

  eff->GetXaxis()->SetRangeUser(xmin,xmax);
  eff->GetYaxis()->SetRangeUser(ymin,ymax);

  return eff;
}


TH1F* makeEff(TH1D* hnum, TH1D *hden, const double& xmin=0, const double& xmax=0, const double& ymin=0., const double& ymax=1000., const int& irebin=1){

  TH1F *h1 = (TH1F*)hnum->Clone();
  TH1F *h2 = (TH1F*)hden->Clone();

  int n1=h1->GetEntries();
  int n2=h2->GetEntries();
  if (n1 == 0) cout << "Problem! Number of Entries in Num: " << n1 << endl;
  if (n2 == 0) cout << "Problem! Number of Entries in Den: " << n2 << endl;

  if (irebin > 1){
    h1->Rebin(irebin);
    h2->Rebin(irebin);
  }

  h1->Sumw2(); h2->Sumw2();


  TH1F *eff = (TH1F*)h1->Clone(); eff->SetName("TriggerEff");
  eff->Divide(h1,h2,1.,1.,"B");  

  eff->GetXaxis()->SetRangeUser(xmin,xmax);
  eff->GetYaxis()->SetRangeUser(ymin,ymax);

  return eff;
}
