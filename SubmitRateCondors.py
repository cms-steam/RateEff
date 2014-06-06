import sys, os, glob, subprocess


condorFile = 'condor_rates.csh'
submitFile = 'CondorJob.cfg'
 
DOMUCUTS = 'false'   ## set to true in "if statement below" for bins 80-120 and below
DOELECUTS = 'false'

bs = '25ns'
#bs = '50ns'
vsn = '62X'
#vsn = '700'
rs = '13TeV'
theDate = '20140604'

#Bins = ['QCD_Pt-20to30_MuEnrichedPt5_antiEM']
#Bins = ['QCD_Pt-5to10_antiEM', 'QCD_Pt-10to15_antiEM', 'QCD_Pt-15to30_antiEM', 'QCD_Pt-30to50_antiEM', 'QCD_Pt-50to80_antiEM', 'QCD_Pt-80to120_antiEM', 'QCD_Pt-120to170_antiEM', 'QCD_Pt-170to300_nofilt', 'QCD_Pt-300to470_nofilt', 'QCD_Pt-470to600_nofilt', 'QCD_Pt-600to800_nofilt', 'QCD_Pt-800to1000_nofilt', 'QCD_Pt-1000to1400_nofilt', 'QCD_Pt-1400to1800_nofilt', 'QCD_Pt-1800_nofilt']
#Bins = ['QCD_Pt-5to10_EMEnriched', 'QCD_Pt-10to20_EMEnriched', 'QCD_Pt-20to30_EMEnriched', 'QCD_Pt-30to80_EMEnriched', 'QCD_Pt-80to170_EMEnriched']
#Bins = ['QCD_Pt-15to20_MuEnrichedPt5_antiEM', 'QCD_Pt-20to30_MuEnrichedPt5_antiEM', 'QCD_Pt-30to50_MuEnrichedPt5_antiEM', 'QCD_Pt-50to80_MuEnrichedPt5_antiEM', 'QCD_Pt-80to120_MuEnrichedPt5_antiEM', 'QCD_Pt-120to170_MuEnrichedPt5_antiEM', 'QCD_Pt-170to300_MuEnrichedPt5_nofilt', 'QCD_Pt-300to470_MuEnrichedPt5_nofilt', 'QCD_Pt-470to600_MuEnrichedPt5_nofilt', 'QCD_Pt-600to800_MuEnrichedPt5_nofilt', 'QCD_Pt-800to1000_MuEnrichedPt5_nofilt', 'QCD_Pt-1000_MuEnrichedPt5_nofilt']
#Bins = ['WToMuNu', 'WToENu', 'DYToEE', 'DYToMuMu']
Bins = ['QCD_Pt-15to30_antiEM', 'QCD_Pt-30to50_antiEM', 'QCD_Pt-50to80_antiEM', 'QCD_Pt-80to120_antiEM', 'QCD_Pt-120to170_antiEM', 'QCD_Pt-170to300_nofilt', 'QCD_Pt-300to470_nofilt', 'QCD_Pt-470to600_nofilt', 'QCD_Pt-600to800_nofilt', 'QCD_Pt-800to1000_nofilt', 'QCD_Pt-1000to1400_nofilt', 'QCD_Pt-1400to1800_nofilt', 'QCD_Pt-1800_nofilt', 'QCD_Pt-10to20_EMEnriched', 'QCD_Pt-20to30_EMEnriched', 'QCD_Pt-30to80_EMEnriched', 'QCD_Pt-80to170_EMEnriched', 'QCD_Pt-15to20_MuEnrichedPt5_antiEM', 'QCD_Pt-20to30_MuEnrichedPt5_antiEM', 'QCD_Pt-30to50_MuEnrichedPt5_antiEM', 'QCD_Pt-50to80_MuEnrichedPt5_antiEM', 'QCD_Pt-80to120_MuEnrichedPt5_antiEM', 'QCD_Pt-120to170_MuEnrichedPt5_antiEM', 'QCD_Pt-170to300_MuEnrichedPt5_nofilt', 'QCD_Pt-300to470_MuEnrichedPt5_nofilt', 'QCD_Pt-470to600_MuEnrichedPt5_nofilt', 'QCD_Pt-600to800_MuEnrichedPt5_nofilt', 'WToMuNu', 'WToENu', 'DYToEE', 'DYToMuMu']

DS = ['noprescl', 'BJetPlusX', 'BTag', 'DoubleElectron', 'DoubleMu', 'DoublePhoton', 'DoublePhotonHighPt', 'ElectronHad', 'HTMHT', 'JetHT', 'MET', 'MuEG', 'MuHad', 'MuOnia', 'MultiJet', 'PhotonHad', 'SingleElectron', 'SingleMu', 'SinglePhoton', 'Tau', 'TauPlusX']
#DS = ['MultiJet']

