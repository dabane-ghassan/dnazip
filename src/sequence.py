# -*- coding: utf-8 -*-
"""
A script to read and write DNA sequences (or a list of characters) to a file.

@author: Ghassan DABANE
"""

class Sequence:
    
    def __init__(self: object, path: str) -> None:
        self.path = path
        
    def __str__(self: object) -> str:
        return "Hey there! I'm a Sequence object"
    
    def __repr__(self: object) -> str:
        return "Sequence(%s)" % self.path
        
    def read(self: object) -> str:
        with open(self.path, 'r') as f:
            return f.readline()
        
    def write(self: object, out: str, content: str) -> None:
        with open(out, 'w') as f:
            f.writelines(content)
