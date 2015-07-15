#!/bin/bash

# QUEUE=cmscaf1nd
QUEUE=1nd
# QUEUE=test
SUB_SCRIPT=toBatch.sh

RFDIR=XXX  # if XXX do not copy output to RFDIR
# RFDIR=${CASTOR_HOME}/Beam/run62232_v13
# RFDIR=${CASTOR_HOME}/Beam/run62384_v13


ARGS=2
if [ $# -lt "$ARGS" ]
# Test number of arguments to script (always a good idea).
then
  echo "Usage: `basename $0` <cfgfile>  <logfile> "
  exit $E_BADARGS
fi
cfgfile=$1
logfile=$2


echo
echo "************************************************"
echo "Submitting job to the CERN $QUEUE batch queue"
echo "************************************************"
echo 
echo "CFG: " $cfgfile
echo "LOG: " $logfile
echo


## bsub -q ${QUEUE} -R "type==SLC4_64" -oo ${logfile} -N ${SUB_SCRIPT} ${cfgfile} ${RFDIR}
bsub -q ${QUEUE} -oo ${logfile} -N ${SUB_SCRIPT} ${cfgfile} ${RFDIR}
