# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:09:30 2021

@author: KugelBlitZZZ
"""
import filemanager as fm
from typing import List, Tuple

file = fm.FileManager("../data/test_seq.txt")
seq = file.read()

"""second"""

def suffix_array(sequence: str) -> List[Tuple[str, int]]:
    
    sequence += '$'
    return sorted([(sequence[c:], c) for c in range(len(sequence))])

def bwt_transform(sequence: str) -> str:
   
    bwt = []
    for suff in suffix_array(sequence):
        i = suff[1] # The suffix's index is the 2nd element in the tuple
        if i == 0:
            bwt.append('$')
        else:
            bwt.append(sequence[i - 1])
    return ''.join(bwt)

def rankBwt(bw):
    ''' Given BWT string bw, return parallel list of B-ranks.  Also
        returns tots: map from character to # times it appears. '''
    tots = dict()
    ranks = []
    for c in bw:
        if c not in tots:
            tots[c] = 0
        ranks.append(tots[c])
        tots[c] += 1
    return ranks, tots

def firstCol(tots):
    ''' Return map from character to the range of rows prefixed by
        the character. '''
    first = {}
    totc = 0
    for c, count in sorted(tots.items()):
        first[c] = (totc, totc + count)
        totc += count
    return first

def reverseBwt(bw):
    ''' Make T from BWT(T) '''
    ranks, tots = rankBwt(bw)
    first = firstCol(tots)
    rowi = 0 # start in first row
    t = '$' # start with rightmost character
    while bw[rowi] != '$':
        c = bw[rowi]
        t = c + t # prepend to answer
        # jump to row that starts with c of same rank
        rowi = first[c][0] + ranks[rowi]
    return t

yo = bwt_transform(seq)

reverseBwt(yo)
seq
"""first
rot = seq *2
yo = sorted(rot[i:i+len(seq)] for i in range(len(seq)))

seq
''.join([y[-1] for y in yo])
"""