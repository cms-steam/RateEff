from ROOT import gROOT, gStyle, gSystem, TCanvas, TF1, TFile, TH1F, TPad, TGraphErrors
from ROOT import TColor, TLine, TLegend, TLatex
from ROOT import SetOwnership

import sys,string,math,os,ROOT
ROOT.gROOT.SetBatch(ROOT.kTRUE)

from array import array
sys.path.append(os.path.join(os.environ.get("HOME"),'rootmacros'))
from myPyRootSettings import prepPlot
from myPyRootMacros import GetHist, PrepLegend, drawErrorBarsUser, DrawText

from DataSets_MC_noprescl import DataSets

theLabels=["QCD15to30","QCD30to50","QCD50to80","QCD80to120","QCD120to170","QCD170to300","QCD300to470","QCD470to600","QCD600to800","QCD800to1000","EMEnr30to80","EMEnr80to170","WToENu","ZToEE","WToMuNu","ZToMuMu"]

DoAll=True

#UseLowPTQCD=False
UseLowPTQCD=True

UseEnriched=True
## UseEnriched=False

vsn1 = '721_withEff'
vsn2 = '721_WithPU'

INPUTDIR='RatePerSample'
#INPUTDIR2='700'


if DoAll:
    WhichDS = sys.argv[1]
else:
    ## WhichDS="METParked"

    #WhichDS="MET"
    #WhichDS="SingleElectron"
    #WhichDS="SingleMu"
    #WhichDS="HTMHT"
    #WhichDS="DoublePhoton"
    #WhichDS="DoublePhotonHighPt"
    WhichDS="All"
    #WhichDS="SinglePhoton"

    #WhichDS="JetHT"

    #WhichDS="DoubleElectron"
    #WhichDS="PhotonHad"
    #WhichDS="MultiJet"
    #WhichDS="MuHad"
    #WhichDS="MuOnia"

    #WhichDS="BTag"
    #WhichDS="ElectronHad"


    #WhichDS="TauPlusX"
    #WhichDS="Tau"
    #WhichDS="BJetPlusX"
    #WhichDS="MuEG"
    #WhichDS="noprescl"

    ## WhichDS="MuEGTauPlusXBJetPlusX"

logx=True
#logx=False
## used to determine which lumi to scale to
## run="207884" 
run="207889" 

writePlot=True
# suffix="_MuEnr.gif"
suffix=".png"

lumiLen=23.3  # length (in seconds) of a lumi section

#===============================================================

def OpenFile(file_in,iodir):
    """  file_in -- Input file name
         iodir   -- 'r' readonly  'r+' read+write """
    try:
        ifile=open(file_in, iodir)
        # print "Opened file: ",file_in," iodir ",iodir
    except:
        print "Could not open file: ",file_in
        sys.exit(1)
    return ifile

def CloseFile(ifile):
    ifile.close()


def prep2by1Plot(cname,ctitle,wtopx=300,wtopy=20,ww=840,wh=500):

    c = TCanvas(cname,ctitle,wtopx,wtopy,ww,wh)
    SetOwnership(c,1 )

    bmargin=0.075
    rmargin=0.02
    lmargin=0.45
    tmargin=0.01
    
                                    ## xlow ylow xup yup
    pad1 = TPad("pad1","This is pad1",0.0,0.0,0.74,1.0);
    pad2 = TPad("pad2","This is pad1",0.74,0.0,1.0,1.0);

    # pad1 = TPad("pad1","This is pad1",0.0,0.0,0.8,1.0);
    # pad2 = TPad("pad2","This is pad1",0.8,0.0,1.0,1.0);


    pad1.SetTopMargin(0.02);
    pad1.SetBottomMargin(0.1);
    pad2.SetTopMargin(0.02);
    pad2.SetBottomMargin(0.1);

    rmargin=0.005
    pad1.SetRightMargin(rmargin);
    pad2.SetRightMargin(rmargin);

    lmargin=0.025
    pad1.SetLeftMargin(lmargin);
    lmargin=0.01
    pad2.SetLeftMargin(lmargin);

    SetOwnership(pad1,1 )
    SetOwnership(pad2,1 )

    c.SetBottomMargin(bmargin);
    c.SetRightMargin(rmargin);
    c.SetLeftMargin(lmargin);
    c.SetTopMargin(tmargin);

    c.SetLogy(0);
    c.SetLogx(0);

    return c,pad1,pad2

