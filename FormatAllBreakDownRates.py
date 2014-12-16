import os
from array import array 
import sys
import glob 
import re
#import numpy as np
#import plotPathsOne
#dataSets = ['B2G']

dataSets = ['B2G','SUSY','EXO','Higgs','TOP','BPH','E_GAMMA','Taus','SMP','JET_MET','BTV']
print dataSets
for d in range(0, len(dataSets)):
    print dataSets[d]
filein1 = open(sys.argv[1],'r')
lines1 = filein1.readlines()
#l = len(lines1)
for d in range(0, len(dataSets)):
    #command = "'python plotPathsOne.py "
    #sendlog = " >& "
    #dataset = '"'+dataSets[d]+'"'
    string = "python plotRatePerSampleOne.py "
    pag = "'"+dataSets[d]+"'"
    string2 = ">& " 
    pagtxt = dataSets[d]+'.txt'
    os.system(string+pag+string2+pagtxt)
    #print dataset 
    #os.system(command+dataset+"'" + sendlog + dataSets[d] + ".txt")
for d in range(0,len(dataSets)):
    cmd = "python CleanSummary.py "
    pagtxt = dataSets[d]+'.txt'
    os.system(cmd+ pagtxt)


    #os.system('python makeDStables.py') 

