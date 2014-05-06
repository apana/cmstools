#!/bin/bash

# dir="$STOREUSER"/lpchbb/apana/Ntuple_Step1V42_Step2Tag_EDMV42_Step2_V4a_MC
# dir="$STOREUSER"/lpchbb/apana/Ntuple_Step1V42_Step2Tag_EDMV42_Step2_V4_Data
dir="$STOREUSER"/lpchbb/apana/Ntuple_Step1V42_Step2Tag_EDMV42_Step2_V4_DataMoreStat

CMD=dcsize

for file in `ls -t $dir`
do

    echo ${dir}/${file}
    $CMD ${dir}/${file}
    echo

done