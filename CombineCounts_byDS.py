import math,ROOT,sys,os
from ROOT import gROOT, TFile, TChain, TTree, TH1F, TF1,SetOwnership

#BaseDirectory="/uscmst1b_scratch/lpc1/lpctrig/ingabu/TMD/HLT"
BaseDirectory="./"

RootS="13TeV"
## RootS="8TeV"

## BS="50ns"
BS="25ns"

#vsn = '700'
vsn = '62X'

# ilumi = 5.5e33  # run 196532
# ilumi = 5.3e33  # run 207884
# ilumi = 3.12e33 # run 207889
# ilumi = 1.7e34 # projected lumi for 13 TeV
ilumi = 1.1e34 # projected lumi for 13 TeV, 25 ns bunch spacing

## DataSets=["BJetPlusX", "BTag", "DoubleElectron", "DoubleMu", "DoublePhoton", "DoublePhotonHighPt", "ElectronHad", "HTMHT", "JetHT", "MET", "MuEG", "MuHad", "MuOnia", "MultiJet", "PhotonHad", "SingleElectron", "SingleMu", "SinglePhoton", "Tau", "TauPlusX"]
DataSets=['noprescl', 'BJetPlusX', 'BTag', 'DoubleElectron', 'DoubleMu', 'DoublePhoton', 'DoublePhotonHighPt', 'ElectronHad', 'HTMHT', 'JetHT', 'MET', 'MuEG', 'MuHad', 'MuOnia', 'MultiJet', 'PhotonHad', 'SingleElectron', 'SingleMu', 'SinglePhoton', 'Tau', 'TauPlusX']

## theDate="20131029"
## theDate="20131128"
theDate="20140604"


mfillb = 3564.
if BS == "50ns":
    nfillb = 1331.
    xtime = 50e-9
elif BS == "25ns":
    nfillb = 2662.
    xtime = 25e-9
else:
    print "Illegal bunch spacing"
    sys.exit(1)

collrate = (nfillb/mfillb)/xtime

OutDir=os.path.join("resultsByDS" + "_" + RootS +"_"+ theDate + '_no15to30_' + vsn,str(ilumi))

from CrossSections import crossSections13TeV

## ========================================================================= ##

def Rate(counts,nevt,xs):
    rate = collrate * (1 - math.exp(-1* (xs*ilumi*counts/nevt)/collrate))
    return rate

def RateErr(counts,nevt,xs):
    rateerr = xs * ilumi * ((math.sqrt(counts + ((counts)**2)/nevt))/nevt)
    return rateerr

def usage():
        """ Usage: GetRates.py
        Combine counts from a bunch in RateEff histograms and convert to rate
        """
        pass

def GetHistsAndAddCounts(indir,outdir):

    outHist="XXX"
    filelist=os.listdir(indir)
    nfound=0
    rootFiles=[]
    for f in filelist:
        if f.find("PU.root")>-1:
            print "Skipping: ", f
            continue
        if f.find(".root")>-1 and f.find("correlations")==-1:
            rootFiles.append(os.path.join(indir,f))

    if len(rootFiles) == 0:
        print "Could not find any root file in directory: ",indir, "  -- Exiting"
        sys.exit(1)


    f0=os.path.basename(rootFiles[0])
    outfile=os.path.join(outdir,f0[:f0.rfind("_")] + "_combined.root")
    AddCounts(rootFiles,outfile)
   
    return outfile

def AddCounts(rootFiles,outfile,sumEvents=True):

    outf = TFile(outfile,"RECREATE");
    SetOwnership( outf, False )   # tell python not to take ownership
    print "Output written to: ", outfile

    
    i=-1
    handles=[]
    for f in rootFiles:
        i+=1
        ## print i,f

        infile = TFile.Open(f)
        handles.append(infile)
        histInd = infile.Get("individual")
        histCum = infile.Get("cumulative")
        if sumEvents:
            nevt = infile.Get("NEVTS")
        
        if i==0:
            histInd_all = histInd.Clone()
            histCum_all = histCum.Clone()
            if sumEvents: NEVTS = nevt.Clone()
        else:
            histInd_all.Add(histInd)
            histCum_all.Add(histCum)
            if sumEvents: NEVTS.Add(nevt)

    outf.cd()
    histInd_all.Write()
    histCum_all.Write()
    if sumEvents: NEVTS.Write()
    outf.Close()

    for inf in handles:
        inf.Close()
    
