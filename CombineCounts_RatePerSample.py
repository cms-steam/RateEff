import math,ROOT,sys,os
from ROOT import gROOT, TFile, TChain, TAxis, TTree, TH1F, TF1,SetOwnership, TObjString, TString

BaseDirectory="/uscms/physics_grp/lpctrig/ingabu/TMD/GetCounts"
#BaseDirectory="./"

theLabels=["QCD30to50","QCD50to80","QCD80to120","QCD120to170","QCD170to300","QCD300to470","QCD470to600","QCD600to800","QCD800to1000","QCD1000to1400", "QCD1400to1800","EMEnr20to30","EMEnr30to80","EMEnr80to170","MuEnr20to30","MuEnr30to50","MuEnr50to80","MuEnr80to120","WToENu","ZToEE","WToMuNu","ZToMuMu"]

RootS="13TeV"
## RootS="8TeV"

## BS="50ns"
BS="25ns"

vsn = '700'
#vsn = '62X'
#vsn='53X'

# ilumi = 5.5e33  # run 196532
# ilumi = 5.3e33  # run 207884
# ilumi = 3.12e33 # run 207889
# ilumi = 1.7e34 # projected lumi for 13 TeV
ilumi = 1.1e34 # projected lumi for 13 TeV, 25 ns bunch spacing

DataSets=["BJetPlusX", "BTag", "DoubleElectron", "DoubleMu", "DoublePhoton", "DoublePhotonHighPt", "ElectronHad", "HTMHT", "JetHT", "MET", "MuEG", "MuHad", "MuOnia", "MultiJet", "PhotonHad", "SingleElectron", "SingleMu", "SinglePhoton", "Tau", "TauPlusX"]
##DataSets=['noprescl', 'BJetPlusX', 'BTag', 'DoubleElectron', 'DoubleMu', 'DoublePhoton', 'DoublePhotonHighPt', 'ElectronHad', 'HTMHT', 'JetHT', 'MET', 'MuEG', 'MuHad', 'MuOnia', 'MultiJet', 'PhotonHad', 'SingleElectron', 'SingleMu', 'SinglePhoton', 'Tau', 'TauPlusX']

#theDate="20131029"
## theDate="20131128"
#theDate="20140623JustQCD"
theDate="20140803"

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

OutDir=os.path.join(BaseDirectory,"resultsByDS" + "_" + RootS +"_"+ theDate + '_no15to30_' + vsn + 'CorrMuCuts',str(ilumi))

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


def AddCounts(rootFiles,outfile,sumEvents=True):

    outf = TFile(outfile,"RECREATE");
    SetOwnership( outf, False )   # tell python not to take ownership
    print "Output written to: ", outfile
    
    theSamples=crossSections.keys()
    histlist=[]
    i=-1
    handles=[]
    for f in rootFiles:
        i+=1
        print i,f
        fstart=f.split('/')
        fstart=fstart[len(fstart)-2]
        fstart=fstart[0:fstart.find('Out_')]
        print fstart
        thelabel=" "
        for sample in theSamples :
            if  crossSections[sample][1].find(fstart)==0 :
                thelabel=sample
                break
        print thelabel
        infile = TFile.Open(f)
        handles.append(infile)
        histInd = infile.Get("individual")
        histCum = infile.Get("cumulative")
        if sumEvents:
            nevt = infile.Get("NEVTS")
        
        if i==0:
            for path in histInd.GetXaxis().GetLabels():
                name=path.GetString().Data()
                h=TH1F( name[:name.rfind("_")] , 'Rates for ' + name, len(theLabels), 0, float(len(theLabels)) )
                h.Sumw2()
                isa=0
                for sample in theLabels :
                    isa+=1
                    print "bin",isa," label ",sample
                    h.GetXaxis().SetBinLabel(isa,sample)
                bin=h.GetXaxis().FindBin(thelabel)
                err2=histInd.GetBinError(histInd.GetXaxis().FindBin(name))
                h.SetBinContent(bin,histInd.GetBinContent(histInd.GetXaxis().FindBin(name)))
                h.SetBinError(bin,err2)
                histlist.append(h)                
            histInd_all = histInd.Clone()
            histCum_all = histCum.Clone()
            if sumEvents: NEVTS = nevt.Clone()
        else:            
            for h in histlist:
                name=h.GetTitle().split(' ')[2]
                bin=h.GetXaxis().FindBin(thelabel)
                content=h.GetBinContent(bin)
                error=h.GetBinError(bin)
                err2=histInd.GetBinError(histInd.GetXaxis().FindBin(name))
                error=math.sqrt(error*error+err2*err2)
                h.SetBinContent(bin,content+histInd.GetBinContent(histInd.GetXaxis().FindBin(name)))
                h.SetBinError(bin,error)
                
            histInd_all.Add(histInd)
            histCum_all.Add(histCum)
            if sumEvents: NEVTS.Add(nevt)

    outf.cd()
    histInd_all.Write()
    histCum_all.Write()
    for h in histlist:
        h.Write()
    if sumEvents: NEVTS.Write()
    outf.Close()

    for inf in handles:
        inf.Close()
    

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
        for Sample in sorted(theSamples):

            ## print crossSections[Sample][1],crossSections[Sample][1].find("QCD_Pt-15to30Out")
            #if crossSections[Sample][1].find("QCD_Pt-15to30_antiEMOut")==0 or crossSections[Sample][1].find("QCD_Pt-15to20")==0:
            #if crossSections[Sample][1].find("QCD_Pt-5to10_antiEMOut_")==0  or crossSections[Sample][1].find("QCD_Pt-10to15_antiEMOut_")==0 or crossSections[Sample][1].find("QCD_Pt-15to30_antiEMOut_")==0 or crossSections[Sample][1].find("QCD_Pt-5to10_EMEnrichedOut_")==0 or crossSections[Sample][1].find("QCD_Pt-10to20_EMEnrichedOut_")==0 or crossSections[Sample][1].find("QCD_Pt-800to1000_MuEnrichedPt5_nofiltOut_")==0 or crossSections[Sample][1].find("QCD_Pt-1000_MuEnrichedPt5_nofiltOut_")==0 :
            #    continue
#            print ""
            
            inDir=os.path.join(OutDir,crossSections[Sample][1])
            inDir=inDir + BS + "_" + RootS + "_DS_" + DS + '_' + vsn
#            inDir=inDir + BS + "_" + RootS + "_DS_" + DS 
            if not os.path.isdir(inDir):
                print "Input directory    " + inDir + "   does not exist -- Exiting"
                print Sample
                sys.exit(1)

            rateHist=os.path.join(inDir,'hltmenu_'+RootS+'_8.0e33_'+theDate+'_rates.root')
#            rateHist=os.path.join(inDir,'hltmenu_'+RootS+'_7.0e33_20140129_rates.root')
# list of rootfiles containing full sample rates for a dataset
            theRateHists.append(rateHist)

        # now add all the samples together
        if len(theRateHists)>0:
            FinalDir='/uscms/physics_grp/lpctrig/ingabu/TMD/GetCounts/Muriel/0803CorrMuCuts/'
            outfile=os.path.join(FinalDir,OutFile)
# adds the rates of all the samples for one dataset
            AddCounts(theRateHists,outfile,False)
        else:
            print "Problem -- no rate histograms were created"
