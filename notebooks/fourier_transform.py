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
    num_stats = 1
    count = 0
    test = ipdft(result, dints)
    obs_stat = test.power()
    for period in range(len(obs_stat)):
        for rep in range(num_reps):
            sampled_indices = sampled_places(block_size, length)
            new_signal = signal.take(sampled_indices)
            tes = ipdft(new_signal,dints)
            sim_stat = tes.power()
            if num_stats > 1:
                count[(sim_stat[period]) >= (obs_stat[period])] += 1
            elif sim_stat[period] >= obs_stat[period]:
                count += 1
        return count / num_reps

#a = ipdft("ATGTATTGCTAAAAATAGCAATAAATAGCATAATTAAGCTTATTTATTTT","GC")
#developed for each period
