void IndRatePlots(const int nplots=1, const bool plotIt=false)
{
  gROOT->SetStyle("Plain");
  gStyle->SetPalette(1);
  gStyle->SetOptTitle(0);
  gStyle->SetPadTopMargin(0.02);
  gStyle->SetPadTickX(1);


  //TString filename = "hltmenu_data_nofltr.root"; Int_t color=kBlue; double max=5.5; double min=0.001;

  

  string lumi="4.0e29";
  string filename = "hltmenu_7TeV_" + lumi + "_startup_2010March27.root"; 

  TFile *f = TFile::Open(filename.c_str());

  Int_t color=kRed; double max=5.5; double min=0.001;

  TH1F *h2 = (TH1F *)f->Get("individual");
  h2->SetFillColor(color);
  Float_t label_s=0.03;
  h2->SetLabelSize(label_s,"x"); // axis label size
  h2->SetLabelSize(label_s,"y");
  h2->SetTitleSize(label_s,"y"); // axis label size

  TH1F *h3 = h2->Clone();

  Int_t wtopx=400,wtopy=20; UInt_t ww=800, wh=650;
  if (nplots==1){
    wtopx=600,wtopy=20;
    ww=860, wh=900;
  }

  TCanvas *c2 = new TCanvas("c2","c2",wtopx, wtopy, ww, wh);

  float bmargin=0.07;
  float rmargin=0.02;
  float lmargin=0.32;
  c2->SetBottomMargin(bmargin);
  c2->SetRightMargin(rmargin);
  c2->SetLeftMargin(lmargin);
  c2->SetLogx(0);

  // last is 51;

  int ilast=51, i2=51;
  if (nplots==2) i2=36;

  h2->GetXaxis()->SetRange(1,i2); 


  //h2->SetMaximum(max);
  //h2->SetMinimum(min);
  
  h2->Draw("hbar3");

  TLatex *t = new TLatex(); t->SetNDC();
  Double_t xtxt=0.85, ytxt=0.95;
  t->SetTextColor(kDarkGreen);
  t->SetTextAlign(23);
  t->SetTextSize(0.042);
  string label="L= " + lumi;
  t->DrawLatex(xtxt,ytxt,label.c_str());

  if (plotIt){
    string outfile="individual_" + lumi + "_jme";
    if (nplots==1) outfile="individual_" + lumi;

    outfile=outfile + ".gif";
    cout << "\nWriting file: " << outfile << endl;
    c2->Print(outfile.c_str());
    //c2->Refresh();
  }

  if (nplots ==1) return;

  TCanvas *c3 = new TCanvas("c3","c3",400,300,600,450);

  
  h3->GetXaxis()->SetRange(i2+1,ilast); 

  float bmargin=0.1;
  float rmargin=0.02;
  float lmargin=0.3;
  c3->SetBottomMargin(bmargin);
  c3->SetRightMargin(rmargin);
  c3->SetLeftMargin(lmargin);
  c3->SetLogx(0);
  h3->Draw("hbar3");

  //c1->Refresh();

  if (plotIt){
    string outfile="individual_" + lumi + "_minbplus";
    outfile=outfile + ".gif";
    cout << "\nWriting file: " << outfile << endl;
    c3->Print(outfile.c_str());
  }

}
