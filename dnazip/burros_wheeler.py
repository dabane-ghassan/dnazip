# -*- coding: utf-8 -*-
"""
Burrows-Wheeler Algorithm Class, contains naive and advanced construction
methods, static methods were written as explicit as possible and were
factorized to facilitate algorithmic readability.
The yielding in some functions doesn't respect Space complexity, but it was done in this
manner to facilitate the data flow into the View class (the GUI).
"""
from __future__ import absolute_import
from typing import List, Tuple

class BurrosWheeler:
    """A class to represent the Burrows-Wheeler algorithm, all methods are
    static for ease of reading and outside usability.
    """
    @staticmethod
    def pprint(mat: List[str]) -> None:
        """Pretty print, this method prints a burrows wheeler matrix
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

            rot = double_seq[i:i+len(seq)]
            all_rotations.append(rot)

            yield [rot for rot in all_rotations]

    @staticmethod
    def construct_bwm(rotations: List[str]) -> List[str]:
        """This method constructs the Burrows-Wheeler Matrix from a list of
        string rotations.

        Parameters
        ----------
        rotations : List[str]
            A list of strings, i.e; a BW matrix like object.

        Returns
        -------
        List[str]
            A list of strings or a Burrows-Wheeler Matrix.

        """

        sorted_rotations = sorted(rotations)
        return sorted_rotations

    @staticmethod
    def encode_bwt(matrix: List[str]) -> str:
        """Returns the Burrows-Wheeler Transform from a given Burros-Wheeler
        Matrix. the Burros-Wheeler Transform corresponds to the last column
        of the matrix.

        Parameters
        ----------
        matrix : List[str]
            A Burrows-Wheeler Matrix.

        Returns
        -------
        str
            The Burrows-Wheeler Transform.

        """

        last_column = []
        for line in matrix:
            last_char = line[-1]
            last_column.append(last_char)

        transformed_seq = ''.join(last_column)
        return transformed_seq

    @staticmethod
    def reconstruct_bwm(bwt: str) -> List[str]:
        """This method reconstructs the Burrows-Wheeler Matrix given the
        corresponding Burros-Wheeler Transform. The naive algorithm for
        constructing the matrix given the transform is going to iteratively
        add the transform as a left column, then sorts lexicographically
        the columns.

        Parameters
        ----------
        bwt : str
            The Burrows-Wheeler Transform.

        Returns
        -------
        List[str]
            A Burrows-Wheeler Matrix.

        """
        bwm = []
        # first loop to create seeds for lines O(n)
        for _ in range(0, len(bwt), 1):
            bwm.append('')

        for _ in range(0, len(bwt), 1):

            for i in range(0, len(bwt), 1):
                bwm[i] = bwt[i] + bwm[i]
 
            yield [line for line in bwm]
            bwm.sort()
            yield [line for line in bwm]

    @staticmethod
    def decode_bwt(matrix: List[str]) -> str:
        """This method returns the original sequence from a given
        Burrows-Wheeler Matrix, the original sequence is the line that ends
        with the character '$'.

        Parameters
        ----------
        matrix : List[str]
            A Burrows-Wheeler Matrix.

        Returns
        -------
        str
            The original sequence.

        """

        seq = ""
        for line in matrix: # search for the line that ends with '$'
            if line[-1] == "$":
                seq += line

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
        for i in range(0, len(sequence), 1):
            suff_arr.append((sequence[i:], i))

        return sorted(suff_arr)

    @staticmethod
    def bwt_advanced(sequence: str) -> str:
        """Generates a Burrows-Wheeler Transfrom from a suffix array, advanced
        construction of BWT. Better algorithmic complexity.

        Parameters
        ----------
        sequence : str
            The sequence to ve transformed.

        Returns
        -------
        str
            The Burrows-Wheeler Transform.

        """

        bwt = []
        for suff in BurrosWheeler.suffix_array(sequence):
            i = suff[1] # The suffix's index is the 2nd element in the tuple
            if i == 0:
                bwt.append('$')
            else:
                bwt.append(sequence[i - 1])

        return ''.join(bwt)
