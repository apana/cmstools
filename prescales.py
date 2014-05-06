
import urllib2
import sys
import FWCore.ParameterSet.Config as cms

def prettyPrint(prescales):
 length = 0
 for name in prescales:
     length = max(length,len(name))
 for name in sorted(prescales.iterkeys()):
   print name,(length-len(name))*" ", ":", prescales[name] 


##########################
if __name__ == "__main__":
 if len(sys.argv)!=2:
   print "usage: %s <trigger menu name>" %sys.argv[0]
   sys.exit(1)
 else:
   configName = sys.argv[1]
   pageurl = "http://cms-project-confdb-hltdev.web.cern.ch/cms-project-confdb-hltdev/get.jsp?dbName=ORCOFF&configName=%s&cff=&nooutput=&format=Python" %configName
   page = urllib2.urlopen(pageurl)
   content = page.read()
   if not content.startswith("# "):
     print "Couldn't retrieve prescales. Probably the trigger menu is not known."
     sys.exit(1)
   #translate config into python objects 
   tmp = {} 
   exec(content,tmp)

   # get the prescales
   prescales = {} 

   # first fill a default 1 for all paths in the menu
   for key, value in tmp.iteritems():
     if isinstance(value,cms.Path) and key != 'HLTriggerFinalPath':
       prescales[key] = 1

   for pset in tmp['PrescaleService'].prescaleTable:
       prescales[pset.pathName.value()] = pset.prescales[0]

   prettyPrint(prescales)
