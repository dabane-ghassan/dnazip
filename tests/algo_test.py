# coding: utf-8
"""Script pour tester la classe linkedList.

@author: Ghassan Dabane
"""
from __future__ import absolute_import
import unittest
import sys
sys.path.append('../')
from src.burros_wheeler import BurrosWheeler
from src.huffman import HuffmanTree

class AlgorithmsTest(unittest.TestCase):
    """Test class to try out The Algorithms that were implemented, i.e;
    The Burros-Wheeler De/Transform and Huffman De/coding."""

    def setUp(self: object) -> None:
        """Initialize before every test"""
        self.sequence = "mississippi"
        self.transform = "ipssm$pissii"
        self.unicode = '\x8fL¾\x80'

    def test_bw_transform_naive(self: object) -> None:

        all_rots = BurrosWheeler.string_rotations(self.sequence)
        mat = BurrosWheeler.construct_bwm(all_rots) 
        t = BurrosWheeler.encode_bwt(mat)
        
        self.assertEqual(t, self.transform)

    def test_bw_detransform_naive(self: object) -> None:
        
        mat = BurrosWheeler.reconstruct_bwm(self.transform)
        seq = BurrosWheeler.decode_bwt(mat)
        
        self.assertEqual(seq, self.sequence)
    
    def test_bw_transform_advanced(self: object) -> None:
        
        t = BurrosWheeler.bwt_advanced(self.sequence)
        self.assertEqual(t, self.transform)
        
    def test_huffman_coding(self: object) -> None:
    
        tree = HuffmanTree(self.transform)
        tree.get_codings(tree.root)
        binary = tree.seq_to_bin_str()
        unicode = HuffmanTree.bin_str_to_unicode(binary)
        self.assertEqual(unicode, self.unicode)
        
        binary = HuffmanTree.unicode_to_bin_str(self.unicode)
        binary_no_pad = tree.remove_padding(binary)
        decoded = tree.bin_str_to_seq(binary_no_pad)
        self.assertEqual(decoded, self.transform)
 

    def tearDown(self: object) -> None:
        
        self.sequence = None
        self.transform = None
        self.unicode = None

