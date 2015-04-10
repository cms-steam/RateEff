#crossSections8TeV={
    ## QCD Cross sections
    #'QCD15to30'    :(9.8828742E8,"QCD_Pt-15to30Out_"),
    #'QCD30to50'    :(6.6285328E7,"QCD_Pt-30to50Out_"),
    #'QCD50to80'    :(8148778.0,"QCD_Pt-50to80Out_"),
    #'QCD80to120'   :(1033680.0,"QCD_Pt-80to120Out_"),
    #'QCD120to170'  :(156293.3,"QCD_Pt-120to170Out_"),
    #'QCD170to300'  :(34138.15,"QCD_Pt-170to300Out_"),
    #'QCD300to470'  :(1759.549,"QCD_Pt-300to470Out_"),
    #'QCD470to600'  :(113.8791,"QCD_Pt-470to600Out_"),
    #'QCD600to800'  :(26.9921,"QCD_Pt-600to800Out_"),
    #'QCD800to1000' :(3.550036,"QCD_Pt-800to1000Out_"),
    #'QCD1000to1400':(0.737844,"QCD_Pt-1000to1400Out_"),
    #'QCD1400to1800':(0.03352235,"QCD_Pt-1400to1800Out_"),
    ## 'QCD1800'      :(0.001829005,"QCD_Pt-1800Out_"),
    ## EM Enriched cross sections    
    #'EMEnr20to30'    :(2914860.,"QCD_Pt-20to30_EMEnrichedOut_"),
    #'EMEnr30to80'    :(4615893.,"QCD_Pt-30to80_EMEnrichedOut_"),
    #'EMEnr80to170'   :(183294.9,"QCD_Pt-80to170_EMEnrichedOut_"),
    ## Mu Enriched cross sections
    #'MuEnr15to20'    :(2738580.,"QCD_Pt-15to20_MuEnrichedPt5Out_"),
    #'MuEnr20to30'    :(1865500.,"QCD_Pt-20to30_MuEnrichedPt5Out_"),
    #'MuEnr30to50'    :(806298.,"QCD_Pt-30to50_MuEnrichedPt5Out_"),
    #'MuEnr50to80'    :(176187.6,"QCD_Pt-50to80_MuEnrichedPt5Out_"),
    #'MuEnr80to120'   :(40448.,"QCD_Pt-80to120_MuEnrichedPt5Out_"),
    ## W and Z cross sections
    #'WToENu'         :(9140.0,"WToENuOut_"),
    #'WToMuNu'        :(9130.0,"WToMuNuOut_"),
    #'ZToMuMu'        :(1510.0,"DYToMuMu_M_20Out_"),
    #'ZToEE'          :(1510.0,"DYToEE_M_20Out_"),
    ## Photon Cross Section (Flat. Weights already applied by IB)
    ## 'G_Pt-15to3000'  :(2.064133E7,"PUPhoton")
    #}

