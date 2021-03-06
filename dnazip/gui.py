#!/usr/bin/env python3
# -*- coding: utf-8 -*
import os
from tkinter import Tk, Button, Toplevel, filedialog, Menu, messagebox, Label, StringVar
from sequence import Sequence, RandomSequence
from decoder import HuffDecoder, BWDecoder, FullDecoder
from encoder import HuffEncoder, BWEncoder, FullEncoder
from burros_wheeler import BurrosWheeler

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
            self, text="BWT", command=self.bwt_window).grid(row=0,column=0),
                   "DEBWT": Button(
                       self, text="reverse BWT", command=self.debwt_window).grid(
                           row=1,column=0),
                   "Huffcode": Button(
                       self, text="Huffman coding", command=self.huffcode_window).grid(
                           row=0,column=1),
                   "Huffdecode": Button(
                       self, text="Huffman decoding", command=self.huffdecode_window).grid(
                           row=1,column=1),
                   "fullzip": Button(
                       self, text="Full zip", command=self.fullzip_window).grid(
                           row=0,column=2),
                   "fullunzip": Button(
                       self, text="Full unzip", command=self.fullunzip_window).grid(
                           row=1,column=2)}
        self.buttons = buttons

    def open_file(self):

        self.file = filedialog.askopenfilename(
            initialdir= os.getcwd(),title="Select File",filetypes=(
                ("Text Files", "*.txt"),("all files","*.*")))

        if self.file:
            messagebox.showinfo("Selected file", "You have selected %s"%(
                self.file))

    def next_btn(self, controller): 

        try:
            to_print = next(controller)
            if isinstance(to_print, list):
                return '\n'.join(to_print)
            else: 
                return to_print

        except StopIteration:
            return "The protocole is finished"

    def BW_output(self, controller):

        controller.encode()
        yield controller.seq.read()
        yield controller.rotations
        yield controller.bwm
        yield controller.bwt


    def bwt_window(self):
        
        if self.file:
            bwt_window = Toplevel(self)
            bwt_window.title("Burros-Wheeler Transform")
            bwt_window.geometry("600x600")
            names = (step for step in ["Step 1 : Visualizing the sequence",
                     "Step 2: Generating all rotations of the sequence",
                     "Step 3: Creating the Burros-Wheeler matrix by sorting all rotations",
                     "Step 4: The Burros-Wheeler transform is the last column of the matrix",
                     "Please refer to the main menu to select another sequence"])
            steps = StringVar()
            Label(bwt_window, textvariable=steps).pack()
            controller = BWEncoder(self.file)
            protocol = self.BW_output(controller)
            lab_content = StringVar()
            lab_content.set("Please press on the button below to start")
            Label(bwt_window, textvariable=lab_content).pack()
            Button(bwt_window, text="Next", 
                   command=lambda : [lab_content.set(
                       self.next_btn(protocol)),steps.set(
                           self.next_btn(names))]).pack(side="bottom")
            
            self.program_output(bwt_window, controller.bwt_output)

        else: 
            self.no_file_error()

    def DeBW_output(self, controller):

        
        controller.decode()
        yield controller.seq.read()
        yield controller.bwm
        yield controller.original

    def debwt_window(self):

        if self.file:
            debwt_window = Toplevel(self)
            debwt_window.title("Reversing Burros-Wheeler Transform")
            debwt_window.geometry("600x600")
            names = (step for step in ["Step 1 : Visualizing the sequence",
                     "Step 2: Creating the Burros-Wheeler Matrix",
                     "Step 3: The original sequence is the one that has a $ sign as a last column",
                     "Please refer to the main menu to select another sequence"])
            steps = StringVar()
            Label(debwt_window, textvariable=steps).pack()
            controller = BWDecoder(self.file)
            protocol = self.DeBW_output(controller)
            lab_content = StringVar()
            lab_content.set("Please press on the button below to start")
            Label(debwt_window, textvariable=lab_content).pack()
            Button(debwt_window, text="Next", 
                   command=lambda : [lab_content.set(
                       self.next_btn(protocol)),steps.set(
                           self.next_btn(names))]).pack(side="bottom")
            
            self.program_output(debwt_window, controller.debwt_output)
        else: 
            self.no_file_error()

    def Huff_output(self, controller):

        controller = HuffEncoder(self.file)
        controller.encode()
        yield controller.seq.read()
        yield controller.binary
        yield controller.compressed

    def huffcode_window(self):

        if self.file:
            huff_code_window = Toplevel(self)
            huff_code_window.title("Huffman coding")
            huff_code_window.geometry("600x600")
        else: 
            self.no_file_error()

    def deHuff_output(self, controller):

        controller = HuffDecoder(self.file)
        controller.decode()
        yield controller.seq.read()
        yield controller.binary
        yield controller.decompressed

    def huffdecode_window(self):

        if self.file:
            huff_decode_window = Toplevel(self)
            huff_decode_window.title("Huffman decoding")
            huff_decode_window.geometry("600x600")
        else: 
            self.no_file_error()   


    def fullzip_output(self, controller):

        controller = FullEncoder(self.file)
        controller.full_zip()

        yield controller.bw_encoder.seq.read()
        yield controller.bw_encoder.rotations
        yield controller.bw_encoder.bwm
        yield controller.bw_encoder.bwt
        yield controller.huff_encoder.binary
        yield controller.huff_encoder.compressed

    def fullzip_window(self):

        if self.file:
            fullzip_window = Toplevel(self)
            fullzip_window.title("Burrow-Wheeler Transform + Huffman coding")
            fullzip_window.geometry("600x600")
        else: 
            self.no_file_error()
            
    def fullunzip_output(self, controller):

        controller = FullDecoder(self.file)
        controller.full_unzip()
        
        yield controller.huff_decoder.seq.read()
        yield controller.huff_decoder.binary
        yield controller.huff_decoder.decompressed
        yield controller.bw_decoder.bwm
        yield controller.bw_decoder.original

    def fullunzip_window(self):
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
        menubar.add_cascade(label="File", menu=menuFile)
        self.bind_all("<Control-o>", lambda e: self.open_file())
        self.config(menu=menubar)

    def no_file_error(self):
        messagebox.showerror("No file selected", "Please select a file")
    
    def program_output(self, window,  path):
        messagebox.showinfo(parent=window, title="Program output", message="The output will be saved to \n %s" %(
            path))

    def main(self):
        print("[View] main")
        messagebox.showinfo("Welcome", "Welcome to dnazip! a graphical " + \
                            "representation of Burros-Wheeler and Huffman " + \
                            "Coding algorithms")
        self.mainloop()

    def quit(self):
        self.destroy()

yo = Interface()
yo.main()
