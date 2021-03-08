#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Encoder classes, Controller architecture.

@author: Ghassan Dabane
"""
from __future__ import absolute_import
import os
from sequence import Sequence
from burros_wheeler import BurrosWheeler
from huffman import HuffmanTree

class BWEncoder:

    def __init__(self: object, path: str) -> None:

        self.path = os.path.splitext(path)[0]
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

        self.path = os.path.splitext(path)[0]
        self.seq = Sequence(path)
        self.huff_output = self.path + '_compressed.txt'
        self.binary = None
        self.header = None
        self.unicode = None
        self.compressed = None

    def encode(self: object) -> None:

        tree = HuffmanTree(self.seq.read())
        tree.get_codings(tree.root)
        self.binary = tree.seq_to_binstr()
        self.unicode = HuffmanTree.binstr_to_unicode(self.binary)
        self.header = tree.codes_to_header()
        self.compressed =  self.header + self.unicode
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
