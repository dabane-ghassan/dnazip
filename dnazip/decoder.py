#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 09:38:14 2021

@author: Ghassan Dabane
"""
from __future__ import absolute_import
from sequence import Sequence
from burros_wheeler import BurrosWheeler
from huffman import HuffmanTree

class HuffDecoder:

    def __init__(self: object, path: str) -> None:

        self.path = path[:-4]
        self.seq = Sequence(path)
        self.dehuffman_output = self.path + '_dehuff.txt'
        self.binary = None
        self.decompressed = None

    def decode(self: object) -> None:

        seq = self.seq.read_bytes()
        header = seq[:seq.index('\n')]
        uni = seq[seq.index('\n')+1:]
        re_codes = HuffmanTree.header_to_codes(header)
        binary = HuffmanTree.unicode_to_binstr(uni)
        padding = int(re_codes['pad'])
        self.binary = HuffmanTree.remove_padding(binary, padding)
        self.decompressed = HuffmanTree.binstr_to_seq(self.binary, re_codes)
        Sequence(self.dehuffman_output).write(self.decompressed)

class BWDecoder:
    
    def __init__(self: object, path: str) -> None:
        
        self.path = path[:-4]
        self.seq = Sequence(path)
        self.debwt_output = self.path + '_debwt.txt'
        self.bwm = None
        self.original = None
        
    def decode(self: object) -> None:

        self.bwm = BurrosWheeler.reconstruct_bwm(self.seq.read())
        self.original = BurrosWheeler.decode_bwt(self.bwm)
        Sequence(self.debwt_output).write(self.original)

class FullDecoder:

    def __init__(self: object, path: str) -> None:
        
        self.path = path
        self.huff_decoder = None
        self.bw_decoder = None
        
    def full_unzip(self: object) -> None:

        self.huff_decoder = HuffDecoder(self.path)
        self.huff_decoder.decode()

        self.bw_decoder = BWDecoder(self.huff_decoder.dehuffman_output)
        self.bw_decoder.decode()
