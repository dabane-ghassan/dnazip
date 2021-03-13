#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Decoder classes, Controller architecture.

@author: Ghassan Dabane
"""
from __future__ import absolute_import
import os
from sequence import Sequence
from burros_wheeler import BurrosWheeler
from huffman import HuffmanTree

class HuffDecoder:
    """A decoder class for Huffman decompression, it is used as a controller
    in a MVC architecture.
    
    Attributes
    ----------
    path: str
        The path of the file to be decompressed with Huffman decompression.
    seq: Sequence
        The sequence that was extracted from the file; a Sequence object.
    dehuffman_output: str
        The output file path for Huffman decompression.
    binary: str
        The binary sequence that was translated from unicode using Huffman
        codes.
    header: str
        The header of the compressed file; contains Huffman codes and paths
        as well as padding that were generated when compressing the sequence.
    unicode: str
        The compressed format of the sequence.
    decompressed: str
        The decompressed sequence; normally the Burros-Wheeler transform of an
        original sequence.
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
        self.dehuffman_output = self.path + '_dehuff.txt'
        self.binary = None
        self.header = None
        self.unicode = None
        self.decompressed = None

    def decode(self: object) -> None:
        """The main decoding method of the controller.

        Returns
        -------
        None
            Fills all the properties of an object and writes out the
            decompressed sequence to a file.

        """
        seq = self.seq.read_bytes()
        self.header = seq[:seq.index('\n')]
        self.unicode = seq[seq.index('\n')+1:]
        re_codes = HuffmanTree.header_to_codes(self.header)
        binary = HuffmanTree.unicode_to_binstr(self.unicode)
        padding = int(re_codes['pad'])
        self.binary = HuffmanTree.remove_padding(binary, padding)
        self.decompressed = HuffmanTree.binstr_to_seq(self.binary, re_codes)
        Sequence(self.dehuffman_output).write(self.decompressed)

class BWDecoder:
    """A decoder class for inversing the Burros-Wheeler transform, it is used 
    as a controller in a MVC architecture.
    
    Attributes
    ----------
    path: str
        The path of the file to be transformed with inverse of Burros-Wheeler.
    seq: Sequence
        The sequence that was extracted from the file; a Sequence object.
    debwt_output: str
        The output file path for the inverse of BWT.
    bwm: List[str]
        The reconstructed Burros-Wheeler Matrix.
    original: str
        The original sequence from the inverse BWT.
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
        self.debwt_output = self.path + '_debwt.txt'
        self.bwm = None
        self.original = None
        
    def decode(self: object) -> None:
        """The main decoding method of the controller.

        Returns
        -------
        None
            Fills all the properties of an object and writes out the original
            sequence to a file.

        """
        self.bwm = list(BurrosWheeler.reconstruct_bwm(self.seq.read()))
        self.original = BurrosWheeler.decode_bwt(self.bwm[-1])
        Sequence(self.debwt_output).write(self.original)

class FullDecoder:
    """A decoder class for both Huffman decompression and the inverse of the
    Burros-Wheeler transform, controller architecture.

    Attributes
    ----------
    path: str
        The path of the file to be compressed with BWT + Huffman compression.
    huff_decoder: HuffDecoder
        A HuffDecoder object to do the Huffman decompression on a compressed
        sequence.
    bw_decoder: BWDecoder
        A BWDecoder object to do the inverse of Burros-Wheeler transform on
        the output of Huffman decompression.
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
        self.huff_decoder = None
        self.bw_decoder = None
        
    def full_unzip(self: object) -> None:
        """The main decoding method of the controller, it first decodes the
        sequence with Huffman decompression, then passes the uncompressed
        sequence to do the Inverse of Burros-Wheeler transform and obtain
        the original sequence.

        Returns
        -------
        None
            Fills all the properties of an object and writes out the
            original sequence to a file.

        """
        self.huff_decoder = HuffDecoder(self.path)
        self.huff_decoder.decode()

        self.bw_decoder = BWDecoder(self.huff_decoder.dehuffman_output)
        self.bw_decoder.decode()
