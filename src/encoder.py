#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 22:19:48 2021

@author: ghassan
"""
from __future__ import absolute_import
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

        self.seq.write_bytes(self.encoded_output, compressed)
        

pfft = Encoder("../data/random.txt")

ts = pfft.encode()

next(ts)

############################################
class Decoder:
    pass

seq = Sequence("../data/random_compressed.txt").read_bytes()

header = seq[:seq.index('\n')]
uni = seq[seq.index('\n')+1:]
re_codes = HuffmanTree.header_to_codes(header)
binary = HuffmanTree.unicode_to_binstr(uni)
padding = int(re_codes['pad'])
no_pad_bin = HuffmanTree.remove_padding(binary, padding)

tf = HuffmanTree.binstr_to_seq(no_pad_bin, re_codes)
bwm = BurrosWheeler.reconstruct_bwm(tf)
original_seq = BurrosWheeler.decode_bwt(bwm)


Sequence("../data/random.txt").read()