for b in range(len(Bins)):

    for d in range(len(DS)):

        cfgFile = 'cfgs/hltmenu_' + DS[d] + '.cfg'
        cfgFileOld = 'hltmenu_' + DS[d] + '.cfg'

	newDir = Bins[b] + 'Out_' + bs + '_' + rs + '_DS_' + DS[d] + '_' + theDate + '_' + vsn
        newDir2 = newDir + '/logs'

        if not os.path.exists(newDir2):
            os.makedirs(newDir2)

        if (Bins[b] == 'QCD_Pt-15to30_antiEM' or Bins[b] == 'QCD_Pt-30to50_antiEM' or Bins[b] == 'QCD_Pt-50to80_antiEM' or Bins[b] == 'QCD_Pt-80to120_antiEM' or Bins[b] == 'QCD_Pt-120to170_antiEM' or Bins[b] == 'QCD_Pt-170to300_nofilt' or Bins[b] == 'QCD_Pt-300to470_nofilt' or Bins[b] == 'QCD_Pt-470to600_nofilt' or Bins[b] == 'QCD_Pt-600to800_nofilt' or Bins[b] == 'QCD_Pt-20to30_EMEnriched' or Bins[b] == 'QCD_Pt-30to80_EMEnriched' or Bins[b] == 'QCD_Pt-80to170_EMEnriched'):
            DOMUCUTS = 'true'
            BASENAME1 = '/eos/uscms/store/user/lpctrig/ingabu/TMD/PU20bx25/' + Bins[b] + '_TuneZ2star_' + rs + '_pythia8/'
        elif (Bins[b] == 'WToMuNu' or Bins[b] == 'WToENu' or Bins[b] == 'DYToEE' or Bins[b] == 'DYToMuMu'):
            DOMUCUTS = 'false'
            BASENAME1 = '/eos/uscms/store/user/lpctrig/ingabu/TMD/PU20bx25/' + Bins[b]+ '_Tune4C_' + rs + '-pythia8/'
        else:
            DOMUCUTS = 'false'
            BASENAME1 = '/eos/uscms/store/user/lpctrig/ingabu/TMD/PU20bx25/' + Bins[b] + '_TuneZ2star_' + rs + '_pythia8/'


        print "InDir: ", BASENAME1

        #File range for input to code e.g, 1-50 then r =50
        r = 50

        s = 1   #starting file
        e = r   #end file
            
        allfiles = glob.glob(BASENAME1 + "*" + vsn + "*.root")
        af = []
        for allf in allfiles:
            af.append(allf.split('/')[-1])

        Totfiles = len(af)
        whichproc = 1

        while (s <= Totfiles):

            infiles = []
            endrange = s+r-1
            if endrange > Totfiles:
                endrange = Totfiles
            for moo in range(s-1, endrange):
                infiles.append(af[moo])

            inf = '", "'.join(infiles)
            #print inf
            
            subprocess.call('cp ' + condorFile + ' ' + newDir, shell=True)
            subprocess.call('cp ' + submitFile + ' ' + newDir, shell=True)
            arguments = bs + ' ' + rs + ' ' + vsn + ' ' + theDate + ' ' + str(whichproc)
            subprocess.call('sed -i \'s/THEARGS/' + arguments + '/g\'' + ' ' + newDir + '/' + submitFile, shell=True)

            cfgFileNew = 'hltmenu_' + str(whichproc) + '.cfg'
            subprocess.call('cp ' + cfgFile + ' ' + newDir, shell=True)
            subprocess.call('mv ' + newDir + '/' + cfgFileOld + ' ' + newDir + '/' + cfgFileNew, shell=True)

            subprocess.call('sed -i \'s#BASENAME#' + BASENAME1 + '#g\'' + ' ' + newDir + '/' + cfgFileNew, shell=True)
            subprocess.call('sed -i \'s/BASEFILES/' + inf + '/g\'' + ' ' + newDir + '/' + cfgFileNew, shell=True)
            subprocess.call('sed -i \'s/ABCD/' + DOMUCUTS + '/g\'' + ' ' + newDir + '/' + cfgFileNew, shell=True)
            subprocess.call('sed -i \'s/EFGH/' + DOELECUTS + '/g\'' + ' ' + newDir + '/' + cfgFileNew, shell=True)
            subprocess.call('sed -i \'s/VERSIONTAG/' + theDate + '/g\'' + ' ' + newDir + '/' + cfgFileNew, shell=True)

            os.chdir(newDir)

            subprocess.call('condor_submit ' + submitFile, shell=True)
            os.chdir('..')

            s = s + r
            e = e + r
            whichproc = whichproc + 1

        

        
        


