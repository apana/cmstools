#!/bin/sh

for a in {1..11}
do
  # submit.sh MWGR42_highrate_v4_${a}.py runMWGR42_highrate_v4_${a}.log
  # submit.sh MWGR43_highrate_v6_${a}.py runMWGR43_highrate_v6_${a}.log

  config=cfgs/HLTBitAnalysis_cfg_${a}.py
  logfile=logs/HLTBitAnalysis_cfg_${a}.log

  submit.sh $config $logfile
done
echo
echo done
echo
