#includes ----------------------------
import sys          #used for command line arguments
import os.path      #used for file i/o
import urlparse     #used for parsing unfo from result's urls
import pickle       #used to save objects to a file

#set global variables ----------------
dbg_opt = 0         #debug option, toggles all of the debuging outputs on       
out_opt = 0         #output option, determine where data will be output.
                    #either cmd line or txt file
srcfile = "src.txt" #stores the location of the text file used to store the
                    #sprecially formated web address of a
                    #source search results page
outpath = ""        #holds the location of the file that will hold output
outfile = ""        #specifies the name of the output file
inpath = ""         #hold the location of the file that will be used as input
infile = ""         #specifies the name of the output file
CLA = []            #a list of the command line arguments used as
                    #temporary storage for handling
file_test = ("", "")#a pair for testing if the output file was specified correctly

#Function Definitions ----------------
def prgm_exit(cause,x):
    print "The program has exited due to the following problem: "
    if (x == 0):
        print "The output file specified, " + cause \
        + ", is not a file, please specify a file nest time"        

#Command Line Arguments --------------
# dealing with syntax and the flags used
for arg in sys.argv:
    if arg == "-d":     #if -d is a Command Line Argument, turn on debug mode
        dbg_opt = 1
    CLA.append(arg)     #add each argument to the list CLA for
                        #syntax testing and handling

if dbg_opt == 1:        #indicate if debug mode is on
    print "Debug mode is enabled"

i = 0
f = (len(CLA) - 1)
while i < f:                    #loop through each flag and deal with syntax
    i = i + 1                   #next argument from CLI
    if CLA[i] ==  "-o":         #if flag '-o' us used,
        out_opt = 1             #set output location to Command Line Interface,
                                #unless a file is indicated afterwords
        temp = CLA[i+1]         #set the next argument to temp for testing
        if temp[0] != '-':      #if the next argument isn't a flag, set it to be
                                #the output file location
            if dbg_opt == 1:    #if debug mode is on, output the filepath
                print "This is the filepath:" + ' ' + CLA[i+1]
            outpath = CLA[i+1]  #setting the outpath from the CLA
            file_test = os.path.splitest(basename(outpath))
            if file_test[1] == '' or file_test[0] == '' :    #if the ext is missing, exit program
                prgm_exit(outpath, 0)  #exiting program
            else :
                outfile = basename(outpath)
            f = f - 1
            del CLA[i+1]

