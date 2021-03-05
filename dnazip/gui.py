#!/usr/bin/env python3
# -*- coding: utf-8 -*
import os
from tkinter import Tk, Button, Toplevel, filedialog, Menu, messagebox
from sequence import Sequence
from decoder import HuffDecoder, BWDecoder, FullDecoder
from encoder import HuffEncoder, BWEncoder, FullEncoder

"""
Class Interface of the main application.

@author : Ghassan DABANE
"""
class Interface(Tk):
    
    def __init__(self):
        
        super().__init__()
        self.title("dnazip")
        self.create_menu()
        self.create_buttons()
        self.file = None
        
    def create_buttons(self):
        buttons = {"BWT": Button(
            self, text="BWT", command=self.bwt).grid(row=0,column=0),
                   "DEBWT": Button(
                       self, text="reverse BWT", command=self.debwt).grid(
                           row=1,column=0),
                   "Huffcode": Button(
                       self, text="Huffman coding", command=self.huffcode).grid(
                           row=0,column=1),
                   "Huffdecode": Button(
                       self, text="Huffman decoding", command=self.huffdecode).grid(
                           row=1,column=1),
                   "fullzip": Button(
                       self, text="Full zip", command=self.fullzip).grid(
                           row=0,column=2),
                   "fullunzip": Button(
                       self, text="Full unzip", command=self.fullunzip).grid(
                           row=1,column=2)}
        self.buttons = buttons

    def open_file(self):

        self.file = filedialog.askopenfilename(
            initialdir= os.getcwd(),title="Select File",filetypes=(
                ("Text Files", "*.txt"),("all files","*.*")))

        if self.file:
            messagebox.showinfo("Selected file", "You have selected %s"%(
                self.file))

    def bwt(self):
        
        if self.file:
            bwt_window = Toplevel(self)
            bwt_window.title("Burros-Wheeler Transform")
            bwt_window.geometry("600x600")
        else: 
            self.no_file_error()
        
    def debwt(self):
        if self.file:
            debwt_window = Toplevel(self)
            debwt_window.title("Reversing Burros-Wheeler Transform")
            debwt_window.geometry("600x600")
        else: 
            self.no_file_error()        
    def huffcode(self):
        if self.file:
            huff_code_window = Toplevel(self)
            huff_code_window.title("Huffman coding")
            huff_code_window.geometry("600x600")
        else: 
            self.no_file_error()
    def huffdecode(self):
        if self.file:
            huff_decode_window = Toplevel(self)
            huff_decode_window.title("Huffman decoding")
            huff_decode_window.geometry("600x600")
        else: 
            self.no_file_error()       
    def fullzip(self):
        if self.file:
            fullzip_window = Toplevel(self)
            fullzip_window.title("Burrow-Wheeler Transform + Huffman coding")
            fullzip_window.geometry("600x600")
        else: 
            self.no_file_error()       
    def fullunzip(self):
        if self.file:
            fullzip_window = Toplevel(self)
            fullzip_window.title("Huffman decoding + reverse Burros-Wheeler transform")
            fullzip_window.geometry("600x600")
        else: 
            self.no_file_error()

    def create_menu(self):
        
        menubar = Menu(self)
        menuFile = Menu(menubar, tearoff=0)
        menuFile.add_command(label="Open", command=self.open_file, accelerator="Ctrl+o")
        menubar.add_cascade( label="File", menu=menuFile)
        self.bind_all("<Control-o>", lambda e: self.open_file())
        self.config(menu=menubar)

    def no_file_error(self):
        messagebox.showerror("No file selected", "Please select a file")

    def main(self):
        print("[View] main")
        self.mainloop()

    def quit(self):
        self.destroy()

yo = Interface()
yo.main()
    