#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 22:19:48 2021

@author: Ghassan Dabane
"""
from __future__ import absolute_import
from sequence import Sequence
from burros_wheeler import BurrosWheeler
from huffman import HuffmanTree

class Encoder:
    
    def __init__(self: object, path: str) -> None:
        
        self.path = path[:-4]
        self.seq = Sequence(path)
        self.bwt_output = self.path + '_bwt.txt'
        self.encoded_output = self.path + '_compressed.txt'
   
    def encode_bw(self: object) -> None:
        
        all_rots = BurrosWheeler.string_rotations(self.seq.read())
        yield all_rots
        
        bwm = BurrosWheeler.construct_bwm(all_rots)
        yield bwm
        
        tf = BurrosWheeler.encode_bwt(bwm)
        self.seq.write(self.bwt_output, tf)
        yield tf
        
    def encode_huffman(self: object) -> None:

        tree = HuffmanTree(self.bwt)
        tree.get_codings(tree.root)
        binary = tree.seq_to_binstr()
        yield binary

        unicode = HuffmanTree.binstr_to_unicode(binary)
        header = tree.codes_to_header()
        compressed =  header + unicode
        self.seq.write_bytes(self.encoded_output, compressed)
        yield unicode
        

pfft = Encoder("../data/random.txt")

ts = pfft.encode()

next(ts)
