# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:36:09 2021

@author: KugelBlitZZZ
"""
import os
os.chdir("C:/Users/33750/Documents/GitHub/dnazip/src")
from typing import Dict
import filemanager as fm

class HeapNode:
    """A class to represent heap nodes of a huffman coding tree.
    
    Attributes
    ----------
    char: str
        The character to be saved as a node value.

    freq: int
        The frequency of the char.

    right_child: HeapNode
        The right child of the heap node.

    left_child: HeapNode
        The left child of the heap node.

    """
    
    def __init__(self: object, char: str, freq: int) -> None:
        self.char = char
        self.freq = freq
        self.right_child = None
        self.left_child = None
        
    
    def __repr__(self: object) -> str:
        return "HeapNode(%s, freq=%d, right=%s, left=%s)" %(self.char, 
                                                            self.freq, 
                                                            self.right_child,
                                                            self.left_child)

class Huffman:

    def __init__(self: object) -> None:
        pass

    @staticmethod
    def freq_dict(sequence: str) -> Dict[str, int]:

        f_dict = {}
        for c in sequence: 
            if c in f_dict.keys():
                f_dict[c] += 1
            else:
                f_dict[c] = 1
        return f_dict

file = fm.FileManager("../data/test_seq_bwt.txt")
seq = file.read()
seq

Huffman.freq_dict(seq)