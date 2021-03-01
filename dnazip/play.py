#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 09:22:57 2021

@author: ghassan
"""
from sequence import Sequence, RandomSequence
from encoder import Encoder
from decoder import Decoder

RandomSequence('../data/randseq100kb.txt', 100*1000).generate()
yo = Encoder('../data/randseq100kb.txt')
yo.encode_bw()

yo.encode_huffman()

yo = Decoder('../data/randseq100kb_compressed.txt')
yo.decode_huffman()

yo.decode_bwt()
