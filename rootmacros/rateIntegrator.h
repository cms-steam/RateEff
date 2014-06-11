void rateIntegrator(TH1* hin, TH1* hout, float Lumi){

  Float_t dy=1.;  // take out average over rapidity

  Int_t nbins=hin->GetNbinsX();
  //cout << "Number of bins: " << nbins << endl;

//   for (Int_t ibin=0; ibin<nbins; ++ibin){
//     Float_t cont=h->GetBinContent(ibin+1);
//     Float_t err =h->GetBinError(ibin+1);
//     Float_t bw  =h->GetBinWidth(ibin+1);
//     bw=1.;

//     Float_t fact=bw*dy;

//     //cout << ibin << " " << cont << " +- " << err << " -- BinWidth: " << bw << endl;
//     cont=cont*fact;
//     err = err*fact;
    
//     h->SetBinContent(ibin+1,cont);
//     h->SetBinError(ibin+1,err);
//   }

  // now the integrated rate
  // error on rate is calculated assuming error on integral is dominated by current bin error
  bool doInt=true;

  for (Int_t ibin=0; ibin<nbins; ++ibin){
    Int_t ibin1=ibin+1;
    Int_t ibin2=nbins;

    Float_t cont =hin->GetBinContent(ibin+1);
    Float_t err  =hin->GetBinError(ibin+1);

    if (doInt){
      Float_t ferr=0.;
      if (cont>0.)ferr=err/cont;

      //Float_t fint=h->Integral(ibin1,ibin2,"width");
      Float_t fint=hin->Integral(ibin1,ibin2,"");

      //cout << ibin << "  -- Integral: " << fint << endl;
      cont=fint;
      err = ferr*fint;
    }
    hout->SetBinContent(ibin+1,cont);
    hout->SetBinError(ibin+1,err);
  }
  //cout << "  -- Integral: " << copy_h1->Integral() << endl;


  const float conv=1e-36; // conversion from pb to cm^2
  //const  float conv=1e-27; // conversion from mb to cm^2

  cout << "Calculating rate for Luminosity: " << Lumi << endl;
  // now multiply by luminosity to get total rate
  Float_t fact=Lumi*conv;

  //cout << fact << endl;
  //hout->Scale(fact);
}

TH1F* rateIntegrator(TH1* hin, float Lumi){


  TString newname=hin->GetName();
  newname = newname + "__cloned";
  TH1F* hout = (TH1F*)hin->Clone(); hout->SetName(newname);

  Float_t dy=1.;  // take out average over rapidity

  Int_t nbins=hin->GetNbinsX();
  //cout << "Number of bins: " << nbins << endl;

//   for (Int_t ibin=0; ibin<nbins; ++ibin){
//     Float_t cont=h->GetBinContent(ibin+1);
//     Float_t err =h->GetBinError(ibin+1);
//     Float_t bw  =h->GetBinWidth(ibin+1);
//     bw=1.;

//     Float_t fact=bw*dy;

//     //cout << ibin << " " << cont << " +- " << err << " -- BinWidth: " << bw << endl;
//     cont=cont*fact;
//     err = err*fact;
    
//     h->SetBinContent(ibin+1,cont);
//     h->SetBinError(ibin+1,err);
//   }

  // now the integrated rate
  // error on rate is calculated assuming error on integral is dominated by current bin error
  for (Int_t ibin=0; ibin<nbins; ++ibin){
    Int_t ibin1=ibin+1;
    Int_t ibin2=nbins;

    Float_t cont =hin->GetBinContent(ibin+1);
    Float_t err  =hin->GetBinError(ibin+1);
    
    Float_t ferr=0.;
    if (cont>0.)ferr=err/cont;

    //Float_t fint=h->Integral(ibin1,ibin2,"width");
    Float_t fint=hin->Integral(ibin1,ibin2,"");

    //cout << ibin << "  -- Integral: " << fint << endl;
    cont=fint;
    err = ferr*fint;
    
    hout->SetBinContent(ibin+1,cont);
    hout->SetBinError(ibin+1,err);
  }
  //cout << "  -- Integral: " << copy_h1->Integral() << endl;


  const float conv=1e-36; // conversion from pb to cm^2
  //const  float conv=1e-27; // conversion from mb to cm^2

  cout << "Calculating rate for Luminosity: " << Lumi << endl;
  // now multiply by luminosity to get total rate
  Float_t fact=Lumi*conv;

  //cout << fact << endl;
  hout->Scale(fact);

  return hout;

}
