{
   TStyle *myStyle  = new TStyle("MyStyle","My Default Style File");

   // from ROOT plain style

   myStyle->SetOptTitle(0);
   myStyle->SetOptLogy(0);
   myStyle->SetOptStat(0);
   myStyle->SetPalette(1);

   myStyle->SetPadTopMargin(0.02);
   myStyle->SetPadTickX(1);

   myStyle->SetCanvasBorderMode(0);
   myStyle->SetPadBorderMode(0);
   myStyle->SetPadColor(0);
   myStyle->SetCanvasColor(0);
   myStyle->SetTitleColor(1);
   myStyle->SetStatColor(0);

   myStyle->SetFrameFillColor(0);

   // myStyle->SetLabelSize(0.03,"xyz"); // size of axis values
   myStyle->SetLabelSize(0.045, "XYZ");
   myStyle->SetLabelSize(0.04, "Y");
   myStyle->SetTitleSize(0.05, "XYZ");

   // default canvas positioning
   myStyle->SetCanvasDefX(750);
   myStyle->SetCanvasDefY(20);
   myStyle->SetCanvasDefH(520);
   myStyle->SetCanvasDefW(500);

   myStyle->SetPadBottomMargin(0.1);
   myStyle->SetPadTopMargin(0.1);
   myStyle->SetPadLeftMargin(0.1);
   myStyle->SetPadRightMargin(0.1);


   myStyle->SetPadTickX(1);
   myStyle->SetPadTickY(1);

   myStyle->SetFrameBorderMode(0);

   myStyle->SetHistMinimumZero(); // take out suppressed zero's

   // US letter
   myStyle->SetPaperSize(20, 24);
}
