#!/usr/bin/python
import getopt
import sys
from Bio import SeqIO
col2 = []
input_file1=""
input_file2=""
output_file=""
#parsing command line (structure)
try:
    a, b = getopt.getopt(sys.argv[1:],"hf:c:o:",["input1=","input2=","output="]) #getopt returns (option letters, value) pairs and arguments
except getopt.GetoptError:                              #if not getting options, print a line below
    print("extract_enrich.py -f <input1> -c <input2> -o <output>\n")
    print("-f, --input1: sample_hs.mapQ25.ex.fastaptamer_count.fa\n")
    print("-c, --input2: sample_hs.mapQ25.ex.fastaptamer_count.line_fit.csv\n")
    print("-o, --output: cut-off_sequences.fa")
    sys.exit(2)                                         #exit from Python with Unix 
for option,value in a:
    if option == "-h":
        print ("file_name.py <input1> <input2> <output>\n")
        print ("<input1>: sample_hs.mapQ25.ex.fastaptamer_count.fa\n")
        print ("<input2>: sample_hs.mapQ25.ex.fastaptamer_count.line_fit.csv\n")
        print ("<output>: cut-off_sequences.fa (default)")
        sys.exit(2)
    elif option in ("-f","--input1"):
        input_file1 = value
    elif option in ("-c","--input2"):
        input_file2 = value
    elif option in ("-o","--output"):
        output_file = value

f = open(input_file1,"r")
g = open(input_file2,"r")   
h = open(output_file,"w")
for line in g:
    col2.append(line.split(",")[1])
copy_number = int(col2[-1])
for sequence in SeqIO.parse(f,"fasta"):
    a = int(sequence.id.split("-")[1])
    if a > copy_number:
        h.write (str(">"+sequence.id+"\n"+sequence.seq+"\n"))
f.close()
g.close()
h.close()
