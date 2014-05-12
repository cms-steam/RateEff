#!/bin/bash

condorFile=condor_rates.csh
submitFile=CondorJob.cfg

## theDate=`date '+%Y%m%d'`
theDate=20140501

## QCD
## DOMUCUTS=true  
DOMUCUTS=false   ## set to true in "if statement below" for bins 80-120 and below
DOELECUTS=false
## EM-Enriched
## DOMUCUTS=true
## DOELECUTS=false
## Mu-Enriched
## DOMUCUTS=false
## DOELECUTS=false
## W to enu, W to numu, DY 
## DOMUCUTS=false
## DOELECUTS=false

bs=25ns
## bs=50ns
#vsn=62X
vsn=700

for rs in 13TeV
## for rs in 8TeV
do
## QCD
for Bin in QCD_Pt-80to120_antiEM
#for Bin in QCD_Pt-5to10_antiEM QCD_Pt-10to15_antiEM QCD_Pt-15to30_antiEM QCD_Pt-30to50_antiEM QCD_Pt-50to80_antiEM QCD_Pt-80to120_antiEM QCD_Pt-120to170_antiEM QCD_Pt-170to300_nofilt QCD_Pt-300to470_nofilt QCD_Pt-470to600_nofilt QCD_Pt-600to800_nofilt QCD_Pt-800to1000_nofilt QCD_Pt-1000to1400_nofilt QCD_Pt-1400to1800_nofilt QCD_Pt-1800_nofilt
#for Bin in QCD_Pt-5to10_EMEnriched QCD_Pt-10to20_EMEnriched QCD_Pt-20to30_EMEnriched QCD_Pt-30to80_EMEnriched QCD_Pt-80to170_EMEnriched
#for Bin in QCD_Pt-15to20_MuEnrichedPt5_antiEM QCD_Pt-20to30_MuEnrichedPt5_antiEM QCD_Pt-30to50_MuEnrichedPt5_antiEM QCD_Pt-50to80_MuEnrichedPt5_antiEM QCD_Pt-80to120_MuEnrichedPt5_antiEM QCD_Pt-120to170_MuEnrichedPt5_antiEM QCD_Pt-170to300_MuEnrichedPt5_nofilt QCD_Pt-300to470_MuEnrichedPt5_nofilt QCD_Pt-470to600_MuEnrichedPt5_nofilt QCD_Pt-600to800_MuEnrichedPt5_nofilt QCD_Pt-800to1000_MuEnrichedPt5_nofilt QCD_Pt-1000_MuEnrichedPt5_nofilt
#for Bin in WToMuNu WToENu DYToEE DYToMuMu
do
    for DS in noprescl JetHT #BJetPlusX BTag DoubleElectron DoubleMu DoublePhoton DoublePhotonHighPt ElectronHad HTMHT JetHT MET MuEG MuHad MuOnia MultiJet PhotonHad SingleElectron SingleMu SinglePhoton Tau TauPlusX
    # for DS in noprescl 
    # for DS in TauPlusX
    do
	oldstring="XXXX"
	replstring="YYYY"
	rsstring="ZZZZ"
	bsstring="UUUU"
	argstring="BS RS VSN VTAG"

	newstring=${Bin}

	cfgFile=hltmenu_${DS}.cfg
	cfgFileORG=cfgs/${cfgFile}
	cfgFileNEW=hltmenu.cfg
	cp ${cfgFileORG} ${cfgFile}

	## newDir=${Bin}Out_${bs}_${rs}_DS_${DS}_noDoLeptonCuts_${theDate}
	newDir=${Bin}Out_${bs}_${rs}_DS_${DS}_${theDate}_${vsn}
	mkdir -p $newDir/logs

	#fileDir="${Bin}_TuneZ2star_${rs}_pythia8_${bs}"
	## echo $fileDir
	if [[ $Bin == QCD_Pt-15to30_antiEM || $Bin == QCD_Pt-30to50_antiEM || $Bin == QCD_Pt-50to80_antiEM || $Bin == QCD_Pt-80to120_antiEM || $Bin == QCD_Pt-120to170_antiEM || $Bin == QCD_Pt-170to300_nofilt || $Bin == QCD_Pt-300to470_nofilt || $Bin == QCD_Pt-470to600_nofilt || $Bin == QCD_Pt-600to800_nofilt || $Bin == QCD_Pt-800to1000_nofilt || $Bin == QCD_Pt-1000to1400_nofilt || $Bin == QCD_Pt-1400to1800_nofilt || $Bin == QCD_Pt-1800_nofil || $Bin == QCD_Pt-20to30_EMEnriched || $Bin == QCD_Pt-30to80_EMEnriched || $Bin == QCD_Pt-80to170_EMEnriched ]]; then
	    DOMUCUTS=true
	    BASENAME1=/eos/uscms/store/user/lpctrig/ingabu/TMD/PU20bx25/${Bin}_TuneZ2star_${rs}_pythia8/
	    BASENAME2=${BASENAME1}
	    nfiles=`ls /eos/uscms/store/user/lpctrig/ingabu/TMD/PU20bx25/${Bin}_TuneZ2star_${rs}_pythia8/ | grep -c ${vsn}`
	elif [[ $Bin == WToMuNu || $Bin == WToENu || $Bin == DYToEE || $Bin == DYToMuMu ]]; then
	    BASENAME1=/eos/uscms/store/user/lpctrig/ingabu/TMD/PU20bx25/${Bin}_Tune4C_${rs}-pythia8/
	    BASENAME2=${BASENAME1}
	    nfiles=`ls /eos/uscms/store/user/lpctrig/ingabu/TMD/PU20bx25/${Bin}_Tune4C_${rs}-pythia8/ | grep -c ${vsn}`
	else
	    BASENAME1=/eos/uscms/store/user/lpctrig/ingabu/TMD/PU20bx25/${Bin}_TuneZ2star_${rs}_pythia8/
	    BASENAME2=${BASENAME1}
	    nfiles=`ls /eos/uscms/store/user/lpctrig/ingabu/TMD/PU20bx25/${Bin}_TuneZ2star_${rs}_pythia8/ | grep -c ${vsn}`
	fi

	echo $BASENAME2
	echo $newDir  $nfiles

	tmpFileA=XXXXA.txt
	newFile=$newDir/${submitFile}

	arguments="${bs} ${rs} ${vsn} ${theDate}"
	sed -e 's/'$oldstring'/'$nfiles'/' ${submitFile} > ${tmpFileA}
	sed -e 's/'THEARGS'/'"${arguments}"'/' ${tmpFileA} > ${newFile}
	rm ${tmpFileA}
	# echo ${submitFile} ${newFile}

	newFile=$newDir/${condorFile}
	sed -e 's#'BASENAME'#'"${BASENAME1}"'#' ${condorFile} > ${newFile}
	# echo ${condorFile} ${newFile}

	tmpFileA=AXXXX.cfg
	tmpFileB=BXXXX.cfg
	tmpFileC=CXXXX.cfg
	newFile=$newDir/${cfgFileNEW}

	# sed -e 's/'$replstring'/'${fileDir}'/' ${cfgFile} > ${tmpFileA}
	sed -e 's#'BASENAME'#'"${BASENAME2}"'#' ${cfgFile} > ${tmpFileA}
	sed -e 's/'ABCD'/'${DOMUCUTS}'/' ${tmpFileA} > ${tmpFileB}
	sed -e 's/'EFGH'/'${DOELECUTS}'/' ${tmpFileB} > ${tmpFileC}
	sed -e 's/'VERSIONTAG'/'${theDate}'/' ${tmpFileC} > ${newFile}
	rm ${tmpFileA}
	rm ${tmpFileB}
	rm ${tmpFileC}
	rm ${cfgFile}
	echo ${cfgFile} ${newFile}

	cd $newDir
	condor_submit $submitFile
	cd ..
    done
done
done
