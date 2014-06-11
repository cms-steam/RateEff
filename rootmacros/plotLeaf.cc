#include "rootfuncs.h"

void plotLeaf(){

 gROOT->Reset();
 gStyle->SetOptTitle(1);
 gStyle->SetOptStat(1);
 //gStyle->SetTitleOffset(0.8,"y");
 gStyle->SetOptLogy(0);

 //gStyle->SetTitleSize(0.05,"y");
 //gStyle->SetTitleSize(0.05,"x");

 //gStyle->SetLabelSize(0.04,"y");
 //gStyle->SetLabelSize(0.045,"x");

 //gStyle->SetHistFillColor(kYellow);
 gStyle->SetOptLogy(1);
 gROOT->ForceStyle();

 //TString myVar     = "ohEleClusShapLW";
 //TString myVar     = "ohEleDetaLW";
 //TString myVar     = "ohHighestEnergyHFRecHit";
 TString myVar     = "ohHighestEnergyHBHERecHit";

 TString treename  = "HltTree";
 TString rootname = "/uscmst1b_scratch/lpc1/lpctrig/apana/data/MinBias/lumi8e29/Summer08_MinBias_hltanalyzer_redoL1_StartupV8_L1StartupMenu_21.root";

 TFile *rootfile=OpenRootFile(rootname); if (!rootfile) return;
 //rootfile->GetListOfKeys()->Print();
 
 int nbins=25;
 float min=-0, max=100;

 string hname1= myVar + "_1", hname2=myVar +"_2";
 TH1F *h1 = new TH1F("leaf1",hname1.c_str(),nbins,min,max);

 
 TTree *_tree = dynamic_cast<TTree*>(rootfile->Get(treename));
 if (!_tree) {
    cout << " Treename " << treename << " not found" << endl;
    return;
  }

 _tree->Project("leaf1",myVar);

 TCanvas *c1= new TCanvas("c1","Root Canvas 1");

 h1->Draw();



 //gROOT->Reset();

}
