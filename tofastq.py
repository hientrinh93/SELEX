#!/usr/bin/python
import sys
import getopt
def open_file(arg):                                         #defining function named "open_file" with variable "arg"
    input_file=""                                           #variables = string
    output_file=""
    #parsing command line (structure)
    try:
        a, b = getopt.getopt(arg,"h:i:o:",["input=","output="]) #getopt returns (option letters, value) pairs and arguments
    except getopt.GetoptError:                              #if not getting options, print a line below
        print ("file_name.py <input_file> <output_file>")
        sys.exit(2)                                         #exit from Python with Unix 
    #what is input and output file?
    for option,value in a:
        if option == "-h":
            print ("file_name.py <input_file> <output_file>")
            sys.exit()
        elif option in ("-i","--input"):
            input_file = value
        elif option in ("-o","--output"):
            output_file = value
if __name__ == "__main__":
    open_file(sys.argv[1:])
    f = open(sys.argv[1],"rtU")
    g = open(str(sys.argv[1])+".fq","w")
    ID = 0
    for line in f:
        first = line[0:1]
        col = line.split("\t")
        if (first == "#" or first == ">" or first == "\n" or len(col) != 3):
            continue
        else:
            ID = ID + 1
            g.write("@SEQ_"+str(ID)+"_"+str(col[1])+"\n"+col[1]+"\n"+"+"+"\n"+col[2])
    f.close()
    g.close()
