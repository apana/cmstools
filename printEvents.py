import sys,string,os.path,glob

EXEC="root -b -q -l -n"
# EXEC="root"

mymacro="printEvents.cc"
def usage():
    """ Usage: printEvents <directory or filename> <treeName>
    
 Printout the leaves on <rootfile>
    """
    pass


if __name__ == '__main__':

    narg=len(sys.argv)
    if narg < 2 :
        print usage.__doc__
        sys.exit(1)

    rootpath=os.path.join(os.environ['HOME'],"rootmacros")
    rootmacro=os.path.join(rootpath,mymacro)
        
    rootdir=sys.argv[1]
    rootTree="HltTree"
    if narg == 3:
        rootTree=sys.argv[2]

    if (os.path.isdir(rootdir)):
        os.chdir(rootdir)
        #filelist=os.listdir(".")
        filelist=glob.glob("./*.root")
    else:
        filelist=[rootdir]
    
    print filelist

    for rootfile in filelist:

        
        Command="\'" + rootmacro + "(\"" + rootfile + "\"," +\
                 "\"" + rootTree + "\"" +\
                 ")\'"
    
        myargs = string.join([EXEC,Command])
        # print "Command arguments: ",myargs
        os.system(myargs)

    
