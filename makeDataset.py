#!/bin/python
import string
config=open("hltmenu_8e33.cfg",'r')
dataset=open("DatasetList_2012_8e33V3.list","w")
for line in config:
    if "HLT_" in line :
        list=line.strip(' ').strip('#').strip(' ').split(' ')
        if "HLT_" in list[0]:
            path=list[0].lstrip("(").rstrip(",").strip("\"")
            print "   "+str(path)
    if "dataset" in line:
        list=line.split(' ')
        dataset=list[2]
        print
        print str(dataset)+":"
                

