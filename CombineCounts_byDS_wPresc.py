import math,ROOT,sys,os
from ROOT import gROOT, TFile, TChain, TTree, TH1F, TF1,SetOwnership

#BaseDirectory="/uscmst1b_scratch/lpc1/lpctrig/ingabu/TMD/HLT"
BaseDirectory="./"

RootS="13TeV"
## RootS="8TeV"

## BS="50ns"
BS="25ns"

vsn = '731'
#vsn = '62X'

# ilumi = 1.7e34 # projected lumi for 13 TeV
#ilumi = 1.1e34 # projected lumi for 13 TeV, 25 ns bunch spacing
ilumi = 7.0e33

## DataSets=["BJetPlusX", "BTag", "DoubleElectron", "DoubleMu", "DoublePhoton", "DoublePhotonHighPt", "ElectronHad", "HTMHT", "JetHT", "MET", "MuEG", "MuHad", "MuOnia", "MultiJet", "PhotonHad", "SingleElectron", "SingleMu", "SinglePhoton", "Tau", "TauPlusX"]
#DataSets=['All']
DataSets = ['Higgs', 'B2G', 'EXO', 'SUSY', 'TOP', 'BPH', 'Taus', 'E_GAMMA', 'SMP', 'JET_MET', 'BTV', 'TSG', 'All']

#theDate="20140803"
#theDate="20140623JustQCD"
theDate="20141212"

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

#OutDir=os.path.join("resultsByDS" + "_" + RootS +"_"+ theDate + '_no15to30_' + vsn + 'CorrMuCuts',str(ilumi))
OutDir=os.path.join("resultsByDS" + "_" + RootS + "_" + theDate + "_" + vsn,str(ilumi))

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

def GetCorrelHistsAndAddCounts(indir,outdir):

    outHist="XXX"
    filelist=os.listdir(indir)
    nfound=0
    rootFiles=[]
    for f in filelist:
        if f.find("PU.root")>-1:
            print "Skipping: ", f
            continue
        if f.find(".root")>-1 and f.find("correlations")>-1:
            rootFiles.append(os.path.join(indir,f))

    if len(rootFiles) == 0:
        print "Could not find any root file in directory: ",indir, "  -- Exiting"
        sys.exit(1)


    f0=os.path.basename(rootFiles[0])
    outfile=os.path.join(outdir,f0[:f0.rfind("_")] + "_combined.root")
    AddCorrelCounts(rootFiles,outfile,False)
   
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
        histHLTpresc = infile.Get("HLTPrescale")
        histL1presc = infile.Get("L1Prescale")
        histL1names = infile.Get("L1Trignames")
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
    histHLTpresc.Write()
    histL1presc.Write()
    histL1names.Write()
    if sumEvents: NEVTS.Write()
    outf.Close()

    for inf in handles:
        inf.Close()

def AddCorrelCounts(rootFiles,outfile,LastStep=False):

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
        if LastStep: 
            histPie = infile.Get("h_pie_QCD")
            histSharedRate = infile.Get("h_shared_rate_QCD")
        else:
            histPie = infile.Get("unnormalized/h_pie_QCD")
            histSharedRate = infile.Get("unnormalized/h_shared_rate_QCD")
        
        if i==0:
            histPie_all = histPie.Clone()
            histSharedRate_all = histSharedRate.Clone()
        else:
            histPie_all.Add(histPie)
            histSharedRate_all.Add(histSharedRate)

    outf.cd()
    histPie_all.Write()
    histSharedRate_all.Write()
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
    histHLTpresc = infile.Get("HLTPrescale")
    histL1presc = infile.Get("L1Prescale")
    histL1names = infile.Get("L1Trignames")
    
    histInd_cl = histInd.Clone()
    histCum_cl = histCum.Clone()
    
    
    histNevt = infile.Get("NEVTS")
    nevt = histNevt.GetBinContent(1)
    
    nbins = histInd.GetNbinsX()
    
    print "Sample: ",Sample, " Cross section: ",xs/1.e-36, "N: ",nevt
    
    
    for b in xrange(1,nbins+1):
        Label = histInd.GetXaxis().GetBinLabel(b)
        CountInd = histInd.GetBinContent(b)
        CountCum = histCum.GetBinContent(b)
    
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
    histHLTpresc.Write()
    histL1presc.Write()
    histL1names.Write()
    outf.Close()
    infile.Close()

    return outfile

