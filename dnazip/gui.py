#!/usr/bin/env python3
# -*- coding: utf-8 -*

from dearpygui.core import *
from dearpygui.simple import *
import os
os.chdir(os.path.expanduser('~'))

def file_picker(sender, data):
    open_file_dialog(callback=apply_selected_file, extensions=".*")

def apply_selected_file(sender, data):

    log_debug(data)  # so we can see what is inside of data
    directory = data[0]
    file = data[1]
    set_value("directory", directory)
    set_value("file", file)
    set_value("file_path", f"{directory}/{file}")

with window("Main"):

    set_theme("Red")
    add_button("Select file", callback=file_picker)
    add_text("Chosen file: ")
    add_same_line()
    add_label_text("##filepath", source="file_path", color=[255, 0, 0])

    with window("Welcome", autosize=True):
        add_text("Welcome to dnazip!")
     
    with window("Burros-Wheeler Transform"):
        add_button("Next")
        
    with window("Huffman Coding"):
        add_button("Next")
        
    with window("Burros-Wheeler Detransform"):
        add_button("Next")
        
    with window("Huffman Decoding"):
        add_button("Next")
    

start_dearpygui(primary_window="Main")
