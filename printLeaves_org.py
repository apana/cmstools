import sys,string,os.path

EXEC="root -b -q -l -n"
# EXEC="root"

mymacro="printLeaves.cc"
def usage():
    """ Usage: printLeaves <rootFile> <treeName>
    
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
        
    rootfile=sys.argv[1]
    rootTree="myTree"
    if narg == 3:
        rootTree=sys.argv[2]
    
    Command="\'" + rootmacro + "(\"" + rootfile + "\"," +\
                 "\"" + rootTree + "\"" +\
                 ")\'"
    
    myargs = string.join([EXEC,Command])
    # print "Command arguments: ",myargs
    os.system(myargs)

    