def ConvertCorrelToRate(xs,histfile,histfileMain):

    outfile=histfile.replace("combined","rates")

    outf = TFile(outfile,"RECREATE");
    SetOwnership( outf, False )   # tell python not to take ownership
    print "Rate Histogram written to: ", outfile
    
    infileNEVTS = TFile.Open(histfileMain)

    histNevt = infileNEVTS.Get("NEVTS")
    nevt = histNevt.GetBinContent(1)

    infileNEVTS.Close()

    infile = TFile.Open(histfile)

    histPie = infile.Get("h_pie_QCD")
    histSharedRate = infile.Get("h_shared_rate_QCD")
    
    histPie_cl = histPie.Clone()
    histSharedRate_cl = histSharedRate.Clone()
    
    
    nbins = histPie.GetNbinsX()
    binx = histSharedRate.GetNbinsX()
    biny = histSharedRate.GetNbinsY()
    nbinsSh = histSharedRate.GetBin(binx,biny)
    
    print "Sample: ",Sample, " Cross section: ",xs/1.e-36, "N: ",nevt
    
    for b in xrange(1,nbins+1):
        #Label = histPie.GetXaxis().GetBinLabel(b)
        CountPie = histPie.GetBinContent(b)
    
        RatePie = Rate(CountPie,nevt,xs)
        RatePieErr = RateErr(CountPie,nevt,xs)
    
        histPie_cl.SetBinContent(b,RatePie)
        histPie_cl.SetBinError(b,RatePieErr)
    
    for b in range(1,nbinsSh+1):
        CountShared = histSharedRate.GetBinContent(b)

        RateSharedRate = Rate(CountShared,nevt,xs)
        RateSharedRateErr = RateErr(CountShared,nevt,xs)

        histSharedRate_cl.SetBinContent(b,RateSharedRate)
        histSharedRate_cl.SetBinError(b,RateSharedRateErr)
        histSharedRate_cl.SetTitle("QCD")
    
    outf.cd()
    histPie_cl.Write()
    histSharedRate_cl.Write()
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
        OutFileCorrel="hltmenu_"+RootS+"_"+BS+"_combinedRate_correlations_"+str(ilumi)+"_"+DS+ '_' + vsn + ".root"

        theRateHists=[]
        if DS == "All":
            theRateHistsCorrel=[]
        theSamples=crossSections.keys()
        for Sample in theSamples:

            print ""
            
            outDir=os.path.join(OutDir,crossSections[Sample][1])
            outDir=outDir + BS + "_" + RootS + "_DS_" + DS + '_' + vsn
            if not os.path.isdir(outDir):
                os.makedirs(outDir)

            inDir=os.path.join(BaseDirectory,crossSections[Sample][1])
            #if (inDir.find("30to50") > -1 or inDir.find("50to80") > -1 or inDir.find("80to120") > 1
            #or inDir.find("20to30") > -1 or inDir.find("30to80") > -1 or inDir.find("80to170") > -1):
            #if inDir.find("30to50" or "50to80" or "80to120" or "20to30" or "30to80" or "80to170") > -1:
            #    inDir=inDir + BS + "_" + RootS + "_DS_" + DS + '_20140912_' + vsn
            #else:
            inDir=inDir + BS + "_" + RootS + "_DS_" + DS  + "_" + theDate + '_' + vsn
            if not os.path.isdir(inDir):
                print "Input directory    " + inDir + "   does not exist -- Exiting"
                print Sample
                sys.exit(1)

            combinedHist=GetHistsAndAddCounts(inDir,outDir)
            rateHist=ConvertToRate(crossSections[Sample][0]*1e-36,combinedHist)
            theRateHists.append(rateHist)
            if DS == "All":
                combinedCorrelHist=GetCorrelHistsAndAddCounts(inDir,outDir)
                rateCorrelHist=ConvertCorrelToRate(crossSections[Sample][0]*1e-36,combinedCorrelHist,combinedHist)
                theRateHistsCorrel.append(rateCorrelHist)

        # now add all the samples together
        if len(theRateHists)>0:
            outfile=os.path.join(OutDir,OutFile)
            AddCounts(theRateHists,outfile,False)
        else:
            print "Problem -- no rate histograms were created"
        if DS == "All" and len(theRateHistsCorrel)>0:
            outfileCorrel=os.path.join(OutDir,OutFileCorrel)
            AddCorrelCounts(theRateHistsCorrel,outfileCorrel,True)
        #else:
        #    print "Problem -- no rate histograms were created"