def ConvertToRate(xs,histfile):

    outfile=histfile.replace("combined","rates")

    outf = TFile(outfile,"RECREATE");
    SetOwnership( outf, False )   # tell python not to take ownership
    print "Rate Histogram written to: ", outfile
    
    infile = TFile.Open(histfile)
    
    histInd = infile.Get("individual")
    histCum = infile.Get("cumulative")
    
    histInd_cl = histInd.Clone()
    histCum_cl = histCum.Clone()
    
    
    histNevt = infile.Get("NEVTS")
    nevt = histNevt.GetBinContent(1)
    
    nbins = histInd.GetNbinsX()
    
    print "Sample: ",Sample, " Cross section: ",xs/1.e-36, "N: ",nevt
    
    offset=0.
    for b in xrange(1,nbins+1):
        Label = histInd.GetXaxis().GetBinLabel(b)
        CountInd = histInd.GetBinContent(b)
        CountCum = histCum.GetBinContent(b)
    
        # if Label == "HLT_HcalPhiSym_v10" or Label == "HLT_HcalNZS_v9" or \
        #         Label == "HLT_DiJet35_MJJ700_AllJets_DEta3p5_VBF_v1" or \
        #         Label == "HLT_DiJet35_MJJ750_AllJets_DEta3p5_VBF_v1" or \
        #         Label == "HLT_QuadJet50_v2" or Label == "HLT_QuadJet50_Jet20_v1":
        # Label == "HLT_HcalPhiSym_v10" or Label == "HLT_HcalNZS_v9":
        ## if Label == "HLT_DiJet35_MJJ700_AllJets_DEta3p5_VBF_v1" or \
        ##         Label == "HLT_HcalPhiSym_v10" or Label == "HLT_HcalNZS_v9" or \
        ##         Label == "HLT_QuadJet50_v2":
        ##         
        ##     # print Label," ",Rate(CountInd),Rate(CountCum)
        ##     offset=histCum.GetBinContent(b)-histCum.GetBinContent(b-1)
        ##     print "A: ",b,Label,histCum.GetBinContent(b),histCum.GetBinContent(b-1),offset
        ## 
        ##     histInd.SetBinContent(b,0.)
        ##     histInd.SetBinError(b,0.)
        ## elif  Label == "HLT_DiJet35_MJJ750_AllJets_DEta3p5_VBF_v1" or\
        ##         Label == "HLT_QuadJet50_Jet20_v1":
        ##     histInd.SetBinContent(b,0.)
        ##     histInd.SetBinError(b,0.)
    
        CountCum=CountCum-offset
        histCum.SetBinContent(b,CountCum)
        histCum.SetBinError(b,math.sqrt(CountCum))
    
    
    
    for b in xrange(1,nbins+1):
        Label = histInd.GetXaxis().GetBinLabel(b)
        CountInd = histInd.GetBinContent(b)
        CountCum = histCum.GetBinContent(b)
    
    
        if Label == "HLT_DiJet35_MJJ700_AllJets_DEta3p5_VBF_v1":
            print "B: ",b,Label,histCum.GetBinContent(b),histCum.GetBinContent(b-1)
    
        RateInd = Rate(CountInd,nevt,xs)
        RateIndErr = RateErr(CountInd,nevt,xs)
    
        RateCum = Rate(CountCum,nevt,xs)
        RateCumErr = RateErr(CountCum,nevt,xs)
    
        histInd_cl.SetBinContent(b,RateInd)
        histInd_cl.SetBinError(b,RateIndErr)
    
        histCum_cl.SetBinContent(b,RateCum)
        histCum_cl.SetBinError(b,RateCumErr)
    
        # print Label, "  ", RateInd, " +- ", RateIndErr, "  ", RateCum, " +- ", RateCumErr
    
    outf.cd()
    histInd_cl.Write()
    histCum_cl.Write()
    outf.Close()
    infile.Close()

    return outfile


if __name__ == '__main__':

    gROOT.Reset()

    if RootS == "8TeV":
        crossSections=crossSections8TeV
    elif RootS == "13TeV":
        crossSections=crossSections13TeV
    else:
        print "Bad beam energy"
        sys.exit(1)

    for DS in DataSets:
        print "Running DS:", DS

        OutFile="hltmenu_"+RootS+"_"+BS+"_combinedRate_"+str(ilumi)+"_"+DS+ '_' + vsn + ".root"

        theRateHists=[]
        theSamples=crossSections.keys()
        for Sample in theSamples:

            ## print crossSections[Sample][1],crossSections[Sample][1].find("QCD_Pt-15to30Out")
            #if crossSections[Sample][1].find("QCD_Pt-15to30_antiEMOut")==0 or crossSections[Sample][1].find("QCD_Pt-15to20")==0:
            if crossSections[Sample][1].find("QCD_Pt-5to10_antiEMOut_")==0  or crossSections[Sample][1].find("QCD_Pt-10to15_antiEMOut_")==0 or crossSections[Sample][1].find("QCD_Pt-15to30_antiEMOut_")==0 or crossSections[Sample][1].find("QCD_Pt-5to10_EMEnrichedOut_")==0 or crossSections[Sample][1].find("QCD_Pt-10to20_EMEnrichedOut_")==0 or crossSections[Sample][1].find("QCD_Pt-800to1000_MuEnrichedPt5_nofiltOut_")==0 or crossSections[Sample][1].find("QCD_Pt-1000_MuEnrichedPt5_nofiltOut_")==0 :
                continue
            print ""
            
            outDir=os.path.join(OutDir,crossSections[Sample][1])
            outDir=outDir + BS + "_" + RootS + "_DS_" + DS + '_' + vsn
            if not os.path.isdir(outDir):
                os.makedirs(outDir)

            inDir=os.path.join(BaseDirectory,crossSections[Sample][1])
            inDir=inDir + BS + "_" + RootS + "_DS_" + DS  + "_" + theDate + '_' + vsn
            if not os.path.isdir(inDir):
                print "Input directory    " + inDir + "   does not exist -- Exiting"
                print Sample
                sys.exit(1)

            combinedHist=GetHistsAndAddCounts(inDir,outDir)
            rateHist=ConvertToRate(crossSections[Sample][0]*1e-36,combinedHist)
            theRateHists.append(rateHist)

        # now add all the samples together
        if len(theRateHists)>0:
            outfile=os.path.join(OutDir,OutFile)
            AddCounts(theRateHists,outfile,False)
        else:
            print "Problem -- no rate histograms were created"
