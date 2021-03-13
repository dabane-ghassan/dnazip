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
    """An encoder class for Burros-Wheeler transform, it is used as a 
    controller in a MVC architecture.

    Attributes
    ----------
    path: str
        The path of the file to be transformed with Burros-Wheeler.
    seq: Sequence
        The sequence that was extracted from the file; a Sequence object.
    bwt_output: str
        The output file path for BWT.
    rotations: List[str]
        A matrix of rotations from the original sequence.
    bwm: List[str]
        The Burros-Wheeler Matrix.
    bwt: str
        The Burros-Wheeler transform of the sequence.
    """
    def __init__(self: object, path: str) -> None:
        """Class constructor.

        Parameters
        ----------
        path : str
            The path of the file to be read.

        Returns
        -------
        None
            A class instance.

        """
        self.path = os.path.splitext(path)[0]
        self.seq = Sequence(path)
        self.bwt_output = self.path + '_bwt.txt'
        self.rotations = None
        self.bwm = None
        self.bwt = None

    def encode(self: object) -> None:
        """The main encoding method of the controller.

        Returns
        -------
        None
            Fills all the properties of an object and writes out the
            transformed sequence to a file.

        """
        self.rotations = list(BurrosWheeler.string_rotations(self.seq.read()))
        self.bwm = BurrosWheeler.construct_bwm(self.rotations[-1])
        self.bwt = BurrosWheeler.encode_bwt(self.bwm)
        Sequence(self.bwt_output).write(self.bwt)

class HuffEncoder:
    """An encoder class for Huffman compression, it is used as a controller
    in a MVC architecture.
    
    Attributes
    ----------
    path: str
        The path of the file to be compressed with Huffman compression.
    seq: Sequence
        The sequence that was extracted from the file; a Sequence object.
    huff_output: str
        The output file path for Huffman compression.
    binary: str
        The binary sequence that was translated from the original sequence 
        using Huffman tree and codes.
    header: str
        The header of the compressed file; contains Huffman codes and paths
        as well as padding that were generated when compressing the sequence.
    unicode: str
        The compressed format of the sequence.
    compressed: str
        The compressed sequence to be written to a file.
    """

    def __init__(self: object, path: str) -> None:
        """Class constructor.

        Parameters
        ----------
        path : str
            The path of the file to be read.

        Returns
        -------
        None
            A class instance.

        """
        self.path = os.path.splitext(path)[0]
        self.seq = Sequence(path)
        self.huff_output = self.path + '_compressed.txt'
        self.binary = None
        self.header = None
        self.unicode = None
        self.compressed = None

    def encode(self: object) -> None:
        """The main encoding method of the controller.

        Returns
        -------
        None
            Fills all the properties of an object and writes out the
            compressed sequence to a file.

        """
        tree = HuffmanTree(self.seq.read())
        tree.get_codings(tree.root)
        self.binary = tree.seq_to_binstr()
        self.unicode = HuffmanTree.binstr_to_unicode(self.binary)
        self.header = tree.codes_to_header()
        self.compressed =  self.header + self.unicode
        Sequence(self.huff_output).write_bytes(self.compressed)

class FullEncoder:
    """An encoder class for both the Burros-Wheeler transform and Huffman
    compression, controller architecture.
    
    Attributes
    ----------
    path: str
        The path of the file to be compressed with BWT + Huffman compression.
    bw_encoder: BWEncoder
        A BWEncoder object to do the Burros-Wheeler transform on a sequence.
    huff_encoder: HuffEncoder
        A HuffEncoder object to do the Huffman compression on the BW transform.
    """

    def __init__(self: object, path: str) -> None:
        """Class constructor.

        Parameters
        ----------
        path : str
            The path of the file to be read.

        Returns
        -------
        None
            A class instance.

        """
        self.path = path
        self.bw_encoder = None
        self.huff_encoder = None

    def full_zip(self: object) -> None:
        """The main encoding method of the controller, it first encodes the
        sequence with BWT, then passes the BWT to Huffman compression.

        Returns
        -------
        None
            Fills all the properties of an object and writes out the
            compressed sequence to a file.

        """
        self.bw_encoder = BWEncoder(self.path)
        self.bw_encoder.encode()
        
        self.huff_encoder = HuffEncoder(self.bw_encoder.bwt_output)
        self.huff_encoder.encode()
