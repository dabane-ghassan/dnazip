#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""
View architecture of the main application, i.e; a GUI.

@author : Ghassan DABANE
"""
import os
from tkinter import Tk, Button, Toplevel, filedialog, Menu, messagebox, Label, StringVar
from typing import Iterator
from decoder import HuffDecoder, BWDecoder, FullDecoder
from encoder import HuffEncoder, BWEncoder, FullEncoder

class Interface(Tk):
    """View class of the application using a Tkinter interface."""
    
    def __init__(self: object) -> None:

        super().__init__()
        self.title("dnazip")
        self.create_menu()
        self.create_buttons()
        self.file = None
    
    def create_buttons(self: object) -> None:

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

    def open_file(self: object) -> None:

        self.file = filedialog.askopenfilename(
            initialdir= os.getcwd(),title="Select File",filetypes=(
                ("Text Files", "*.txt"),("all files","*.*")))

        if self.file:
            messagebox.showinfo("Selected file", "You have selected %s"%(
                self.file))

    def next_btn(self: object, controller: Iterator[str]) -> str: 

        try:
            to_print = next(controller)
            if isinstance(to_print, list):
                return '\n'.join(to_print)
            else: 
                return to_print

        except StopIteration:
            return "The protocole is finished"

    def BW_output(self: object, controller: BWEncoder) -> Iterator[str]:

        yield controller.seq.read()
        yield controller.rotations
        yield controller.bwm
        yield controller.bwt

    def bwt_window(self: object) -> None:
        
        if self.file:
            bwt_window = Toplevel(self)
            bwt_window.title("Burros-Wheeler Transform")
            bwt_window.geometry("900x900")
            names = (step for step in ["Step 1 : Visualizing the sequence",
                     "Step 2: Generating all rotations of the sequence",
                     "Step 3: Creating the Burros-Wheeler matrix by sorting all rotations",
                     "Step 4: The Burros-Wheeler transform is the last column of the matrix",
                     "Please refer to the main menu to select another sequence"])
            steps = StringVar()
            Label(bwt_window, textvariable=steps).pack()
            controller = BWEncoder(self.file)
            controller.encode()
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

    def DeBW_output(self: object, controller: BWDecoder) -> Iterator[str]:

        yield controller.seq.read()
        yield controller.bwm
        yield controller.original

    def debwt_window(self: object) -> None:

        if self.file:
            debwt_window = Toplevel(self)
            debwt_window.title("Reversing Burros-Wheeler Transform")
            debwt_window.geometry("900x900")
            names = (step for step in ["Step 1 : Visualizing the sequence",
                     "Step 2: Creating the Burros-Wheeler Matrix",
                     "Step 3: The original sequence is the one that has a $ sign as a last column",
                     "Please refer to the main menu to select another sequence"])
            steps = StringVar()
            Label(debwt_window, textvariable=steps).pack()
            controller = BWDecoder(self.file)
            controller.decode()
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

    def Huff_output(self: object, controller: HuffEncoder) -> Iterator[str]:

        yield controller.seq.read()
        yield controller.header
        yield controller.binary
        yield controller.unicode
        yield controller.compressed

    def huffcode_window(self: object) -> None:

        if self.file:
            huff_code_window = Toplevel(self)
            huff_code_window.title("Huffman coding")
            huff_code_window.geometry("900x900")
            names = (step for step in ["Step 1 : Visualizing the sequence",
                     "Step 2: Creating Huffman tree from sequence and calculating paths",
                     "Step 3: Generating the binary sequence from paths and adding a padding",
                     "Step 4: Coding the binary in 8-bits to unicode",
                     "Step 5: Writing paths and unicode to an output file",
                     "Please refer to the main menu to select another sequence"])

            steps = StringVar()
            Label(huff_code_window, textvariable=steps).pack()
            controller = HuffEncoder(self.file)
            controller.encode()
            protocol = self.Huff_output(controller)
            lab_content = StringVar()
            lab_content.set("Please press on the button below to start")
            Label(huff_code_window, textvariable=lab_content).pack()
            Button(huff_code_window, text="Next", 
                   command=lambda : [lab_content.set(
                       self.next_btn(protocol)),steps.set(
                           self.next_btn(names))]).pack(side="bottom")
            
            self.program_output(huff_code_window, controller.huff_output)
        else: 
            self.no_file_error()

    def deHuff_output(self: object, controller: HuffDecoder) -> Iterator[str]:

        yield controller.seq.read()
        yield controller.header
        yield controller.unicode
        yield controller.binary 
        yield controller.decompressed

    def huffdecode_window(self: object) -> None:

        if self.file:
            huff_decode_window = Toplevel(self)
            huff_decode_window.title("Huffman decoding")
            huff_decode_window.geometry("900x900")
            names = (step for step in ["Step 1 : Visualizing the compressed sequence",
                     "Step 2: Reading the header of the file that corresponds to Huffman codes that where created with the tree during compression",
                     "Step 3: Separating the unicode sequence",
                     "Step 4: Transforming the unicode sequence to binary using huffman codes in the header and stripping padding",
                     "Step 5: The decompressed sequence : ",
                     "Please refer to the main menu to select another sequence"])

            steps = StringVar()
            Label(huff_decode_window, textvariable=steps).pack()
            controller = HuffDecoder(self.file)
            controller.decode()
            protocol = self.deHuff_output(controller)
            lab_content = StringVar()
            lab_content.set("Please press on the button below to start")
            Label(huff_decode_window, textvariable=lab_content).pack()
            Button(huff_decode_window, text="Next", 
                   command=lambda : [lab_content.set(
                       self.next_btn(protocol)),steps.set(
                           self.next_btn(names))]).pack(side="bottom")
            
            self.program_output(huff_decode_window, controller.dehuffman_output)
            
        else: 
            self.no_file_error()   


    def fullzip_output(self: object, controller: FullEncoder) -> Iterator[str]:

        yield controller.bw_encoder.seq.read()
        yield controller.bw_encoder.rotations
        yield controller.bw_encoder.bwm
        yield controller.bw_encoder.bwt
        yield controller.huff_encoder.header
        yield controller.huff_encoder.binary
        yield controller.huff_encoder.unicode
        yield controller.huff_encoder.compressed

    def fullzip_window(self: object) -> None:

        if self.file:
            fullzip_window = Toplevel(self)
            fullzip_window.title("Burrow-Wheeler Transform + Huffman coding")
            fullzip_window.geometry("900x900")  
            names = (step for step in ["Step 1 : Visualizing the sequence",
                     "Step 2: Generating all rotations of the sequence",
                     "Step 3: Creating the Burros-Wheeler matrix by sorting all rotations",
                     "Step 4: The Burros-Wheeler transform is the last column of the matrix",
                     "Step 5: Creating Huffman tree from Burros-Wheeler transform and calculating paths",
                     "Step 6: Generating the binary sequence from paths and adding a padding",
                     "Step 7: Coding the binary in 8-bits to unicode",
                     "Step 8: Writing paths and unicode to an output file",
                     "Please refer to the main menu to select another sequence"])

            steps = StringVar()
            Label(fullzip_window, textvariable=steps).pack()
            controller = FullEncoder(self.file)
            controller.full_zip()
            protocol = self.fullzip_output(controller)
            lab_content = StringVar()
            lab_content.set("Please press on the button below to start")
            Label(fullzip_window, textvariable=lab_content).pack()
            Button(fullzip_window, text="Next", 
                   command=lambda : [lab_content.set(
                       self.next_btn(protocol)),steps.set(
                           self.next_btn(names))]).pack(side="bottom")
            
            outputs = controller.bw_encoder.bwt_output + '\n' + controller.huff_encoder.huff_output
            self.program_output(fullzip_window, outputs)

        else: 
            self.no_file_error()
            
    def fullunzip_output(self: object, controller: FullDecoder) -> Iterator[str]:
  
        yield controller.huff_decoder.seq.read()
        yield controller.huff_decoder.header
        yield controller.huff_decoder.unicode
        yield controller.huff_decoder.binary 
        yield controller.huff_decoder.decompressed
        yield controller.bw_decoder.bwm
        yield controller.bw_decoder.original

    def fullunzip_window(self: object) -> None:

        if self.file:

            fullunzip_window = Toplevel(self)
            fullunzip_window.title("Huffman decoding + reverse Burros-Wheeler transform")
            fullunzip_window.geometry("900x900")

            names = (step for step in ["Step 1 : Visualizing the compressed sequence",
                     "Step 2: Reading the header of the file that corresponds to Huffman codes that where created with the tree during compression",
                     "Step 3: Separating the unicode sequence",
                     "Step 4: Transforming the unicode sequence to binary using huffman codes in the header and stripping padding",
                     "Step 5: The decompressed sequence is the burros wheeler transform of the original sequence:",
                     "Step 6: Creating the Burros-Wheeler Matrix from the decompressed sequence",
                     "Step 7: The original sequence is the one that has a $ sign as a last column in the Burros-Wheeler Matrix",
                     "Please refer to the main menu to select another sequence"])

            steps = StringVar()
            Label(fullunzip_window, textvariable=steps).pack()
            controller = FullDecoder(self.file)
            controller.full_unzip()
            protocol = self.fullunzip_output(controller)
            lab_content = StringVar()
            lab_content.set("Please press on the button below to start")
            Label(fullunzip_window, textvariable=lab_content).pack()
            Button(fullunzip_window, text="Next", 
                   command=lambda : [lab_content.set(
                       self.next_btn(protocol)),steps.set(
                           self.next_btn(names))]).pack(side="bottom")

            outputs = controller.huff_decoder.dehuffman_output + '\n' + controller.bw_decoder.debwt_output
            self.program_output(fullunzip_window, outputs)
            
        else: 
            self.no_file_error()

    def create_menu(self: object) -> None:
        
        menubar = Menu(self)
        menuFile = Menu(menubar, tearoff=0)
        menuFile.add_command(label="Open", command=self.open_file, accelerator="Ctrl+o")
        menubar.add_cascade(label="File", menu=menuFile)
        self.bind_all("<Control-o>", lambda e: self.open_file())
        self.config(menu=menubar)

    def no_file_error(self: object) -> None:
        messagebox.showerror("No file selected", "Please select a file")
    
    def program_output(self: object, window: Tk,  path: str) -> None:
        messagebox.showinfo(parent=window, title="Program output", message="The output will be saved to \n %s" %(
            path))

    def main(self: object) -> None:
        print("[View] main")
        messagebox.showinfo("Welcome", "Welcome to dnazip! a graphical " + \
                            "representation of Burros-Wheeler and Huffman " + \
                            "Coding algorithms")
        self.mainloop()

    def quit(self: object) -> None:
        self.destroy()

yo = Interface()
yo.main()
