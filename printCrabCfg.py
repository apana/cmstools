#!/usr/bin/env python

import imp
import FWCore.ParameterSet.Config as cms
from ProdCommon.CMSConfigTools.ConfigAPI.CfgInterface import CfgInterface

fileName="CMSSW.py"

handle = open(fileName, 'r')
try:   # Nested form for Python < 2.5
    try:
        print "Importing .py file"
        cfo = imp.load_source("pycfg", fileName, handle)
        cmsProcess = cfo.process
    except Exception, ex:
        msg = "Your pycfg file is not valid python: %s" % str(ex)
        raise ConfigException(msg)
finally:
    handle.close()
        
cfg = CfgInterface(cmsProcess)
print cmsProcess.dumpPython()
