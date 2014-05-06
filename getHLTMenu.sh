#!/bin/bash
#

# MENU="/users/apana/L1FastJet/420HLT16/Full/V12"
# OUTFILE=hlt12_L1.py

# MENU="/users/jalimena/online_3e33v1p1/For429HLT1hltpatch1/V4"
# OUTFILE=hlt_l1fastjet.py

# MENU="/online/collisions/2011/3e33/v1.1/HLT/V10"
# OUTFILE=hlt_default.py

# MENU="/online/collisions/2011/5e33/v1.1/HLT/V6"
# MENU="/users/apana/L1FastJet/Val/HLT/V2"
# OUTFILE=hlt_l1fastjet.py

MENU="/online/collisions/2011/5e33/v1.4/HLT/V6"
# OUTFILE=hlt_5e33FromSkimMinPre.py
OUTFILE=hlt_5e33ReRunEMU_tst.py
OUTPUT=minimal

# hltGetConfiguration ${MENU} --full --offline --data --unprescale --process TEST --l1-emulator --l1 L1GtTriggerMenu_L1Menu_Collisions2011_v4_mc,sqlite_file:/afs/cern.ch/user/g/ghete/public/L1Menu/L1Menu_Collisions2011_v4/sqlFile/L1Menu_Collisions2011_v4_mc.db >& ${OUTFILE}

# hltGetConfiguration ${MENU} --full --offline --data --unprescale --process TEST --output $OUTPUT --l1-emulator >& ${OUTFILE}
# hltGetConfiguration ${MENU} --full --offline --data --unprescale --process TEST --output $OUTPUT >& ${OUTFILE}


# hltGetConfiguration ${MENU} --full --offline --data --unprescale --process TEST --output $OUTPUT --l1-emulator --l1 L1GtTriggerMenu_L1Menu_Collisions2011_v6_mc >& ${OUTFILE}

# hltGetConfiguration ${MENU} --full --offline --data --unprescale --l1-emulator --process TEST --output minimal >& ${OUTFILE}

# hltGetConfiguration ${MENU} --full --offline --mc --unprescale --process TEST --l1-emulator --l1 L1GtTriggerMenu_L1Menu_Collisions2011_v4_mc,sqlite_file:/uscmst1b_scratch/lpc1/lpctrig/apana/dev/L1FastJet/CMSSW_4_2_6/src/run/L1Menu/L1Menu_Collisions2011_v4_mc.db >& ${OUTFILE}

hltGetConfiguration /users/jjhollar/LensMenu/online_5e33_v21_V12/V2 --full --offline --data --process TEST --output minimal --unprescale >& hlt_5e33indx2_unpre.py