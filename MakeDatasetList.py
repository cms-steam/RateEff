#!/bin/python
import string
config=open("hltmenu_extractedhltmenu_2012_online_7E33v2p0_V2_5E33column.cfg",'r')
dataset=open("DatasetList_7e33V2_2012.list","w")

for line in config:
    if "HLT_" in line :
        list=line.strip(' ').strip('#').strip(' ').split(' ')
        if "HLT_" in list[0]:
            path=list[0].lstrip("(").rstrip(",").strip("\"")
            dataset.write("    "+str(path)+"\n")
    if "dataset" in line:
        list=line.split(' ')
        thedataset=list[2]
        dataset.write(str(thedataset)+":\n")
                

