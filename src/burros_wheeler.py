# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:09:30 2021

@author: KugelBlitZZZ
"""
from __future__ import absolute_import
from typing import List, Tuple

class BurrosWheeler(object):

    @staticmethod
    def pprint(mat: List[str]) -> None:
        """Pretty print, this method prints a burros wheeler matrix 
        beautifully (without lists and strings).

        Parameters
        ----------
        mat : List[str]
            The Burros-Wheeler matrix, i.e; a list of strings.

        Returns
        -------
        None
            Prints the matrix.
        """
        for line in mat:
            print(*line, sep="") # scatter operator to print all elements
                                 # of a line

    @staticmethod
    def string_rotations(seq: str) -> List[str]:
        """Returns all string rotations of a sequence.

        Parameters
        ----------
        seq : str
            he sequence to be rotated.

        Returns
        -------
        List[str]
            Returns a list of strings, i.e; a BW matrix like object.

        """

        seq += '$'
        double_seq = seq * 2
        all_rotations = []
        
        for i in range(0, len(seq), 1):
            all_rotations.append(double_seq[i:i+len(seq)])
            
        return all_rotations

    @staticmethod
    def construct_bwm(rotations: List[str]) -> List[str]:
        """This method constructs the Burros-Wheeler Matrix from a list of
        string rotations.
        

        Parameters
        ----------
        rotations : List[str]
            A list of strings, i.e; a BW matrix like object.

        Returns
        -------
        List[str]
            A list of strings or a Burros-Wheeler Matrix.

        """

        sorted_rotations = sorted(rotations)
        return sorted_rotations

    @staticmethod
    def encode_bwt(matrix: List[str]) -> str:
        """Returns the Burros-Wheeler Transform from a given Burros-Wheeler
        Matrix. the Burros-Wheeler Transform corresponds to the last column
        of the matrix.

        Parameters
        ----------
        matrix : List[str]
            A Burros-Wheeler Matrix.

        Returns
        -------
        str
            The Burros-Wheeler Transform.

        """

        last_column = []
        for l in matrix:
            last_char = l[-1]
            last_column.append(last_char)
        
        transformed_seq = ''.join(last_column)
        return transformed_seq

    @staticmethod
    def reconstruct_bwm(bwt: str) -> List[str]:
        """This method reconstructs the Burros-Wheeler Matrix given the
        corresponding Burros-Wheeler Transform. The naive algortihm for 
        constructing the matrix given the transform is going to iteratively 
        add the transform as a left column, then sorts lexicographically
        the columns.

        Parameters
        ----------
        bwt : str
            The Burros-Wheeler Transform.

        Returns
        -------
        List[str]
            A Burros-Wheeler Matrix.

        """

        bwm = []
        # first loop to create seeds for lines O(n)
        for l in range(0, len(bwt), 1): 
            bwm.append('')
    
        for n in range(0, len(bwt), 1):
            for i in range(0, len(bwt), 1):
                bwm[i] = bwt[i] + bwm[i]
            bwm.sort()

        return bwm

    @staticmethod    
    def decode_bwt(matrix: List[str]) -> str:
        """This method returns the original sequence from a given
        Burros-Wheeler Matrix, the original sequence is the line that ends 
        with the character '$'.

        Parameters
        ----------
        matrix : List[str]
            A Burros-Wheeler Matrix.

        Returns
        -------
        str
            The original sequence.

        """

        seq = ""
        for l in matrix: # search for the line that ends with '$'
            if l[-1] == "$":
                seq += l

        return seq[:-1] # return the sequence without the '$' sign
    
    @staticmethod
    def suffix_array(sequence: str) -> List[Tuple[str, int]]:
        """Builds a suffix-array from a given sequence of characters.
        - Complexity of the algorithm O(n^2log(n))
        - Sorting is O(nlogn) and Finding is O(n)

        Parameters
        ----------
        sequence : str
            The given sequence of characters.

        Returns
        -------
        List[Tuple[str, int]]
            The suffix array of the sequence; a list of tuples.

        """
 
        sequence += '$'
        suff_arr = []
        for c in range(0, len(sequence), 1):
            suff_arr.append((sequence[c:], c))

        return sorted(suff_arr)
    
    @staticmethod
    def bwt_advanced(sequence: str) -> str:
        """Generates a Burros-Wheeler Transfrom from a suffix array, advanced
        construction of BWT. Better algorithmic complexity.

        Parameters
        ----------
        sequence : str
            The sequence to ve transformed.

        Returns
        -------
        str
            The Burros-Wheeler Transform.

        """
    
        bwt = []
        for suff in BurrosWheeler.suffix_array(sequence):
            i = suff[1] # The suffix's index is the 2nd element in the tuple
            if i == 0:
                bwt.append('$')
            else:
                bwt.append(sequence[i - 1])

        return ''.join(bwt)

"""
TODO: ADVANCED REVERSE BWT

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

