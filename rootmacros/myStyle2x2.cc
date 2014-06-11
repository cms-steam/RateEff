{
   TStyle *myStyle2x2  = new TStyle("MyStyle2x2","My Style File for 2x2 plots");

   // from ROOT plain style
   myStyle->SetCanvasBorderMode(0);
   myStyle->SetPadBorderMode(0);
   myStyle->SetPadColor(0);
   myStyle->SetCanvasColor(0);
   myStyle->SetTitleColor(1);
   myStyle->SetStatColor(0);

   myStyle->SetLabelSize(0.03,"xyz"); // size of axis values

   // default canvas positioning
   myStyle->SetCanvasDefX(900);
   myStyle->SetCanvasDefY(20);
   myStyle->SetCanvasDefH(550);
   myStyle->SetCanvasDefW(540);

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
