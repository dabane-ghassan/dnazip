#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 22:19:48 2021

@author: Ghassan Dabane
"""
from __future__ import absolute_import
from typing import Iterator, List
from sequence import Sequence
from burros_wheeler import BurrosWheeler
from huffman import HuffmanTree

class Encoder:

    def __init__(self: object, path: str) -> None:

        self.path = path[:-4]
        self.seq = Sequence(path)
        self.bwt_encode = Sequence(self.path + '_bwt.txt')
        self.huffman_encode = Sequence(self.path + '_compressed.txt')

    def encode_bw(self: object) -> Iterator[List[str]]:
        
        all_rots = BurrosWheeler.string_rotations(self.seq.read())

        
        bwm = BurrosWheeler.construct_bwm(all_rots)

        
        tf = BurrosWheeler.encode_bwt(bwm)
        self.bwt_encode.write(tf)


    def encode_huffman(self: object) -> Iterator[str]:

        tree = HuffmanTree(self.bwt_encode.read())
        tree.get_codings(tree.root)
        binary = tree.seq_to_binstr()


        unicode = HuffmanTree.binstr_to_unicode(binary)
        header = tree.codes_to_header()
        compressed =  header + unicode
        self.huffman_encode.write_bytes(compressed)

  
    def full_protocol(self: object) -> None:
        pass
