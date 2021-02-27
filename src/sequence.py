# -*- coding: utf-8 -*-
"""
A script to read and write DNA sequences (or a list of characters) to a file.

@author: Ghassan DABANE
"""
from __future__ import absolute_import
import random

class Sequence:
    
    def __init__(self: object, path: str) -> None:
        self.path = path
        
    def __str__(self: object) -> str:
        return "Hey there! I'm a Sequence object"
    
    def __repr__(self: object) -> str:
        return "Sequence(%s)" % self.path
        
    def read(self: object) -> str:
        seq = ""
        with open(self.path, 'r') as f:
            for line in f:
                seq += line     
        return seq
        
    def write(self: object, out: str, content: str) -> None:
        with open(out, 'w') as f:
            f.writelines(content)

class RandomSequence(Sequence):
    
    def __init__(self, path, length):
        super().__init__(path)
        self.length = length
        
    def generate(self):
        seq = ''.join([random.choice('ATCGN') for _ in range(self.length)])
        self.write(self.path, seq)
