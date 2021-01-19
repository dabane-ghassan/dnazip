# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:09:30 2021

@author: KugelBlitZZZ
"""
import filemanager as fm
import numpy as np

file = fm.FileManager("../data/test_seq.txt")
seq = file.read()

rot = seq *2
yo = sorted(rot[i:i+len(seq)] for i in range(len(seq)))

seq 
''.join([y[-1] for y in yo])


t = sorted([(seq[i:], i) for i in range(len(seq))])
t

bw = []
for si in map(lambda x: x[1], t):
    if si == 0:
        bw.append('$')
    else:
        bw.append(seq[si-1])
        
''.join(bw)


"""
def suffixArray(s):
    satups = sorted([(s[i:], i) for i in range(len(s))])
    return map(lambda x: x[1], satups)

def bwtViaSa(t):
    # Given T, returns BWT(T) by way of the suffix array
    bw = []
    for si in suffixArray(t):
        if si == 0:
            bw.append('$')
        else:
            bw.append(t[si-1])
    return ''.join(bw) # return string-ized version of list bw
"""