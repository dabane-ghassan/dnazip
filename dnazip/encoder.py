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

class BWEncoder:

    def __init__(self: object, path: str) -> None:

        self.path = path[:-4]
        self.seq = Sequence(path)
        self.bwt_output = self.path + '_bwt.txt'
        self.rotations = None
        self.bwm = None
        self.bwt = None

    def encode(self: object) -> None:
        
        self.rotations = BurrosWheeler.string_rotations(self.seq.read())
        self.bwm = BurrosWheeler.construct_bwm(self.rotations)
        self.bwt = BurrosWheeler.encode_bwt(self.bwm)
        Sequence(self.bwt_output).write(self.bwt)

class HuffEncoder:
    
    def __init__(self: object, path: str) -> None:

        self.path = path[:-4]
        self.seq = Sequence(path)
        self.huff_output = self.path + '_compressed.txt'
        self.binary = None
        self.compressed = None

    def encode(self: object) -> None:

        tree = HuffmanTree(self.seq.read())
        tree.get_codings(tree.root)
        self.binary = tree.seq_to_binstr()
        unicode = HuffmanTree.binstr_to_unicode(self.binary)
        header = tree.codes_to_header()
        self.compressed =  header + unicode
        Sequence(self.huff_output).write_bytes(self.compressed)

class FullEncoder:

    def __init__(self: object, path: str) -> None:

        self.path = path
        self.bw_encoder = None
        self.huff_encoder = None

    def full_zip(self: object) -> None:

        self.bw_encoder = BWEncoder(self.path)
        self.bw_encoder.encode()
        
        self.huff_encoder = HuffEncoder(self.bw_encoder.bwt_output)
        self.huff_encoder.encode()
