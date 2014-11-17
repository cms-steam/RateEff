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

ShowCumRate=True

vsn = '700'
#vsn = '62X'

if not UseLowPTQCD:
    INPUTDIR1="resultsByDS_13TeV_20141114_700wPresc/1.4e+34"
    if not UseEnriched:
        INPUTDIR1='resultsByDS_13TeV_20140602_onlyQCD30_' + vsn
else:
    INPUTDIR1="resultsByDS_13TeV_20140602_" + vsn
    if not UseEnriched:
        INPUTDIR1="resultsByDS_13TeV_20140602_onlyQCD15_" + vsn


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

    WhichDS="JetHT"

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


writePlot=False
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


def prep2by1Plot(cname,ctitle,wtopx=300,wtopy=20,ww=840,wh=500):

    c = TCanvas(cname,ctitle,wtopx,wtopy,ww,wh)
    SetOwnership(c,1 )

    bmargin=0.075
    rmargin=0.02
    lmargin=0.45
    tmargin=0.01
    
                                    ## xlow ylow xup yup
    pad1 = TPad("pad1","This is pad1",0.0,0.0,1.0,1.0);

    pad1.SetTopMargin(0.02);
    pad1.SetBottomMargin(0.1);

    rmargin=0.005
    pad1.SetRightMargin(rmargin);

    lmargin=0.025
    pad1.SetLeftMargin(lmargin);

    SetOwnership(pad1,1 )

    c.SetBottomMargin(bmargin);
    c.SetRightMargin(rmargin);
    c.SetLeftMargin(lmargin);
    c.SetTopMargin(tmargin);

    c.SetLogy(0);
    c.SetLogx(0);

    return c,pad1

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


    print "XXXXXXXXXXXXXXXXX -- ",INPUTDIR1
    MCFile1 = os.path.join(INPUTDIR1,"hltmenu_13TeV_25ns_combinedRate_1.4e+34_" + WhichDS + '_' + vsn + ".root")

    ScaleMC=1.

    h1=GetHist(MCFile1,"individual")
    h1cum=GetHist(MCFile1,"cumulative")
    h1L1names=GetHist(MCFile1,"L1Trignames")
    h1HLTpresc=GetHist(MCFile1,"HLTPrescale")
    h1L1presc=GetHist(MCFile1,"L1Prescale")

    theTriggers=DataSets[WhichDS]
    Triggers=[]
    for trig in theTriggers:
        if trig != "HLT_IsoMu8_eta2p1_LooseIsoPFTau20_L1ETM26_v1" and trig !="HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_L1ETM36_v1": #and trig != "HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_v4":
            Triggers.append(trig[:trig.rfind("_v")])
    print Triggers

    hist1    = TH1F( 'hist', 'Rates for Dataset ' + WhichDS, len(Triggers), 0, float(len(Triggers)) )
    hist1.SetFillColor(ROOT.kRed)

    ibin=-1
    for trig in Triggers:
        ibin+=1
        hist1.GetXaxis().SetBinLabel(ibin+1,trig)



    outDir="newplots/MCs13_" + vsn + "_wPresc"
    if not os.path.exists(outDir):
        os.makedirs(outDir)

    outplot= "comp_13TeVMCrates_" + WhichDS + vsn
    outfile=os.path.join(outDir,"comp_13TeVMCrates_" + WhichDS + vsn)
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

    if ShowCumRate: twfile.write("| *Path Name* | *L1 Condition* | *L1 Prescale* | *HLT Prescale* | *13 TeV MC Rate [Hz]* | *Cumulative Rate* [Hz] |" + "\n")
    else: twfile.write("| *Path Name* | *L1 Condition* | *L1 Prescale* | *HLT Prescale* | *13 TeV MC Rate [Hz]* |" + "\n")

    firstbin1=0.0
    lastbin1=0.0
    firstbinerr1=0.0
    lastbinerr1=0.0
    cum1Tot = 0.0
    cum1Toterr = 0.0

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
                outstring="13TeV : " +  str(ibin) + " " + label + "  Rate: " + str(cont) + " +- " + str(err)
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


        print " "

    print "firstbin1 ", firstbin1, " lastbin1 ", lastbin1
    cum1Tot=lastbin1
    cum1Toterr=lastbinerr1
    print "cum1Tot = ", cum1Tot, " +- ", cum1Toterr

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
        lmargin=0.725; labelsz=0.028; rmax=3.
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

    minRate=0.09

    hist1.SetBarWidth(0.45);
    hist1.SetBarOffset(0.45);


    ylow=900
    c1,p1=prep2by1Plot("c1","MC Comparison",575, 31, 1000, ylow)
    p1.Draw()

    p1.cd()

    if logx:
        p1.SetLogx(True)
    p1.SetLeftMargin(lmargin)

    hist1.Draw("hbar2,e");

    i1=1
    i2=hist1.GetNbinsX()
    
    drawErrorBarsUser(p1,hist1,i1,i2,0.15,minRate)

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
    leg.SetTextSize(0.026);    
    leg.Draw();


    p1.Modified()
    p1.Update()

    for ibin in range(1,nbins+1):

        if ShowCumRate: 
            twstring = "| " + "!" + str(h1.GetXaxis().GetBinLabel(ibin)) + " | " + "!" + str(h1L1names.GetXaxis().GetBinLabel(ibin)) + " | " + str(h1L1presc.GetXaxis().GetBinLabel(ibin)) + " | " + str(h1HLTpresc.GetXaxis().GetBinLabel(ibin)) + " | " + str('{0:.2f}'.format(hist1.GetBinContent(ibin))) + "+-" + str('{0:.2f}'.format(hist1.GetBinError(ibin))) + " | " +  str('{0:.2f}'.format(h1cum.GetBinContent(ibin))) + "+-" + str('{0:.2f}'.format(h1cum.GetBinError(ibin))) + " | "
            twfile.write(twstring + "\n")
        else: 
            twstring = "| " + "!" + str(h1.GetXaxis().GetBinLabel(ibin)) + " | " + "!" + str(h1L1names.GetXaxis().GetBinLabel(ibin)) + " | " + str(h1L1presc.GetXaxis().GetBinLabel(ibin)) + " | " + str(h1HLTpresc.GetXaxis().GetBinLabel(ibin)) + " | " + str('{0:.2f}'.format(hist1.GetBinContent(ibin))) + "+-" + str('{0:.2f}'.format(hist1.GetBinError(ibin))) + " | "
            twfile.write(twstring + "\n")


    twfile.write("| Total Cumulative Dataset Rate | " + str('{0:.2f}'.format(cum1Tot)) + " +- " + str('{0:.2f}'.format(cum1Toterr)) + " | "+ "\n")
    #twfile.write("| Total Cumulative Dataset Rate | " + str('{0:.2f}'.format(cum13Tot)) + " | "+ "\n")
    twfile.write("| <center> <img height=\"220/\" alt=\"\" src=\"%ATTACHURL%" + outplot + ".gif\" /> </center> <br> <center> [[%ATTACHURL%" + outplot + ".gif][Click for full size Figure]] </center> |" + "\n")

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
