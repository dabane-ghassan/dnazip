# -*- coding: utf-8 -*-
"""
Huffman coding algorithm class, contains node and tree classes.

@author: Ghassan Dabane
"""
from typing import Dict

class HuffmanNode(object):
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
    dir: str
        The path of the current node in the Huffman tree, usually a string of
        0s and 1s.
    """
    def __init__(self: object, char: str, freq: int, left: object=None, right: object=None) -> None:
        """Class constructor

        Parameters
        ----------
        char : str
            A character (Huffman coding characters).
        freq : int
            The frequency of the character.
        left : object, optional
            The left child of the heap node. The default is None.
        right : object, optional
            The right child of the heap node. The default is None.

        Returns
        -------
        None
            A class instance.

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

    def __str__(self: object) -> str:
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

class HuffmanTree(object):
    """A class to represent a huffman tree.
    
    Attributes
    ----------
    sequence: str
        The sequence to be encoded, i.e; the Burros-Wheeler transform of the 
        sequence.
    frequency: Dict[str, int]
        A dictionary to store frequency values for each character of the
        sequence, the character as a key and its frequency as a value.
    root: HuffmanNode
        The root node of the Huffman tree.
    codes: Dict[str, str]
        The Huffman codes for a given sequence, The character as a key and
        its tree path as a value(a string).
    pad: int
        The padding of the sequence, i.e; the number of zeroes that was added
        to the end of sequence until it was divisible by 8 (coding in 8 bits).
    """
    def __init__(self: object, sequence: str) -> None:
        """The class constructor.

        Parameters
        ----------
        sequence : str
            The sequence to be coded.

        Returns
        -------
        None
            A class instance.

        """
        self.sequence = sequence
        self.frequency = HuffmanTree.freq_dict(self.sequence)
        self.root = self.create_tree()
        self.codes = {}

    @staticmethod
    def freq_dict(sequence: str) -> Dict[str, int]:
        """This method returns the frequence dictionary of a given sequence.

        Parameters
        ----------
        sequence : str
            The sequence of interest.

        Returns
        -------
        Dict[str, int]
            A dictionary of character frequencies.

        """

        f_dict = {}
        for c in sequence: 
            if c in f_dict.keys():
                f_dict[c] += 1
            else:
                f_dict[c] = 1
        return f_dict

    def create_tree(self: object) -> HuffmanNode:
        

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
    
    def seq_to_binstr(self: object) -> str:

        bin_str = ""
        for char in self.sequence:
            bin_str += self.codes[char]

        pad = 8 - len(bin_str) % 8
        if pad != 0:
            for p in range(0, pad, 1):
                bin_str += '0'
                
        self.codes['pad'] = str(pad) #Save the padding value to codes

        return bin_str

    @staticmethod
    def binstr_to_unicode(bin_str: str) -> str:

        unicode = ""
        for b in range(0, len(bin_str), 8):
            eight_bits = bin_str[b:b+8]
            code = int(eight_bits, 2)
            unicode += chr(code)

        return unicode

    @staticmethod
    def unicode_to_binstr(unicode: str) -> str:

        bin_str = ""
        for u in unicode:
            code = ord(u)
            bin_str += '{:08b}'.format(code)

        return bin_str

    @staticmethod
    def remove_padding(bin_str: str, pad: int) -> str:

        return bin_str[:-pad]
    
    @staticmethod
    def binstr_to_seq(bin_str: str, codes: Dict[str, str]) -> str:

        original_seq = ""
        reading_stream = ""
        for n in bin_str:
            reading_stream += n
            for char, path in codes.items():
                if path == reading_stream:
                    original_seq += char
                    reading_stream = ""
                    break

        return original_seq

    def codes_to_header(self: object) -> str:

        header = ""
        for c, p in self.codes.items():
            header += c + "," + p + ";"
            
        return header + "\n"
    
    @staticmethod
    def header_to_codes(header: str) -> Dict[str, str]:
        
        reconstructed_codes = {}
        for code in header.split(";")[:-1]:
            c, p = code.split(",")
            reconstructed_codes[c] = p
        return reconstructed_codes
