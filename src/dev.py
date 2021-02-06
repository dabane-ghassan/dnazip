# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:09:30 2021

@author: KugelBlitZZZ
"""
import filemanager as fm
from typing import List

file = fm.FileManager("../data/test_seq.txt")
seq = file.read()



def string_rotations(seq: str) -> List[str]:
  
    seq += '$'
    double_seq = seq * 2
    all_rotations = []
    
    for i in range(0, len(seq), 1):
        all_rotations.append(double_seq[i:i+len(seq)])
        
    return all_rotations

def bw_matrix(rotations: List[str]) -> List[str]:

    sorted_rotations = sorted(rotations)
    return sorted_rotations

def bw_transform(matrix: List[str]) -> str:
    
    last_column = []
    for l in matrix:
        last_char = l[-1]
        last_column.append(last_char)
    
    transformed_seq = ''.join(last_column)
    return transformed_seq



seq
all_rots = string_rotations(seq)
all_rots
mat = bw_matrix(all_rots)
mat
t = bw_transform(mat)
t
ls = []
for i in range(len(t)):
    ls.append('')

for n in range(len(t)):
    for i in range(len(t)):
        ls[i] = t[i] + ls[i]
    ls.sort()
ls[4]
mat
seq


"""

################## suffix array to construct BWT
def suffix_array(sequence: str) -> List[Tuple[str, int]]:
    '''O(n^2log(n)) sort nlogn and finding is n,
    maybe multikey quicksort to get that O(n^2) or try something better x(
    '''

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
####################################################

############################# Reverse BWT using b ranks and lf mapping
def rankBwt(bw):
    '''Given BWT string bw, return parallel list of B-ranks.  Also
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
#################################################################
"""

