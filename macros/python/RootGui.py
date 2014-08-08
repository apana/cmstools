import os, sys
import ROOT

# To run, do an "execfile( '<path-to>/demo.py' )" or "python <path-to>/demo.py"

# enable running from another directory than the one where demo.py resides
workdir = os.path.dirname( sys.argv[0] )
if workdir:
   os.chdir( workdir )
   
os.environ["FROMGUI"] = "1"

ROOT.gROOT.Reset()
# ROOT.gStyle.SetScreenFactor(1.2)   # if you have a large screen, select 1.2 or 1.4
ROOT.gROOT.ProcessLine(".x ~/rootmacros/myStyle.cc");
# ROOT.gROOT.ProcessLine(".x ~/rootmacros/setTDRStyle.C");
ROOT.gROOT.SetStyle("MyStyle");

bar = ROOT.TControlBar( 'vertical', 'RootGui', 10, 10 )

newName="xxx"
newFile="xxx.py"

# The callbacks to python work by having CINT call the python interpreter through
# the "TPython" class. Note the use of "raw strings."
# bar.AddButton( 'Help on Demos', r'TPython::Exec( "execfile( \'demoshelp.py\' )" );', 'Click Here For Help on Running the Demos' )
bar.AddButton( 'Quit', r'TPython::Exec( "sys.exit()" );', 'Quit Button' )
bar.AddButton( '    browser    ', r'TPython::Exec( "b = ROOT.TBrowser()" );', 'Start the ROOT browser' )
bar.AddButton( 'TriggerRates', r'TPython::Exec( "execfile( \'TriggerRates.py\' )" );', 'xxxx' )
bar.AddButton( 'DivideHsts', r'TPython::Exec( "execfile( \'DivideHsts.py\' )" );', 'xxxx' )
bar.AddButton( 'CompHsts', r'TPython::Exec( "execfile( \'CompHsts.py\' )" );', 'xxxx' )
bar.AddButton( newName,  r'TPython::Exec( "execfile( \'' +newFile+ '\' )" );', 'xxxx' )

bar.Show()

ROOT.gROOT.SaveContext()


## wait for input to keep the GUI (which lives on a ROOT event dispatcher) alive
if __name__ == '__main__':
   rep = ''
   while not rep in [ 'q', 'Q' ]:
      rep = raw_input( 'enter "q" to quit: ' )
      if 1 < len(rep):
         rep = rep[0]
