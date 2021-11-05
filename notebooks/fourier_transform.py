#!/usr/bin/python3

__author__ = "Hien Trinh"
__copyright__ = "Copyright 2020"
__license__ = "GPLv3"
__email__ = "hientrinh.hus@gmail.com"

#Citation
#***************************************************************************************
#*    Title: PyCogent source code
#*    Author: Hua Ying, Julien Epps and Gavin Huttley
#*    Date: 2007-2016
#*    Code version: 1.9
#*    Availability: http://www.pycogent.org
#***************************************************************************************

import numpy
from numpy import array, exp, pi, arange, float64
from random import choice
from decimal import Decimal
from Bio import SeqIO
from timeit import timeit


def seqtosymbols(seq, dints):
    length = len(seq)
    result = numpy.zeros(length, numpy.uint8) #create arrays array([1, 0], dtype=uint8)         
    for i in range(0,length-1):
        if seq[i:i+2] in dints:
            result[i] = 1
    return result

class ipdft(object):
    def __init__(self, result, dints):
        #self.seq = seq
        self.length = len(result)
        self.result = result
        self.dints = dints
        #self.result = numpy.zeros(self.length, numpy.uint8) #create arrays array([1, 0], dtype=uint8)         
        #for i in range(0,self.length-1):
            #if self.seq[i:i+2] in self.dints:
                #self.result[i] = 1
            #else:
                #break
        self.llim = 2
        self.ulim = self.length - 1
        self.periods = array(range(self.llim, self.ulim + 1))
        
    def ipdft_inner(self, X, W, ulim, N):
        for p in range(ulim):
            w = 1
            for n in range(N):
                if n != 0:
                    w *= W[p]
                X[p] = X[p] + self.result[n] * w
        return X

    def seqtosymbols(self):
        return self.result
    
    def period(self):
        return self.periods

    def power(self,period = None):
        self.W = exp(-1j*2*pi/arange(1, self.ulim + 1))
        self.X = array([0 + 0j]*self.length)
        self.X = self.ipdft_inner(self.X, self.W, self.ulim, self.length)
        power = abs(self.X[self.llim-1:self.ulim])
        return power       
        if period is not None:
            return '%.5E' % Decimal(power[period-2])

def circular_indices(vector, start, length, num):
    if start > length:
        start = start-length
        
    if start+num < length:
        return vector[start: start+num]
    return vector[start:] + vector[:start+num-length]

def sampled_places(block_size, length):
    """returns randomly sampled positions with block_size to make a new vector
    with length
    """
    num_seg, remainder = divmod(length, block_size)
    vector = list(range(length))
    result = []
    for seg_num in list(range(num_seg)):
        i = choice(vector)
        result += circular_indices(vector, i, length, block_size)
    
    if remainder:
        result += circular_indices(vector, i+block_size, length, remainder)
    return result

def blockwise_bootstrap(seq, dints, block_size, num_reps):
    length = len(seq)
    result = seqtosymbols(seq, dints)
    signal = numpy.array(list(result))    
    obs_stat = ipdft(result, dints).power()
    p_value = numpy.array([], dtype=float64)
    for period in range(len(obs_stat)):
        count = 0
        for rep in range(num_reps):
            sampled_indices = sampled_places(block_size, length)
            new_signal = signal.take(sampled_indices)
            sim_stat = ipdft(new_signal,dints).power()
            if sim_stat[period] >= obs_stat[period]:
                count += 1
        p_value= numpy.append(p_value,count / num_reps)
    return p_value

if __name__ == "__main__":    
    import matplotlib.pyplot as plt
    import numpy as np
    from itertools import combinations as ic
    from Bio import SeqIO
    import os
    #sequence
    seq = "ATGTATTGCTAAAAATAGCAATAAATAGCATAATTAAGCTTATTTATTTT"

  
    #dints
    dints_list = [['AC','AG','CA','CG','CT','GT','TC','TG'],['AA','TT','AT','TA'],['CC','GG','CG','GC']]
    dints_comb = []
    index = 0
    while index <= 1:
        if index != 1:
            for subset in ic(dints_list[index], 1):
                dints_comb.append(list(subset))
        index += 1 
        for L in range(1,5):
            for subset in ic(dints_list[index], L):
                dints_comb.append(list(subset))
    fasta_sequences = SeqIO.parse(open("enriched_seq.fa"),'fasta')

    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)
        print(sequence)
        filename = "/Users/hien/OneDrive - National University of Ireland, Galway/Documents/indu/fourier_transform/"+str(name)+"_FT"
        os.mkdir(filename)
        
        for subset in dints_comb:
        #convert sequence into symbols
            a = seqtosymbols(str(sequence),subset)
        
        #get periods, powers, P_value with block_size 15 and num_reps 1000
            b = ipdft(a,subset)
            periods = b.period()
            powers = b.power()
            p_value = blockwise_bootstrap(str(sequence),subset,15,2)

        #plots
            plt.plot(periods[0:49],powers[0:49],linewidth = 2)
            plt.plot(periods[0:49],p_value[0:49],linewidth = 2)
            plt.title("ipdft "+str(subset))
            plt.title(str(subset),fontsize = 18)
            plt.yticks(np.arange(0,16, step=1))
            plt.xticks(np.arange(0,51, step=5))
            plt.xlabel('period', fontsize = 14)
            plt.tick_params(labelsize = 14)
            plt.legend(['signal power','p-value'],prop={'size': 12},loc=1, borderaxespad=0)
            plt.grid()
            my_path = os.path.abspath(filename)
            plt.savefig(my_path+"/EMG{0}.png".format(subset))
            plt.close()
