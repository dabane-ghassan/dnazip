# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:09:30 2021

@author: KugelBlitZZZ
"""
import filemanager as fm
from typing import List

file = fm.FileManager("../data/test_seq.txt")
seq = file.read()

"""first
rot = seq *2
yo = sorted(rot[i:i+len(seq)] for i in range(len(seq)))

seq
''.join([y[-1] for y in yo])
"""

"""second"""

def suffix_array(sequence: str) -> List[tuple]:
    
    sequence += '$'
    return sorted([(sequence[c:], c) for c in range(len(sequence))])

def bwt_transform(sequence: str) -> str:
   
    bwt = []
    for suff in suffix_array(sequence):
        i = suff[1]
        if i == 0:
            bwt.append('$')
        else:
            bwt.append(sequence[i - 1])
    return ''.join(bwt)

