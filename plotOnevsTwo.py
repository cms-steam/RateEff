from ROOT import gROOT, gStyle, gSystem, TCanvas, TF1, TFile, TH1F, TPad, TGraphErrors
from ROOT import TColor, TLine, TLegend, TLatex
from ROOT import SetOwnership

import sys,string,math,os,ROOT

from array import array

sys.path.append('rootmacros')
from myPyRootSettings import prepPlot
from myPyRootMacros import GetHist, PrepLegend, drawErrorBarsUser, DrawText

from DataSets_MC_noprescl import DataSets

DoAll=False

UseLowPTQCD=False
#UseLowPTQCD=True

UseEnriched=True
## UseEnriched=False

vsn = '700'
#vsn = '62X'

if not UseLowPTQCD:
    #INPUTDIR1="resultsByDS_13TeV_20140623JustQCD_no15to30_" + vsn + "onlyQCD/1.1e+34"
    INPUTDIR1="resultsByDS_13TeV_20140609_no15to30_" + vsn + "NewXSec/1.1e+34"
    INPUTDIR2="resultsByDS_no15to30_13TeV_20140129/1.1e+34"
    #INPUTDIR2="resultsByDS_13TeV_20140609_no15to30_" + vsn + "/1.1e+34"
    if not UseEnriched:
        INPUTDIR1='resultsByDS_13TeV_20140602_onlyQCD30_' + vsn
        INPUTDIR2="resultsByDS_no15to30_NoEnrichedMC_20131128"
else:
    INPUTDIR1="resultsByDS_13TeV_20140602_" + vsn
    INPUTDIR2=''
    if not UseEnriched:
        INPUTDIR1="resultsByDS_13TeV_20140602_onlyQCD15_" + vsn
        INPUTDIR2=''


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

    #WhichDS="JetHT"

    #WhichDS="DoubleElectron"
    #WhichDS="PhotonHad"
    #WhichDS="MultiJet"
    #WhichDS="MuHad"
    #WhichDS="MuOnia"

    #WhichDS="BTag"
    #WhichDS="ElectronHad"


    #WhichDS="TauPlusX"
    WhichDS="Tau"
    #WhichDS="BJetPlusX"
    #WhichDS="MuEG"
    #WhichDS="noprescl"

    ## WhichDS="MuEGTauPlusXBJetPlusX"

logx=True

## used to determine which lumi to scale to
## run="207884" 
run="207889" 

writePlot=True
# suffix="_MuEnr.gif"
suffix=".gif"

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


