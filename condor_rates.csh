#!/bin/csh
 
set workDir=$ANALYZEDIRECTORY

echo "Beginning condor_rates.csh"

echo "-------------------------------"
echo "Current Directory: "
pwd
echo "CONDOR_SCRATCH_DIR: $_CONDOR_SCRATCH_DIR"
echo "-------------------------------"

## Project area: 
setenv JINGYU /uscms_data/d3/jingyu/TMD/CMSSW_7_3_1_patch1/src/HLTrigger/HLTanalyzers/test/RateEff
cd $JINGYU
echo "Project dir: " 
pwd
source /cvmfs/cms.cern.ch/cmsset_default.csh
setenv SCRAM_ARCH slc6_amd64_gcc491
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
setenv CFG hltmenu_$whichproc.cfg

echo -n " ---- Configuration file ------------"
echo 
cat $CFG

$JINGYU/OHltRateEff $CFG

echo "Directory contents after job"
echo 
ls -xsFt
echo
echo "---------------------------"
echo
rm -f *.tex
rm -f MyEffHist*.root
mv hltmenu_13TeV_7.0e33_${VTAG}.root hltmenu_${rs}_7e33_${VTAG}_$whichproc.root
mv hltmenu_13TeV_7.0e33_${VTAG}.twiki hltmenu_${rs}_7e33_${VTAG}_$whichproc.twiki
mv PATH_PAGv3_correlations.root PATH_PAGv3_correlations_${rs}_${VTAG}_$whichproc.root

echo "Job finished on `date`" 

