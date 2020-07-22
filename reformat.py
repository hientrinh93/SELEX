#!/usr/bin/python
import sys
import getopt
def open_file(arg):                                         
    input_file=""                                          
    output_file=""
    #parsing command line (structure)
    try:
        a, b = getopt.getopt(arg,"h:i:",["input="]) 
    except getopt.GetoptError:                              
        print ("file_name.py <input_file>")
        sys.exit(2)                                         
    #input file
    for option,value in a:
        if option == "-h":
            print ("file_name.py <input_file> <output_file>")
            sys.exit()
        elif option in ("-i","--input"):
            input_file = value


if __name__ == "__main__":
    open_file(sys.argv[0:])
    f = open(sys.argv[1],"r")
    g = open(str(sys.argv[1])+".final.bed","w")
    read_name, pos1, pos2, pos3, pos5 = ([] for i in range(5))
    for line in f:
        col = line.split("\t")
        read_name.append(col[3][0:-2])
        pos1.append(col[0])
        pos2.append(col[1])
        pos3.append(col[2])
        pos5.append(col[4])
    i = 0
    for i in range(0,len(read_name),2):
        if read_name[i] == read_name[i+1]:
            if int(pos2[i]) > int(pos2[i+1]):
                g.write(pos1[i]+"\t"+pos2[i+1]+"\t"+pos3[i]+"\t"+read_name[i][0:-2]+"\t"+pos5[i]+"\t"+"+"+"\n")
            else:
                g.write(pos1[i]+"\t"+pos2[i]+"\t"+pos3[i+1]+"\t"+read_name[i][0:-2]+"\t"+pos5[i]+"\t"+"+"+"\n")  
    f.close()
    g.close()