def ReadRatesFromFile(Sample,infile):

    try:
        print "Opening ",infile
        ifile=open(infile, 'r')
    except:
        print "Could not open file: ",infile
        sys.exit(1)

    hltSummary = {}
    x = ifile.readline()

    iline=0

    TrigNames=[]
    Rates=[]
    Errs=[]

    while x != "":
        iline+=1

        
        xx=string.rstrip(x)
        if xx.find("#") != 0:

            inputLine=string.split(xx)
            if inputLine[0].find(Sample) == 0:
                print inputLine
                TrigNames.append(inputLine[2])
                Rates.append(float(inputLine[4]))
                Errs.append(float(inputLine[6]))

        x = ifile.readline()

    # print TrigNames
    ifile.close()

    h    = TH1F( 'individual' + Sample, 'Rates for ' + Sample, len(TrigNames), 0, float(len(TrigNames)) )
    h.Sumw2()
    ibin=-1
    for trig in TrigNames:
        ibin+=1
        h.GetXaxis().SetBinLabel(ibin+1,trig)

        rate=Rates[ibin]
        err=Errs[ibin]
        h.SetBinContent(ibin+1,rate)
        h.SetBinError(ibin+1,err)

    return h

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
        print "Could not dataset ",WhichDS," in dictionary"
        sys.exit(1)


    print "XXXXXXXXXXXXXXXXX -- ",INPUTDIR2, " ", INPUTDIR1
    MCFile1 = os.path.join(INPUTDIR1,"hltmenu_13TeV_25ns_combinedRate_1.1e+34_" + WhichDS + '_' + vsn + ".root")
    MCFile2 = os.path.join(INPUTDIR2,"hltmenu_13TeV_25ns_combinedRate_1.1e+34_" + WhichDS + ".root")
    #MCFile2 = os.path.join(INPUTDIR2,"hltmenu_13TeV_25ns_combinedRate_1.1e+34_" + WhichDS + '_' + vsn + ".root")

    ScaleMC=1.

    if WhichDS == "MuEGTauPlusXBJetPlusX":
        h1=ReadRatesFromFile("h1","comp_8TeVand13TeVMCrates_combined.txt")
        h2=ReadRatesFromFile("h2","comp_8TeVand13TeVMCrates_combined.txt")
    else:
        h1=GetHist(MCFile1,"individual")
        h2=GetHist(MCFile2,"individual")
        h1cum=GetHist(MCFile1,"cumulative")
        h2cum=GetHist(MCFile2,"cumulative")

    theTriggers=DataSets[WhichDS]
    Triggers=[]
    for trig in theTriggers:
        if trig != "HLT_IsoMu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1" and trig !="HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_L1ETM36_v1" and trig != "HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_v4":
            Triggers.append(trig[:trig.rfind("_v")])
    print Triggers

    hist1    = TH1F( 'hist', 'Rates for Dataset ' + WhichDS, len(Triggers), 0, float(len(Triggers)) )
    hist1.SetFillColor(ROOT.kRed)

    ibin=-1
    for trig in Triggers:
        ibin+=1
        hist1.GetXaxis().SetBinLabel(ibin+1,trig)



    outDir="newplots/MCs13New" + vsn + "vs13Old_NewXSecNoMu15_20"
    if not os.path.exists(outDir):
        os.makedirs(outDir)

    outplot= "comp_13TeVNewand13TeVOldMCrates_withRat_" + WhichDS + vsn
    outfile=os.path.join(outDir,"comp_13TeVNewand13TeVOldMCrates_withRat_" + WhichDS + vsn)
    if not UseEnriched:
        outfile=outfile + "_noEnrichedMC"
        outplot=outplot + "_noEnrichedMC"
    if not UseLowPTQCD:
        outfile=outfile + "_no15to30MC"
        outplot=outplot + "_no15to30MC"
    txtfile=outfile+ ".txt"
    tfile=OpenFile(txtfile,"w")

    twikifile=outfile+ ".twiki"
    twfile=OpenFile(twikifile,"w")


    outstring="%TWISTY{mode=\"div\" showlink=\"show !"+ WhichDS +"&nbsp;\" hidelink=\"hide\" showimgleft=\"%ICONURLPATH{toggleopen-small}%\" hideimgleft=\"%ICONURLPATH{toggleclose-small}%\" }%" 
    twfile.write(outstring + "\n")
    twfile.write("---++++!! *" + WhichDS + "*" + "\n")

    twfile.write("| *Path Name* | *13 TeV MC Rate 53X [Hz] * | *13 TeV MC Rate " + vsn + " [Hz]* | *Ratio* |"+ "\n")

    hist2=hist1.Clone()
    hist2.SetName("MC")   

    firstbin1=0.0
    lastbin1=0.0
    firstbinerr1=0.0
    lastbinerr1=0.0
    firstbin2=0.0
    lastbin2=0.0
    firstbinerr2=0.0
    lastbinerr2=0.0
    cum1Tot = 0.0
    cum2Tot = 0.0
    cum1Toterr = 0.0
    cum2Toterr = 0.0

    for itrig in range(len(Triggers)):
        trig=Triggers[itrig]
        print "------------------- ", trig, " ====================="
        nbins=h1.GetNbinsX() 

        for ibin in range(1,nbins+1):
            label=h1.GetXaxis().GetBinLabel(ibin)
            tstTrig=label[:label.rfind("_v")]
            if tstTrig == trig:
                cont=h1.GetBinContent(ibin)/ScaleMC;
                err=h1.GetBinError(ibin)/ScaleMC;
                outstring="13TeV 700: " +  str(ibin) + " " + label + "  Rate: " + str(cont) + " +- " + str(err)
                print outstring
                tfile.write(outstring + "\n")
                
                hist1.SetBinContent(itrig+1,cont)
                hist1.SetBinError(itrig+1,err)
                cum1 = h1cum.GetBinContent(ibin)
                cum1err = h1cum.GetBinError(ibin)
                print label, " Cum1Rate = ", cum1, " +- ", cum1err
                if itrig==0:
                    firstbin1=cum1
                    firstbinerr1=cum1err
                if itrig == len(Triggers)-1:
                    lastbin1=cum1
                    lastbinerr1=cum1err


        nbins=h2.GetNbinsX() 
        for ibin in range(1,nbins+1):
            label=h2.GetXaxis().GetBinLabel(ibin)
            tstTrig=label[:label.rfind("_v")]
            if tstTrig == trig:
                cont=h2.GetBinContent(ibin)/ScaleMC;
                err=h2.GetBinError(ibin)/ScaleMC;

                outstring="13TeV 53X: " +  str(ibin) + " " + label + "  Rate: " + str(cont) + " +- " + str(err)
                print outstring
                tfile.write(outstring + "\n")
                if err>=cont:
                    err=cont
                hist2.SetBinContent(itrig+1,cont)
                hist2.SetBinError(itrig+1,err)
                cum2 = h2cum.GetBinContent(ibin)
                cum2err = h2cum.GetBinError(ibin)
                print label, " Cum2Rate = ", cum2, " +- ", cum2err
                if itrig==0:
                    firstbin2=cum2
                    firstbinerr2=cum2err
                if itrig == len(Triggers)-1:
                    lastbin2=cum2
                    lastbinerr2=cum2err
        print " "

    print "firstbin1 ", firstbin1, " lastbin1 ", lastbin1
    print "firstbin2 ", firstbin2, " lastbin2 ", lastbin2
    cum1Tot=lastbin1
    cum1Toterr=lastbinerr1
    cum2Tot=lastbin2
    cum2Toterr=lastbinerr2
    print "cum1Tot = ", cum1Tot, " +- ", cum1Toterr
    print "cum2Tot = ", cum2Tot, " +- ", cum2Toterr

    CloseFile(tfile)
    ### CCLA defaults
    labelsz=0.033
    lmargin=0.5
    hmax=-1.
    hmin=0.1

    xl1=.02; 
    if not logx:
        xl1=.02
    yl1=.01; 

    rmax=10.
    ## CCLA Tuning
    if WhichDS == "BTag":
        pass
    if WhichDS == "BJetPlusX":
        lmargin=0.58; rmax=2.
    elif WhichDS == "DoublePhoton":
        lmargin=0.725; labelsz=0.028; rmax=4.
    elif WhichDS == "DoublePhotonHighPt":
        lmargin=0.425; labelsz=0.028; rmax=3.
    elif WhichDS == "MuEG":
        lmargin=0.55; rmax=3.
    elif WhichDS == "MuOnia":
        rmax=4.
    elif WhichDS == "TauPlusX":
        lmargin=0.76; labelsz=0.04; rmax=4.
    elif WhichDS == "ElectronHad":
        lmargin=0.69 ; labelsz=0.03; rmax=3.
    elif WhichDS == "MuHad":
        lmargin=0.62 ; labelsz=0.03; hmin=0.05; rmax=3.
    elif WhichDS == "METParked":
        hmin=0.0005
    elif WhichDS == "MET":
        hmin=0.0005; lmargin=0.76; rmax=3.
    elif WhichDS == "HTMHT":
        lmargin=0.4 ; rmax=1.5; hmin=0.8
        ## hmin=0.0005
    elif WhichDS == "MultiJet":
        lmargin=0.37; labelsz=0.042; rmax=2.
    elif WhichDS == "PhotonHad":
        rmax=2.
    elif WhichDS == "SingleElectron":
        labelsz=0.03; lmargin=0.7; rmax=3.
    elif WhichDS == "SingleMu":
        lmargin=0.5 ; labelsz=0.028; rmax=6.
    elif WhichDS == "JetHT":
        hmin=0.1; rmax=3.; lmargin=0.6
    elif WhichDS == "DoubleElectron":
        lmargin=0.785; labelsz=0.03; rmax=6.
    elif WhichDS == "SinglePhoton":
        lmargin=0.55; rmax=4.
    elif WhichDS == "DoubleMu":
        lmargin=0.48; rmax=3.
    elif WhichDS=="MuEGTauPlusXBJetPlusX":
        lmargin=0.6
    elif WhichDS=="Tau":
        lmargin=0.6; rmax = 2.



    hist1.SetFillColor(ROOT.kBlue)
    hist2.SetFillColor(ROOT.kRed)

    hist2.GetYaxis().SetLabelSize(.03);
    hist2.GetYaxis().SetTitleSize(0.035);
    hist2.GetYaxis().SetTitle("Rate (Hz)");
    hist2.GetYaxis().SetTitleOffset(.95);
    hist2.GetYaxis().SetLabelOffset(-.005);

    hist2.GetXaxis().SetLabelSize(labelsz);

    # h1.GetXaxis().SetTitle("Trigger Path");
    hist2.GetXaxis().SetTitleOffset(4.11);

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
    c1,p1,p2=prep2by1Plot("c1","MC and Data Comparision",575, 31, 1250, ylow)
    ## c1,p1,p2=prep2by1Plot("c1","MC and Data Comparision",1300, 1, 1220, ylow)
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
    la.SetTextSize(0.03)

    header=WhichDS + " DS"    
    xt=xl2+0.11; yt=yl2-0.03
    la.SetTextColor(ROOT.kGreen+3)
    la.DrawLatex(xt+.19,yt-.03, header);
    la.SetTextSize(0.026)
    la.SetTextColor(1)
    la.DrawLatex(xt,yt-0.02, "L=1.1e34 Hz/cm^{2}");
    if not UseLowPTQCD:
        la.DrawLatex(xt,yt-0.03-0.015, "no Low PT QCD");

    if not UseEnriched:
        la.DrawLatex(xt+0.2,yt-0.03-0.03, "no Enriched QCD");


    if WhichDS == "MuEGTauPlusXBJetPlusX":
        header= "BJetPlusX / TauPlusX / MuEG"
    ## leg.SetHeader(header)
    leg.AddEntry(hist1,"13TeV 62XMC-HLT700","f");
    leg.AddEntry(hist2,"13TeV 53XMC-HLT53X","f");
    leg.SetTextSize(0.026);    
    leg.Draw();


    p1.Modified()
    p1.Update()


    p2.cd()


    ### now Ratio
    hRat=hist1.Clone();
    ## hRat.SetName("8TeV/13TeV")
    ## hRat.Divide(h1,h2,1.,1.,"");

    hRat.SetName("700/53X")
    hRat.Divide(hist1,hist2,1.,1.,"");

    ## hRat.GetYaxis().SetTitle("8TeV/13TeV");
    hRat.GetYaxis().SetTitle("Ratio 700/53X");
    hRat.GetYaxis().SetTitleOffset(.35);
    hRat.GetYaxis().SetLabelOffset(-.025);

    print labelsz*2.1
    hRat.GetYaxis().SetLabelSize(0.06);
    hRat.GetYaxis().SetTitleSize(0.085);

    hRat.SetBarOffset(0.0);
    hRat.SetBarWidth(1.);

    p0fit = TF1("P0","pol0",1.,hRat.GetNbinsX());
    p0fit.SetLineColor(ROOT.kRed)
    hRat.Fit(p0fit,"0R");

    mean=p0fit.GetParameter(0)
    print "CCLA: ",hRat.GetNbinsX(),mean
    # c2=prepRatio()
    # c2.SetLeftMargin(lmargin)

    hRatZero=hRat.Clone()
    hRatZero.Scale(0.0);
    hRatZero.SetMinimum(0.)
    hRatZero.GetXaxis().SetLabelOffset(-5.);

    hRatZero.SetMaximum(rmax)

    # hRat.Draw("hbar2");
    hRatZero.Draw("hbar2");
    # drawErrorBarsUser(c2,hRat,i1,i2,0.0,minRate)

    x, y , ex, ey = array( 'd' ), array( 'd' ), array( 'd' ), array( 'd' )

    n=hRat.GetNbinsX()
    for ibin in range(1,n+1):
        # print ibin,hRat.GetXaxis().GetBinCenter(ibin)
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

        
        twstring = "| " + "!" + str(hRat.GetXaxis().GetBinLabel(ibin)) + " | " + str('{0:.2f}'.format(hist2.GetBinContent(ibin))) + "+-" + str('{0:.2f}'.format(hist2.GetBinError(ibin))) + " | " + str('{0:.2f}'.format(hist1.GetBinContent(ibin))) + "+-" + str('{0:.2f}'.format(hist1.GetBinError(ibin))) + " | " + str('{0:.2f}'.format(hRat.GetBinContent(ibin))) + "+-" + str('{0:.2f}'.format(hRat.GetBinError(ibin))) + " | "
        twfile.write(twstring + "\n")


    twfile.write("| Total Cumulative Dataset Rate | " + str('{0:.2f}'.format(cum2Tot)) + " +- " + str('{0:.2f}'.format(cum2Toterr)) + " | " + str('{0:.2f}'.format(cum1Tot)) + " +- " + str('{0:.2f}'.format(cum1Toterr)) + " | "+ "\n")
    #twfile.write("| Total Cumulative Dataset Rate | " + str('{0:.2f}'.format(cum13Tot)) + " | "+ "\n")
    twfile.write("| <center> <img height=\"220/\" alt=\"\" src=\"%ATTACHURL%" + outplot + ".gif\" /> </center> <br> <center> [[%ATTACHURL%" + outplot + ".gif][Click for full size Figure]] </center> |" + "\n")

    gr = TGraphErrors(n,y,x,ey,ex);

    gr.SetMarkerColor(ROOT.kBlue)
    gr.SetMarkerStyle(20)
    gr.SetLineColor(ROOT.kBlue)
    gr.SetMarkerSize(1.5)

    gr.Draw("P");

    y=mean
    l1 = TLine(y,0,y,n)
    l1.SetLineStyle(2)
    l1.SetLineWidth(3)
    l1.SetLineColor(ROOT.kMagenta)
    l1.Draw();

    latex=ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextAlign(31)
    latex.SetTextSize(0.06)

    x0=0.95
    y0=0.85
    ## latex.DrawLatex(x0, y0, '#color[1]{ Mean = ' + '{0:.3f}'.format(p0fit.GetParameter(0)) + ' #pm ' + '{0:.3f}'.format(p0fit.GetParError(0)) +'}')
    ## latex.DrawLatex(x0, y0, '#color[1]{ Mean = ' + '{0:.3f}'.format(p0fit.GetParameter(0))+'}')
    latex.DrawLatex(x0, y0, '#color[1]{ Mean = ' + '{0:.1f}'.format(p0fit.GetParameter(0))+'}')
    c1.Modified()
    c1.Update()
       
    outstringend="%ENDTWISTY%" 
    twfile.write(outstringend + "\n")
    CloseFile(twfile)

    if writePlot:
        plot=outfile + suffix
        c1.Print(plot)    

    if os.getenv("FROMGUI") == None:
        print "Not from GUI"
        if not DoAll:
            raw_input('\npress return to end the program...')
