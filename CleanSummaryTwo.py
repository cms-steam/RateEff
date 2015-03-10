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
for i in range(0,l-10):
    if 'studying' in lines[i]:
        words = re.split('  +',lines[i])
        hltname = words[1].strip('\^J').strip('\n').strip('?').strip('\^J')
        print hltname
        summary = open(pag+"Summary"+hltname+".txt",'w')
        summary.write("---++++!! *"+hltname+"*\n")
        summary.write("| *Sample* | *Rate* | *Error* |"+"\n")

        for j in range (i+4,i+20):
            samples = re.split(' +',lines[j])
            if len(samples)>2 and ('QCD' in samples[1] or 'EMEn' in samples[1] or 'MuEn' in samples[1] or 'WTo' in samples[1] or 'ZTo' in samples[1]):
                sample = samples[1]
                if 'in' in samples[2] : continue
                rate1=float(samples[2])
                if rate1 > 9e-3:
                    rate1='{:5.2f}'.format(rate1)
                    error1 = '{:5.2f}'.format(float(samples[4])) 
                    #print "One: ", hltname, " ", sample, " ", rate1, " ", error1
                    summary.write('|'+sample+'_withFilter|'+rate1+'|'+error1+'|''\n')
        

        for j in range (i+20,i+36):
            samples = re.split(' +',lines[j])
            if len(samples)>2 and ('QCD' in samples[1] or 'EMEn' in samples[1] or 'MuEn' in samples[1] or 'WTo' in samples[1] or 'ZTo' in samples[1]):
                sample = samples[1]
                if 'in' in samples[2] : continue
                rate2=float(samples[2])
                if rate2 > 9e-3:
                    rate2='{:5.2f}'.format(rate2)
                    error2 = '{:5.2f}'.format(float(samples[4]))
                    summary.write('|'+sample+'_noFilter|'+rate2+'|'+error2+'|''\n')
                    #print "Two: ", hltname, " ", sample, " ", rate2, " ", error2

total = open(pag+'Summary.txt','w')
for file in glob.glob(pag+'Summary*.txt'):
    with open(file) as myFile:
        li = myFile.readlines()
        if len(li)>3:
            for i in range(0,len(li)):
                total.write(li[i])
