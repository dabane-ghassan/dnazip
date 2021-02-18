# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:36:09 2021

@author: KugelBlitZZZ
"""
import os
os.chdir("/home/ghassan/M1/dnazip/src")
from typing import Dict
import filemanager as fm

class HuffmanNode:
    """A class to represent heap nodes of a huffman coding tree.

    Attributes
    ----------
    char: str
        The character to be saved as a node value.

    freq: int
        The frequency of the char.

    right_child: HuffmanNode
        The right child of the heap node.

    left_child: HuffmanNode
        The left child of the heap node.

    """
    def __init__(self: object, char: str, freq: int, left: object=None, right: object=None) -> None:
        """Class constructor.

        Parameters
        ----------
        char : str
            A character (Huffman coding characters).
        freq : int
            The frequency of the character.
            DESCRIPTION.

        Returns
        -------
        None

        """
        self.char = char
        self.freq = freq
        self.__left_child = left
        self.__right_child = right
        self.dir = ''

    @property
    def right_child(self: object) -> object:
        """The getter of the right child.

        Returns
        -------
        object

        """
        return self.__right_child

    @right_child.setter
    def right_child(self: object, right_child: object) -> None:
        """The setter of the right child.

        Parameters
        ----------
        right_child : object
            The new child.

        Returns
        -------
        None

        """
        self.__right_child = right_child

    @property
    def left_child(self: object) -> object:
        """The getter of the left child.

        Returns
        -------
        object

        """
        return self.__left_child

    @left_child.setter
    def left_child(self: object, left_child: object) -> None:
        """The setter of the left child.

        Parameters
        ----------
        right_child : object
            The new child.

        Returns
        -------
        None

        """
        
        self.__left_child = left_child
        
    def __str(self: object) -> str:
        """Returns a string representation using print().
        

        Returns
        -------
        str
            A string to be displayed with print().

        """
        return "Hello! I'm a Huffman coding HeapNode class instance."
    
    def __repr__(self: object) -> str:
        """A coder friendly representation of the HuffmanNode object.
        
        Returns
        -------
        str
            A string.

        """
        return "Node(%s, freq=%s, right=%s, left=%s)"%(self.char,
                                                       self.freq, 
                                                       self.right_child,
                                                       self.left_child)

    def __eq__(self: object, other_node: object) -> bool:
        """Checks if two nodes has the same frequency.

        Parameters
        ----------
        other_node : object
            The other node.

        Returns
        -------
        bool

        """
        return self.freq == other_node.freq

    def __lt__(self: object, other_node: object) -> bool:
        """Checks if the node has a frequency less than a second node.

        Parameters
        ----------
        other_node : object
            The other node.

        Returns
        -------
        bool

        """
        return self.freq < other_node.freq

    def __le__(self: object, other_node: object) -> bool:
        """Checks if the node has a frequency less or equal than a second node.

        Parameters
        ----------
        other_node : object
            The other node.

        Returns
        -------
        bool

        """
        return self.freq <= other_node.freq

    def __gt__(self: object, other_node: object) -> bool:
        """Checks if the node has a frequency greater than a second node.

        Parameters
        ----------
        other_node : object
            The other node.

        Returns
        -------
        bool

        """
        return self.freq > other_node.freq

    def __ge__(self: object, other_node: object) -> bool:
        """Checks if the node has a frequence greater or equal than a 
        second node.

        Parameters
        ----------
        other_node : object
            The other node.

        Returns
        -------
        bool

        """
        return self.freq >= other_node.freq

class HuffmanTree:

    def __init__(self: object, sequence: str) -> None:
        
        self.sequence = sequence
        self.frequency = HuffmanTree.freq_dict(self.sequence)
        self.root = self.create_tree()
        self.codes = {}
        self.reverse_map = {}

    @staticmethod
    def freq_dict(sequence: str) -> Dict[str, int]:

        f_dict = {}
        for c in sequence: 
            if c in f_dict.keys():
                f_dict[c] += 1
            else:
                f_dict[c] = 1
        return f_dict
    
    def create_tree(self: object) -> None:
        
        leafs = []
        for char, freq in self.frequency.items():
            leafs.append(HuffmanNode(char, freq))

        while len(leafs) > 1:
            leafs = sorted(leafs, key=lambda x: x.freq)
            
            left = leafs.pop(0)
            right = leafs.pop(0)
            
            new_char = left.char + right.char
            new_freq = left.freq + right.freq
            
            left.dir = "0"
            right.dir = "1"

            new_node = HuffmanNode(new_char, new_freq, left, right)
            leafs.append(new_node)  
            
        return leafs[0]
        
    def get_codings(self: object, node: HuffmanNode, val: str='') -> None:

        curr_path = val + node.dir

        if node.left_child:
            self.get_codings(node.left_child, curr_path)
        if node.right_child:
            self.get_codings(node.right_child, curr_path)

        if not node.left_child and not node.right_child:
            self.codes[node.char] = curr_path
            
    def seq_to_bin_str(self: object) -> None:
        
        bin_str = ""
        for char in self.sequence:
            bin_str += self.codes[char]
        return bin_str

file = fm.FileManager("../data/test_seq_bwt.txt")
seq = file.read()

pfft = HuffmanTree(seq)
pfft.root
pfft.get_codings(pfft.root)
#bin(int(something, 2))
pfft.codes
len(seq)
8 - len(pfft.seq_to_bin_str()) % 8
"{0:08b}".format(2)
