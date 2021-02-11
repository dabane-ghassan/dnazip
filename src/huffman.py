# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:36:09 2021

@author: KugelBlitZZZ
"""
import os
import filemanager as fm

os.chdir("C:/Users/33750/Documents/GitHub/dnazip/src")
file = fm.FileManager("../data/test_seq_bwt.txt")
seq = file.read()
seq
