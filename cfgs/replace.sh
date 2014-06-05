#!/bin/bash

for filename in `ls hltmenu*.cfg`
do
    echo $filename
    tmpFileA=AXXXX.cfg
    sed -e "s/DatasetList_2012_8e33v3.list/DatasetList_2012_8e33V3.list/" ${filename} > ${tmpFileA}
    cp $tmpFileA $filename
    rm $tmpFileA

done
