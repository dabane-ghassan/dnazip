#!/usr/bin/env python3
# -*- coding: utf-8 -*

# coding: utf-8

import os
from tkinter import Button
from tkinter import Entry
from tkinter import filedialog 
from tkinter import Label
from tkinter import Menu
from tkinter import StringVar
from tkinter import Tk
from tkinter import messagebox
"""
Class Interface of dnazip.

@author : Ghassan DABANE
"""
class Interface(Tk):
    
    def __init__(self):
        
        super().__init__()
        self.widgets_labs = {}
        self.widgets_entry = {}
        self.widgets_button = {}
        self.buttons = ["Chercher", "Inserer", "Effacer"]
        self.modelListFields = []
        self.fileName = None

    def open_file(self):
        self.fileName = filedialog.askopenfilename(initialdir= os.getcwd(),title="Select File",filetypes=(("Text Files", "*.txt"),("all files","*.*"))) 
        #self.controller.set_model_config(self.fileName)

    def create_menu(self):
        menubar = Menu(self)

        menuFile = Menu(menubar, tearoff=0)
        menuFile.add_command(label="Open", command=self.open_file, accelerator="Ctrl+o")
        menuFile.add_separator()
        menuFile.add_command(label="Quit", command=self.quit, accelerator="Ctrl+q")
        menubar.add_cascade( label="File", menu=menuFile)
        self.bind_all("<Control-q>", self.quit)
        self.bind_all("<Control-o>", lambda e: self.open_file())

        self.config(menu=menubar)

    def main(self):
        print("[View] main")
        self.title("dnazip")
        self.create_menu()
        self.mainloop()
        
    def quit(self):
        self.controller.save()
        self.destroy()

yo = Interface()
yo.main()
    