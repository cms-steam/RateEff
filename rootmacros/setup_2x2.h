void SetupCanvas(){

  gStyle->SetOptTitle(0);
  gStyle->SetOptStat(0);
  gStyle->SetTitleOffset(0.8,"y");
  gStyle->SetTitleOffset(1.2,"x");
  gStyle->SetOptLogy(0);

  gStyle->SetTitleSize(0.05,"y");
  gStyle->SetTitleSize(0.05,"x");
  
  gStyle->SetLabelSize(0.04,"y");
  gStyle->SetLabelSize(0.045,"x");

  gStyle->SetHistFillColor(kYellow);

  gStyle->SetPadTopMargin(0.025);
  gStyle->SetPadRightMargin(0.025);

  TCanvas *c1 = new TCanvas("c1","Root Canvas",450,20,840,675); // My Default Canvas
  Int_t wtopx,wtopy; UInt_t ww, wh;
  c1->GetCanvasPar(wtopx,wtopy,ww,wh); // Gets Canvas Parameters
  //cout << wtopx << " " << wtopy << " " << ww << " " << wh << endl;
  //TCanvas *c2 = new TCanvas("c2","Root Canvas 2");
  //TCanvas *c3 = new TCanvas("c3","Root Canvas 3",2);

  pad1 = new TPad("pad1","This is pad1",0.0,0.5,0.5,1.00);
  pad2 = new TPad("pad2","This is pad1",0.5,0.5,1.00,1.00);
  pad3 = new TPad("pad3","This is pad3",0.0,0.0,0.5,0.5);
  pad4 = new TPad("pad4","This is pad4",0.5,0.0,1.00,0.5);

  pad1->UseCurrentStyle();
  pad2->UseCurrentStyle();
  pad3->UseCurrentStyle();
  pad4->UseCurrentStyle();

  bool useColor=false;
  useColor=true;
  if (!useColor){
    color=(TColor*)(gROOT->GetListOfColors()->At(kMagenta)); color->SetRGB(0,0,0);
  }
  // Set the right and left margins for all pads
  Double_t p1_lm=0.100, p3_lm=p1_lm;   // pad1 and 3 left margins
  Double_t p1_rm=0.05, p3_rm=p1_rm;   // pad1 and 3 right margins

  Double_t p2_lm=p1_rm, p4_lm=p1_rm;
  Double_t p2_rm=p1_lm, p4_rm=p1_lm;

  pad1->SetLeftMargin(p1_lm); pad1->SetRightMargin(p1_rm);
  pad2->SetLeftMargin(p2_lm); pad2->SetRightMargin(p2_rm);
  pad3->SetLeftMargin(p3_lm); pad3->SetRightMargin(p3_rm);
  pad4->SetLeftMargin(p4_lm); pad4->SetRightMargin(p4_rm);

  // Set the top and bottom margins for all pads
  Double_t p1_tm=0.125, p2_tm=p1_tm;   // pad1 and 2 top margins
  Double_t p1_bm=0.09, p2_bm=p1_bm;   // pad1 and 2 bottom margins

  Double_t p3_tm=p1_bm, p4_tm=p2_bm;
  Double_t p3_bm=p1_tm, p4_bm=p2_tm;

  pad1->SetTopMargin(p1_tm); pad1->SetBottomMargin(p1_bm);
  pad2->SetTopMargin(p2_tm); pad2->SetBottomMargin(p2_bm);
  pad3->SetTopMargin(p3_tm); pad3->SetBottomMargin(p3_bm);
  pad4->SetTopMargin(p4_tm); pad4->SetBottomMargin(p4_bm);

  pad1->Draw();
  pad2->Draw();
  pad3->Draw();
  pad4->Draw();

}
