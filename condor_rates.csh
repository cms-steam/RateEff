#!/bin/csh
 
set workDir=$ANALYZEDIRECTORY

echo "Beginning condor_rates.csh"

echo "-------------------------------"
echo "Current Directory: "
pwd
echo "CONDOR_SCRATCH_DIR: $_CONDOR_SCRATCH_DIR"
echo "-------------------------------"

## Project area: Inga's directory
setenv INGA /uscms_data/d3/ingabu/TMD/CMSSW_7_0_0/src/HLTrigger/HLTanalyzers/test/RateEff
cd $INGA
echo "Project dir: " 
pwd
source /uscmst1/prod/sw/cms/setup/cshrc prod
setenv SCRAM_ARCH slc5_amd64_gcc481
eval `scram runtime -csh`
source setup.csh
##

cd $_CONDOR_SCRATCH_DIR
echo "Condor Directory: "
pwd


@ pid = $argv[1] + 1
set bs = $argv[2]
set rs = $argv[3]
set vsn = $argv[4]
set VTAG = $argv[5]
set whichproc = $argv[6]


## setenv CFG $workDir/hltmenu_prescales.cfg
setenv CFG $workDir/hltmenu_$whichproc.cfg

echo -n " ---- Configuration file ------------"
echo 
cat $CFG

$INGA/OHltRateEff $CFG

echo "Directory contents after job"
echo 
ls -xsFt
echo
echo "---------------------------"
echo
rm -f *.tex
rm -f MyEffHist*.root
mv hltmenu_8TeV_7.0e33_${VTAG}.root hltmenu_${rs}_8.0e33_${VTAG}_$whichproc.root
mv hltmenu_8TeV_7.0e33_${VTAG}.twiki hltmenu_${rs}_8.0e33_${VTAG}_$whichproc.twiki
mv DatasetList_2012_8e33V3_correlations.root DatasetList_2012_8e33V3_correlations_${rs}_${VTAG}_$whichproc.root

echo "Job finished on `date`" 

