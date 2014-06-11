#include "rootfuncs.h"

void compLeaves(){

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

 TString myVar     = "L1NIsolEmEt";

 TString treename  = "HltTree";
 TString rootname1 = "HLTAnalyzer_gtNone.root";
 TString rootname2 = "HLTAnalyzer_gtDigis.root";
 //TString rootname2 = "HLTAnalyzer_test.root";

 TFile *rootfile1=OpenRootFile(rootname1); if (!rootfile1) return;
 rootfile1->GetListOfKeys()->Print();
 TFile *rootfile2=OpenRootFile(rootname2); if (!rootfile2) return;
 
 int nbins=25;
 float min=0., max=25.;

 string hname1= myVar + "_1", hname2=myVar +"_2";
 TH1F *h1 = new TH1F("leaf1",hname1.c_str(),nbins,min,max);
 TH1F *h2 = new TH1F("leaf2",hname2.c_str(),nbins,min,max);

 
 TTree *_tree1 = dynamic_cast<TTree*>(rootfile1->Get(treename));
 if (!_tree1) {
    cout << " Treename " << treename << " not found" << endl;
    return;
  }

 TTree *_tree2 = dynamic_cast<TTree*>(rootfile2->Get(treename));
 if (!_tree2) {
    cout << " Treename " << treename << " not found" << endl;
    return;
  }

 _tree1->Project("leaf1",myVar);
 _tree2->Project("leaf2",myVar);

 TH1F *rat = (TH1F*)h1->Clone(); rat->SetName("ratio");
 rat->Divide(h2,h1,1.,1.,"");

 Double_t minpt=min,maxpt=max;
 //Double_t minpt=-5,maxpt=5;

 h1->SetLineColor(kRed);
 h1->GetXaxis()->SetRangeUser(minpt,maxpt);
 h2->GetXaxis()->SetRangeUser(minpt,maxpt);
 //h1->GetXaxis()->SetTitle("p_{T} (GeV)");
 //h2->GetXaxis()->SetTitle("p_{T} (GeV)");

 h1->SetTitleSize(.05,"x");

 TCanvas *c1= new TCanvas("c1","Root Canvas 1");

 h1->Draw();
 h2->Draw("same");


 Int_t wtopx,wtopy; UInt_t ww, wh;
 c1->GetCanvasPar(wtopx,wtopy,ww,wh); // Gets Canvas Parameters 
 TCanvas *c2 = new TCanvas("c2","Root Canvas 2",20, wtopy, ww, wh);
 gPad->SetLogy(0);
 
 Double_t ymin=0,ymax=1.5;
 rat->GetXaxis()->SetRangeUser(minpt,maxpt);
 rat->GetYaxis()->SetRangeUser(ymin,ymax);

 rat->Draw();


 //gROOT->Reset();

}
