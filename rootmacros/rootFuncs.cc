//
//
//
#include <iostream>
#include <TROOT.h>
#include <TSystem.h>
#include <TString.h>
#include <TChain.h>
#include <TFile.h>
#include <TTree.h>
#include <TH1.h>
#include "TF1.h"

TFile* OpenRootFile(const TString& rootfile) {

  cout << "Rootfile: " << rootfile << endl;

  TFile *file=0;
  if( gSystem->AccessPathName(rootfile) ){
    cout << endl << "File: " << rootfile << " not there!!!" << endl << endl;
    file=0;
  }
  else
    file = new TFile(rootfile);

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

TH1* GetHist(TFile* file,const TString& hname){

  TH1* h=0;
  if (hExist(file,hname)){
    h=(TH1F*)file->Get(hname);
  }

  return h;
}

Int_t writeIt(Int_t ips=0)
{
  std::cout << "Inside writeIt ips= " << ips << std::endl;
  //  printf("Inside writeIt\n"); 
  return 0;
}

Int_t wait_fcn(Int_t iwait=0)
{
  const int cLen = 40;
  char cpause[cLen];
  string answer;

  std::cout << "Inside wait function iwait= " << iwait << std::endl;
  if (iwait == 0) return 0;

  string wait_string=
    "Hit return to continue, q to quit, b to break out of loop";;
  std::cout << wait_string << std::endl;

  std::cin.getline(cpause, cLen);
  std::cout << "Value: " << cpause << std::endl;
  answer = cpause;

  if (answer == "q") return 1;
  if (answer == "b") return 2;

  return 0;
}
