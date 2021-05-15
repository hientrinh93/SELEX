#!/bin/bash
echo "reformat"
awk '{print "F""\t" $0}' 2F_fragment_length > 2F_newformat
awk '{print "I""\t" $0}' 2I_fragment_length > 2I_newformat
awk '{print "L""\t" $0}' 2L_fragment_length > 2L_newformat

echo "merge_file"
cat 2*_newformat > 2FIL_boxplot_data
echo -e "sample\tfragment_length" | cat - 2FIL_boxplot_data > 2FIL_boxplot_header