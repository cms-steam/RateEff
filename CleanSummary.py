import os
from array import array 
import sys
import glob 
import re

filein = open(sys.argv[1],'r')
pag = sys.argv[1].strip('.txt')
lines = filein.readlines()
#print lines
l = len(lines)
for i in range(0,l-22):
    if 'studying' in lines[i]:
        words = re.split('  +',lines[i])
        hltname = words[1].strip('\^J').strip('\n').strip('?').strip('\^J')
        print hltname
        summary = open(pag+"Summary"+hltname+".txt",'w')
        summary.write("---++++!! *"+hltname+"*\n")
        summary.write("| *Sample* | *Rate* | *Error* |"+"\n")
#        print i
        if i<l-23:
            for j in range (i,i+22):
                samples = re.split(' +',lines[j])
            #print len(samples)
                if len(samples)>2 and ('QCD' in samples[1] or 'EMEn' in samples[1] or 'MuEn' in samples[1] or 'WTo' in samples[1] or 'ZTo' in samples[1]):
                    sample = samples[1]
                    if 'in' in samples[2] : continue
                    rate=float(samples[2])
                    if rate > 9e-3 : 
                        rate='{:5.2f}'.format(rate)
                        error = '{:5.2f}'.format(float(samples[4]))
                    #                    print hltname,sample,rate,error
                        summary.write('|'+sample+'|'+rate+'|'+error+'|'+'\n')
total = open(pag+'Summary.txt','w')
for file in glob.glob(pag+'Summary*.txt'):
    with open(file) as myFile:
        li = myFile.readlines()
        if len(li)>3:
            for i in range(0,len(li)):
                total.write(li[i])