if __name__ == '__main__':

    if DoAll and len(sys.argv) < 2:
        print 'Usage: ' + sys.argv[0] + ' whichds'
        sys.exit() 

    gROOT.Reset()
    #gROOT.SetStyle("MyStyle");    
    #gROOT.SetStyle("tdrStyle");    
    gROOT.SetStyle("Plain");    
    gStyle.SetOptLogy(0);
    gStyle.SetPalette(1);
    gStyle.SetOptTitle(0);
    gStyle.SetOptStat(0);
    gStyle.SetOptFit(0);
    gStyle.SetPadTopMargin(0.02);
    gStyle.SetPadTickX(1);

    gStyle.SetLabelSize(0.035, "XYZ");
    gStyle.SetLabelSize(0.035, "Y");
    gStyle.SetTitleSize(0.05, "XYZ");


    if DataSets.has_key(WhichDS)==0:
        print "Could not dataset find",WhichDS," in dictionary"
        sys.exit(1)


    print "XXXXXXXXXXXXXXXXX -- ",INPUTDIR
    MCFile1 = os.path.join(INPUTDIR,"hltmenu_13TeV_25ns_combinedRate_1.4e+34_" + WhichDS + '_' + vsn1 + ".root")
    MCFile2 = os.path.join(INPUTDIR,"hltmenu_13TeV_25ns_combinedRate_1.4e+34_" + WhichDS + '_' + vsn2 + ".root")

    ScaleMC=1.

    

    theTriggers=DataSets[WhichDS]
    outDir="newplots/RatePerSample/15to1000wandwoutSilviosCorr/withEff"
    if not os.path.exists(outDir):
        os.makedirs(outDir)    
    for trig in theTriggers:

        hname=trig[:trig.rfind("_v")]
        #if hname == 'HLT_LooseIsoPFTau50_Trk30_eta2p1' or hname == 'HLT_Mu3er_PFHT140_PFMET125_NoiseCleaned' or hname == 'HLT_RsqMR300_Rsq0p09_MR200' or hname == 'HLT_RsqMR300_Rsq0p09_MR200_4jet' or hname == 'HLT_Rsq0p36' or hname == 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL' or hname == 'HLT_JetE30_NoBPTX3BX_NoHalo' or hname == 'HLT_JetE30_NoBPTX' or hname == 'HLT_JetE50_NoBPTX3BX_NoHalo': continue
        print "studying ", hname
        hist1=GetHist(MCFile1,hname)
        hist1.SetFillColor(ROOT.kRed-7)
        hist2=GetHist(MCFile2,hname)
        hist2.SetFillColor(ROOT.kBlue)
        print vsn1,hist1.GetEntries(), vsn2, hist2.GetEntries()

        count = 0
        for b in range(0,int(hist1.GetEntries())):
            #print "b ", b, " " , hist1.GetBinContent(b)
            if hist1.GetBinContent(b) == 0.:
                count += 1
        #print "count of bins with zero rate: ", count
        if count == hist1.GetEntries(): continue

        outplot= WhichDS +"_"+hname
        outfile=os.path.join(outDir,outplot)
        print outfile+suffix
        
    ### CCLA defaults
        labelsz=0.033
        lmargin=0.5
        hmax=-1.
        hmin=0.0001
    
        xl1=.02; 
        if not logx:
            xl1=.02
        yl1=.01+.1; 

        rmax=10.

        hist2.GetYaxis().SetLabelSize(.03);
        hist2.GetYaxis().SetTitleSize(0.035);
        hist2.GetYaxis().SetTitle("Rate (Hz)");
        hist2.GetYaxis().SetTitleOffset(.95);
        hist2.GetYaxis().SetLabelOffset(-.005);
        hist2.GetXaxis().SetLabelSize(labelsz);
        hist1.GetXaxis().SetLabelSize(labelsz);

        hist1.GetXaxis().SetTitle("Sample");
        hist2.GetXaxis().SetTitleOffset(0.11);

        minRate=0.09
        hist2.SetMinimum(hmin)
        if hmax>-1.:
            hist2.SetMaximum(hmax)

        hist2.SetBarWidth(0.45);
        hist2.SetBarOffset(0.0);
        hist1.SetBarWidth(0.45);
        hist1.SetBarOffset(0.45);

   

    ## c1=prepPlot()
        ylow=900
        c1,p1,p2=prep2by1Plot("c1","700 and 53X Comparison",575, 31, 1250, ylow)
        p1.Draw()
        p2.Draw()

        p1.cd()

        if logx:
            p1.SetLogx(True)
        p1.SetLeftMargin(lmargin)

        hist2.Draw("hbar2");
        hist1.Draw("hbar2,e,same");

        i1=1
        i2=hist1.GetNbinsX()
        print "minbin=",i1," maxbin=",i2
        drawErrorBarsUser(p1,hist1,i1,i2,0.15,minRate)
        drawErrorBarsUser(p1,hist2,i1,i2,-0.25,minRate)
        ## drawErrorBars(p1,h2,-0.15)


        xl2=xl1+.2; yl2=yl1+.085;
        leg =TLegend(xl1,yl1,xl2,yl2);
        leg.SetFillColor(0);
        leg.SetLineColor(0);
        leg.SetShadowColor(0);

        la=ROOT.TLatex()
        la.SetNDC()
        la.SetTextAlign(11)
        la.SetTextSize(0.026)
        
        header=hname
        xt=xl1-.01; yt=yl1+0.85
        la.DrawLatex(xt,yt, header);
        la.DrawLatex(xt,yt-0.03, "L=1.4e34 Hz/cm^{2}");
        if not UseLowPTQCD:
            la.DrawLatex(xt,yt-0.03-0.03, "no 15-30 PT QCD");
        if UseLowPTQCD:
            la.DrawLatex(xt,yt-0.03-0.03, "with 15-30 PT QCD");
            
        if not UseEnriched:
            la.DrawLatex(xt+0.2,yt-0.03-0.03, "no Enriched QCD");



        #leg.AddEntry(hist2,"62XMC-HLT700-Frozen2013","f");
        #leg.AddEntry(hist1,"53XMC-HLT53X-8e33V2","f");
        leg.AddEntry(hist1,"62XMC-HLT721 with Filter","f");
        leg.AddEntry(hist2,"62XMC-HLT721 no Filter","f");
        leg.SetTextSize(0.026);    
        leg.Draw();


        p1.Modified()
        p1.Update()


        p2.cd()


    ### now Ratio
        hRat=hist1.Clone();
    ## hRat.SetName("8TeV/13TeV")
    ## hRat.Divide(h1,h2,1.,1.,"");

        hRat.SetName("Ratio wFilt/noFilt")
        hRat.Divide(hist1,hist2,1.,1.,"");

    ## hRat.GetYaxis().SetTitle("8TeV/13TeV");
        hRat.GetYaxis().SetTitle("Ratio wFilt/noFilt");
        hRat.GetYaxis().SetTitleOffset(.3);
        hRat.GetYaxis().SetLabelOffset(-.05);

        print labelsz*2.1
        hRat.GetYaxis().SetLabelSize(0.07);
        hRat.GetYaxis().SetTitleSize(0.085);

        hRat.SetBarOffset(0.0);
        hRat.SetBarWidth(1.);

        p0fit = TF1("P0","pol0",1.,hRat.GetNbinsX());
        p0fit.SetLineColor(ROOT.kRed)
        hRat.Fit(p0fit,"0RWL");

        mean=p0fit.GetParameter(0)
        print "CCLA: ",hRat.GetNbinsX(),mean
        # c2=prepRatio()
        # c2.SetLeftMargin(lmargin)

        hRatZero=hRat.Clone()
        hRatZero.Scale(0.0);
        hRatZero.SetMinimum(0.1)
        hRatZero.SetMaximum(rmax)
        p2.SetLogx(1)
        p2.SetGridx(1)
    # hRat.Draw("hbar2");
        hRatZero.Draw("hbar2");
    # drawErrorBarsUser(c2,hRat,i1,i2,0.0,minRate)

        x=array('d')
        y=array( 'd' )
        ex=array( 'd' )
        ey=array( 'd' )
        maxx=0
        n=0

        for ibin in range(1,hRat.GetNbinsX()+1):
            if hRat.GetBinError(ibin) == 0 and hRat.GetBinContent(ibin) == 0 :
                print 'skipping'
                continue
            n=n+1
            if hRat.GetBinContent(ibin) > maxx :
                maxx=hRat.GetBinContent(ibin)
            x.append(hRat.GetXaxis().GetBinCenter(ibin))
            ex.append(0.)
            y.append(hRat.GetBinContent(ibin))
            ey.append(hRat.GetBinError(ibin))
            
            cont=hRat.GetBinContent(ibin);
            err=hRat.GetBinError(ibin);
            label=hRat.GetXaxis().GetBinLabel(ibin)                
        # print "13TeV:   ", label, "  Rate: ",cont," +- ",err
            outstring="Ratio: " +  str(ibin) + " " + label + "  Rate: " + str(cont) + " +- " + str(err)
            print outstring
  
        print "total points=",n
        print "y=",y," x=",x
        gr = TGraphErrors(n,y,x,ey,ex);
        gr.SetMarkerColor(ROOT.kBlue)
        gr.SetMarkerStyle(20)
        gr.SetLineColor(ROOT.kBlue)
        gr.SetMarkerSize(1.2)
        gr.Draw("P");
        #ym=mean
        ym=1.0
        #l1 = TLine(ym,0,ym,hRat.GetNbinsX())
        l1 = TLine(ym,0,ym,hRat.GetNbinsX())
        l1.SetLineStyle(2)
        l1.SetLineWidth(3)
        l1.SetLineColor(ROOT.kGreen-2)
        l1.Draw();
            
        latex=ROOT.TLatex()
        latex.SetNDC()
        latex.SetTextAlign(31)
        latex.SetTextSize(0.06)

        x0=0.95
        y0=0.85
    ## latex.DrawLatex(x0, y0, '#color[1]{ Mean = ' + '{0:.3f}'.format(p0fit.GetParameter(0)) + ' #pm ' + '{0:.3f}'.format(p0fit.GetParError(0)) +'}')
    ## latex.DrawLatex(x0, y0, '#color[1]{ Mean = ' + '{0:.3f}'.format(p0fit.GetParameter(0))+'}')
        #latex.DrawLatex(x0, y0, '#color[1]{ Mean = ' + '{0:.1f}'.format(p0fit.GetParameter(0))+'}')
        c1.Modified()
        c1.Update()
       
        if writePlot:
            plot=outfile + suffix
            c1.SaveAs(plot)    
    

        if os.getenv("FROMGUI") == None:
            print "Not from GUI"
            if not (DoAll or WhichDS == 'All'):
                raw_input('\npress return to end the program...')
