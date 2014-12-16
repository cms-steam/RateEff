from ROOT import gROOT, gStyle, gSystem, TCanvas, TF1, TFile, TH1F, TPad, TGraphErrors
from ROOT import TColor, TLine, TLegend, TLatex
from ROOT import SetOwnership

import sys,string,math,os,ROOT

from array import array

sys.path.append('rootmacros')
from myPyRootSettings import prepPlot
from myPyRootMacros import GetHist, PrepLegend, drawErrorBarsUser, DrawText

from DataSets_MC_noprescl import DataSets

DoAll=True

UseLowPTQCD=False


UseEnriched=True


vsn2 = '721'
vsn1 = '721'

INPUTDIR='RatePerSample'



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
    #WhichDS="DoubleMu"
    #WhichDS="SinglePhoton"

    WhichDS="Higgs"

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
    outDir="Plots/MC13_721_NoMuEnr1212_Paths"
    if not os.path.exists(outDir):
        os.makedirs(outDir)    
    for trig in theTriggers:
        hname=trig[:trig.rfind("_v")]
        print "studying ", hname
        hist1=GetHist(MCFile1,hname)
        hist1.SetFillColor(ROOT.kRed-7)
        print vsn1,hist1.GetEntries()
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

        hist1.GetYaxis().SetLabelSize(.03);
        hist1.GetYaxis().SetTitleSize(0.035);
        hist1.GetYaxis().SetTitle("Rate (Hz)");
        hist1.GetYaxis().SetTitleOffset(.95);
        hist1.GetXaxis().SetLabelSize(labelsz);
        hist1.GetXaxis().SetTitleOffset(0.11);

        minRate=0.09
        #hist2.SetMinimum(hmin)
        #if hmax>-1.:
            #hist2.SetMaximum(hmax)
        hist1.SetBarWidth(0.45);
        hist1.SetBarOffset(0.45);

   

    ## c1=prepPlot()
        ylow=900
        c1,p1,p2=prep2by1Plot("c1","Rates per MC sample ",575, 31, 1250, ylow)
        p1.Draw()
        p2.Draw()

        p1.cd()

        if logx:
            p1.SetLogx(True)
        p1.SetLeftMargin(lmargin)

        #hist2.Draw("hbar2");
        hist1.Draw("hbar2,e,same");

        i1=1
        i2=hist1.GetNbinsX()
        print "minbin=",i1," maxbin=",i2
        drawErrorBarsUser(p1,hist1,i1,i2,0.15,minRate)




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
            la.DrawLatex(xt,yt-0.03-0.03, "no Low PT QCD");
            
        if not UseEnriched:
            la.DrawLatex(xt+0.2,yt-0.03-0.03, "no Enriched QCD");

        leg.AddEntry(hist1,"721patch1_GRunv41","f");
        leg.SetTextSize(0.026);    
        leg.Draw();


        p1.Modified()
        p1.Update()


        p2.cd()

        if writePlot:
            plot=outfile + suffix
            c1.SaveAs(plot)    
    

        if os.getenv("FROMGUI") == None:
            print "Not from GUI"
            if not DoAll:
                raw_input('\npress return to end the program...')
