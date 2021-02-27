#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 22:19:48 2021

@author: ghassan
"""
from __future__ import absolute_import
import pickle
from sequence import Sequence
from burros_wheeler import BurrosWheeler
from huffman import HuffmanTree

class Encoder:
    
    def __init__(self: object, path: str) -> None:
        
        self.path = path[:-4]
        self.seq = Sequence(path)
        self.bwt= None
        self.bwt_output = self.path + '_bwt.txt'
        self.tree = None
        self.encoded_seq = None
        self.encoded_output = self.path + '_compressed.txt'
   
    def encode(self: object) -> None:
        
        all_rots = BurrosWheeler.string_rotations(self.seq.read())
        yield all_rots
        
        bwm = BurrosWheeler.construct_bwm(all_rots)
        yield bwm
        
        tf = BurrosWheeler.encode_bwt(bwm)
        yield tf
        
        self.bwt = tf
        self.seq.write(self.bwt_output, tf)
        
        tree = HuffmanTree(self.bwt)
        tree.get_codings(tree.root)
        binary = tree.seq_to_binstr()
        yield binary
        
        unicode = HuffmanTree.binstr_to_unicode(binary)
        yield unicode
        
        self.tree = tree
        self.encoded_seq = unicode
        
        compressed = tree.codes_to_header() + unicode

        self.seq.write(self.encoded_output, compressed)
        

yo = Encoder("../data/random.txt")

pb = yo.encode()
next(pb)

Sequence("../data/random_compressed.txt").read()


    

