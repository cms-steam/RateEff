{
gROOT->Reset();
   TCanvas c1("c1","multipads",900,700);
   gStyle->SetPadBorderMode(0);
   Float_t small = 1e-5;
   c1.Divide(2,2,small,small);
   TH2F h1("h1","test1",10,0,1,20,-1,1);
   TH2F h2("h2","test2",10,0,1,20,-1,1);
   TH2F h3("h3","test3",10,0,1,20,-1,1);
   TH2F h4("h4","test4",10,0,1,20,-1,1);

   c1.cd(1);
   gPad->SetBottomMargin(small);
   gPad->SetRightMargin(small);
   h1.Draw();

   c1.cd(2);
   gPad->SetBottomMargin(small);
   gPad->SetRightMargin(small);
   gPad->SetLeftMargin(small);
   h2.Draw();
   
   c1.cd(3);
   gPad->SetTopMargin(small);
   gPad->SetRightMargin(small);
   h3.Draw();

   c1.cd(4);
   gPad->SetTopMargin(small);
   gPad->SetRightMargin(small);
   gPad->SetLeftMargin(small);
   h4.Draw();
}