## Use this list if you ran hlt_filter.py when making some of your ntuples.
crossSections13TeV={
#    ## QCD Cross sections
#    #1st number is the cross section, the last number is EM anti-filter efficiency
#    #for pt bins 5-170, which you can get using efficiency.py
#    #'QCD5to10'    :(80710000000.*0.999999,"QCD_Pt-5to10_antiEMOut_"),  
#    #'QCD10to15'    :(7528000000.*0.9999,"QCD_Pt-10to15_antiEMOut_"),
    #'QCD15to30'    :(2237000000.*0.9959,"QCD_Pt-15to30_nofilt_noSilvioOut_"),
    #'QCD15to30'    :(2237000000.*0.18802,"QCD_Pt-15to30_nofiltOut_"),
    'QCD30to50'    :(161500000.*0.61315,"QCD_Pt-30to50_antiEMOut_"),  #third number is efficiency of Silvio's filter
    'QCD50to80'    :(22110000.*0.79573,"QCD_Pt-50to80_antiEMOut_"),
    'QCD80to120'   :(3000114.3*0.83154,"QCD_Pt-80to120_antiEMOut_"),
    'QCD120to170'  :(493200.*0.83167,"QCD_Pt-120to170_antiEMOut_"),
    'QCD170to300'  :(120300.,"QCD_Pt-170to300_nofiltOut_"),
    'QCD300to470'  :(7475.,"QCD_Pt-300to470_nofiltOut_"),
    'QCD470to600'  :(587.1,"QCD_Pt-470to600_nofiltOut_"),
    'QCD600to800'  :(167.,"QCD_Pt-600to800_nofiltOut_"),
    'QCD800to1000' :(28.25,"QCD_Pt-800to1000_nofiltOut_"),
#    'QCD1000to1400':(8.195,"QCD_Pt-1000to1400_nofiltOut_"),
#    'QCD1400to1800':(0.7346,"QCD_Pt-1400to1800_nofiltOut_"),
#    'QCD1800'      :(0.1091,"QCD_Pt-1800_nofiltOut_"),
#     #EM Enriched cross sections    
#    #the 2nd number is the EM filtering efficiency you can get from McM website
#    #'EMEnr5to10'    :(80710000000.*0.024,"QCD_Pt-5to10_EMEnrichedOut_"),
#    #'EMEnr10to20'    :(8838000000.*0.143,"QCD_Pt-10to20_EMEnrichedOut_"),
    #'EMEnr20to30'    :(677300000.*0.007,"QCD_Pt-20to30_EMEnrichedOut_"),
    'EMEnr30to80'    :(185900000.*0.056,"QCD_Pt-30to80_EMEnrichedOut_"),
    'EMEnr80to170'   :(3529000.*0.158,"QCD_Pt-80to170_EMEnrichedOut_"),
#     #Mu Enriched cross sections
#    #the 2nd number is the MuEnriched filtering efficiency you can get from McM website
    #'MuEnr15to20'    :(1576000000.*0.0039*0.9991,"QCD_Pt-15to20_MuEnrichedPt5_antiEMOut_"),
    #'MuEnr20to30'    :(675300000.*0.0065*0.9922,"QCD_Pt-20to30_MuEnrichedPt5_antiEMOut_"),
    #'MuEnr30to50'    :(164300000.*0.00816*0.9606,"QCD_Pt-30to50_MuEnrichedPt5_antiEMOut_"),
    #'MuEnr50to80'    :(21810000.*0.01522*0.9074,"QCD_Pt-50to80_MuEnrichedPt5_antiEMOut_"),
    #'MuEnr80to120'   :(2999000.*0.02424*0.8735,"QCD_Pt-80to120_MuEnrichedPt5_antiEMOut_"),
    #'MuEnr120to170'   :(493200.*0.0473*0.8602,"QCD_Pt-120to170_MuEnrichedPt5_antiEMOut_"),
    #'MuEnr170to300'   :(12030.*0.0676,"QCD_Pt-170to300_MuEnrichedPt5_nofiltOut_"),
    #'MuEnr300to470'   :(7475.*0.0864,"QCD_Pt-300to470_MuEnrichedPt5_nofiltOut_"),
    #'MuEnr470to600'   :(587.1*0.1024,"QCD_Pt-470to600_MuEnrichedPt5_nofiltOut_"),
    #'MuEnr600to800'   :(167.*0.0996,"QCD_Pt-600to800_MuEnrichedPt5_nofiltOut_"),
    #'MuEnr800to1000'   :(28.25*0.1033,"QCD_Pt-800to1000_MuEnrichedPt5_nofiltOut_"),
    #'MuEnr1000'   :(8.975*0.1097,"QCD_Pt-1000_MuEnrichedPt5_nofiltOut_"),
#     #W and Z cross sections
    'WToENu'         :(16000.,"WToENuOut_"),
    'WToMuNu'        :(16100.,"WToMuNuOut_"),
    'ZToMuMu'        :(6870.,"DYToMuMuOut_"),
    'ZToEE'          :(6960.,"DYToEEOut_"),
#    # Photon Cross Section (Flat. Weights already applied by IB)
#    # 'G_Pt-15to3000'  :(2.064133E7,"PUPhoton")
#    
}
#
## Use this list if you only ran hlt_nofilter.py when making some of your ntuples.
#crossSections13TeV={
#    ## QCD Cross sections
#    #1st number is the cross section, the last number is EM anti-filter efficiency
#    #for pt bins 5-170, which you can get using efficiency.py
#    #'QCD5to10'    :(80710000000.,"QCD_Pt-5to10_antiEMOut_"),  
#    #'QCD10to15'    :(7528000000.,"QCD_Pt-10to15_antiEMOut_"),
#    #'QCD15to30'    :(2237000000.,"QCD_Pt-15to30_antiEMOut_"),
    #'QCD30to50'    :(161500000.,"QCD_Pt-30to50_nofiltOut_"),
    #'QCD50to80'    :(22110000.,"QCD_Pt-50to80_nofiltOut_"),
    #'QCD80to120'   :(3000114.3,"QCD_Pt-80to120_nofiltOut_"),
    #'QCD120to170'  :(493200.,"QCD_Pt-120to170_nofiltOut_"),
    #'QCD170to300'  :(120300.,"QCD_Pt-170to300_nofiltOut_"),
    #'QCD300to470'  :(7475.,"QCD_Pt-300to470_nofiltOut_"),
    #'QCD470to600'  :(587.1,"QCD_Pt-470to600_nofiltOut_"),
    #'QCD600to800'  :(167.,"QCD_Pt-600to800_nofiltOut_"),
    #'QCD800to1000' :(28.25,"QCD_Pt-800to1000_nofiltOut_"),
    #'QCD1000to1400':(8.195,"QCD_Pt-1000to1400_nofiltOut_"),
#    'QCD1400to1800':(0.7346,"QCD_Pt-1400to1800_nofiltOut_"),
#    'QCD1800'      :(0.1091,"QCD_Pt-1800_nofiltOut_"),
##     #W and Z cross sections
    #'WToENu'         :(16000.,"WToENuOut_"),
    #'WToMuNu'        :(16100.,"WToMuNuOut_"),
    #'ZToMuMu'        :(6870.,"DYToMuMuOut_"),
    #'ZToEE'          :(6960.,"DYToEEOut_"),
#}
