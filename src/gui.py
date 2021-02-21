#!/usr/bin/env python3
# -*- coding: utf-8 -*-



"""
Created on Sun Feb 21 09:19:13 2021

@author: ghassan

from dearpygui.core import *
from dearpygui.simple import *

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

    add_button("Directory Selector", callback=file_picker)
    add_text("Directory Path: ")
    add_same_line()
    add_label_text("##filedir", source="directory", color=[255, 0, 0])
    add_text("File: ")
    add_same_line()
    add_label_text("##file", source="file", color=[255, 0, 0])
    add_text("File Path: ")
    add_same_line()
    add_label_text("##filepath", source="file_path", color=[255, 0, 0])
    
    with window("Welcome", autosize=True):
        add_text("")


start_dearpygui(primary_window="Main")
"""