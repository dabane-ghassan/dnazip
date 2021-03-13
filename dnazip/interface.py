#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""
View architecture of the main application, i.e; a GUI.

@author : Ghassan Dabane
"""
from __future__ import absolute_import
import os
from tkinter import Tk, Toplevel, filedialog, Menu, messagebox, ttk
from tkinter import Label, Entry, Button, StringVar, Text, Scrollbar
from tkinter import RIGHT, Y, X,  HORIZONTAL, BOTTOM, NONE, END
from typing import Iterator, Generator
from dnazip.sequence import Sequence
from dnazip.decoder import HuffDecoder, BWDecoder, FullDecoder
from dnazip.encoder import HuffEncoder, BWEncoder, FullEncoder

class Interface(Tk):
    """View class of the application using a Tkinter interface."""

    def __init__(self: object) -> None:
        """Class constructor

        Returns
        -------
        None
            An interface instance.

        """
        super().__init__()
        self.title("dnazip")
        self.configure(bg='#ebebeb')
        self.create_main()
        self.create_menu()
        self.create_buttons()
        self.file = None

    def create_main(self: object) -> None:
        """This method is used to create the main menu interface of the GUI."""

        welcome_msg = "Welcome to dnazip! \n A graphical " + \
            "representation of Burros-Wheeler and Huffman " + \
            "Coding algorithms"
        rand = "You don't have a DNA sequence? we'll generate a small " + \
            "random one for you"
        Label(self, text=welcome_msg, bg='#ebebeb', font=(None, 15)).grid(row=0, columnspan=3, padx=5, pady=6)
        Label(self, text="Compression", bg='#ebebeb', borderwidth=2, relief="groove", font=(None, 13, 'bold')).grid(row=1, columnspan=3, padx=5, pady=6)
        Label(self, text="Decompression", bg='#ebebeb', borderwidth=2, relief="groove", font=(None, 13, 'bold')).grid(row=5, columnspan=3, padx=5, pady=6)
        separator_one = ttk.Separator(self, orient='horizontal')
        separator_one.grid(row=4, columnspan=3, ipadx=500, padx=5, pady=6) 
        Label(self, text=rand, bg='#ebebeb', font=(None, 12, 'bold')).grid(row=8, columnspan=3, padx=5, pady=6)
        self.random = StringVar()
        self.entry = Entry(self, textvariable=self.random, width=50)
        self.entry.grid(row=9, columnspan=3, padx=5, pady=10)
        separator_two = ttk.Separator(self, orient='horizontal')
        separator_two.grid(row=7, columnspan=3, ipadx=500, padx=5, pady=6) 

    def create_buttons(self: object) -> None:
        """This method creates buttons for the interface."""
        buttons = {"BWT": Button(
            self, text="BWT", command=self.bwt_window, width = 15).grid(row=3,column=0, padx=5, pady=6),
                   "DEBWT": Button(
                       self, text="reverse BWT", command=self.debwt_window,width = 15).grid(
                           row=6,column=0, padx=5, pady=6),
                   "Huffcode": Button(
                       self, text="Huffman coding", command=self.huffcode_window, width = 15).grid(
                           row=3,column=1, padx=5, pady=6),
                   "Huffdecode": Button(
                       self, text="Huffman decoding", command=self.huffdecode_window, width = 15).grid(
                           row=6,column=1, padx=5, pady=6),
                   "fullzip": Button(
                       self, text="Full zip", command=self.fullzip_window, width = 15).grid(
                           row=3,column=2, padx=5, pady=6),
                   "fullunzip": Button(
                       self, text="Full unzip", command=self.fullunzip_window, width = 15).grid(
                           row=6,column=2, padx=5, pady=6),
                    "generate": Button(
                       self, text="Generate", command=self.generate_random, width = 15).grid(
                           row=10,column=1, padx=5, pady=6),
                     "save": Button(
                       self, text="Save", command=self.save_random, width = 15).grid(
                           row=11,column=1, padx=5, pady=6)}

        self.buttons = buttons

    def open_file(self: object) -> None:
        """This method is used to create a file chooser for the interface."""
        self.file = filedialog.askopenfilename(
            initialdir= os.getcwd(),title="Select File",filetypes=(
                ("Text Files", "*.txt"),("all files","*.*")))

        if self.file:
            messagebox.showinfo("Selected file", "You have selected %s"%(
                self.file))

    def save_random(self: object) -> None:
        """This method is used to save a randomly generated DNA sequence 
        to a file.
        """
        seq_to_save = self.entry.get()
        if seq_to_save:
            path = filedialog.asksaveasfilename(
                initialdir= os.getcwd(),title="Select File", filetypes=(
                    ("Text Files", "*.txt"), ("all files","*.*")))
            if path:
                Sequence(path).write(seq_to_save)
                messagebox.showinfo("Sequence saved", "The sequence was saved to %s" %(
                    path))
        else:
            messagebox.showerror("No sequence entered", "The sequence box is empty")

    def about(self: object) -> None:
        """This method is used to generate the about menu page information."""
        msg = 'This project is developed for the "Sequence Algorithms" ' + \
            'Course as a part of The M.Sc. in Bioinformatics degree at ' + \
                'Aix-Marseille University, France. \n' + \
        'Source code available at: https://github.com/dabane-ghassan/dnazip'
        messagebox.showinfo("About dnazip", msg)

    def generate_random(self: object) -> None:
        """This method is used to generate random sequences of DNA of length
        50 and show them inside the random text box tkinter entry.
        """
        self.random.set(Sequence.generate(length=50))

    def next_btn(self: object, controller: Iterator[str]) -> str:
        """This method is used to create the output of a universal next button
        for all protocols of the program, it will be passed to a given label
        that changes its content.

        Parameters
        ----------
        controller : Iterator[str]
            The controller of a given protocol that contains all steps to show.

        Returns
        -------
        str
            Every step to be shown, one at a time.
        """
        try:
            to_print = next(controller)
            if isinstance(to_print, list):
                return '\n'.join(to_print)
            else:  
                return to_print

        except StopIteration:
            return "The protocole is finished"

    def final_btn(self: object, controller: Iterator[str]) -> str:
        """This method is used to create the output of a universal final step 
        button for all protocols of the program, it will be passed to a given
        label that changes its content.

        Parameters
        ----------
        controller : Iterator[str]
            The controller of a given protocol that contains all steps to show.

        Returns
        -------
        str
            The final step to be shown.
        """
        
        try:
            to_print = list(controller)[-1] # Getting the final result of a generator
            return to_print

        except IndexError:
            return "The protocole is finished, please refer to the main menu."

    def step_by_step(self: object, window: Tk, protocol: Iterator[str], names: Generator)-> None:
        """This method creates a universal step by step advancing interface
        for a given chosen protocole.

        Parameters
        ----------
        window : Tk
            The given window.
        protocol : Iterator[str]
            The output protocol to be displayed.
        names : Generator
            The names of the steps to be displayed.

        """ 
        steps = StringVar()
        current_step = Label(window, textvariable=steps, bg="#ebebeb",
                     font=(None, 9, "bold"), borderwidth=2)
        current_step.place(relx = 0.5, 
                   rely = 0.1, anchor="center")
        xscrollbar = Scrollbar(window, orient=HORIZONTAL)
        xscrollbar.pack(side=BOTTOM, fill=X)

        # Vertical (y) Scroll Bar
        yscrollbar = Scrollbar(window)
        yscrollbar.pack(side=RIGHT, fill=Y)

        # Text Widget
        text = Text(window, wrap=NONE, width=100, height=40,
                    xscrollcommand=xscrollbar.set,
                    yscrollcommand=yscrollbar.set)
        text.place(relx = 0.5,
                   rely = 0.5,
                   anchor = 'center')

        # Configure the scrollbars
        xscrollbar.config(command=text.xview)
        yscrollbar.config(command=text.yview)

        Button(window, text="Next",
               command=lambda : [self.update_text(text,
                   self.next_btn(protocol)),steps.set(
                       self.next_btn(names))]).pack(side="bottom")

        Button(window, text="Final step",
        command=lambda : [self.update_text(text,
            self.final_btn(protocol)), steps.set(
                       self.final_btn(names))]).pack(side="bottom")

    def update_text(self: object, widget: Text, new_text: str) -> None:
        """This method updates the Text tkinter widget with every step
        in every protocol. it deletes its contents and then replaces it with
        new_text parameter.

        Parameters
        ----------
        widget : Text
            Tkinter's Text widget.
        new_text : str
            The new text to be shown in the widget.

        Returns
        -------
        None
            Replaces text in a given Text widget.

        """
        widget.delete("1.0", END)   #Clear the text window so we can write.
        widget.insert(END,new_text) 

    def BW_output(self: object, controller: BWEncoder) -> Iterator[str]:
        """This method is used to collect all output for the BW encoding.

        Parameters
        ----------
        controller : BWEncoder
            The given controller.

        Yields
        ------
        Iterator[str]
            The content to be shown in the interface.

        """
        yield controller.seq.read()
        for rot in controller.rotations:
            yield rot
        yield controller.bwm
        yield controller.bwt

    def bwt_window(self: object) -> None:
        """This method creates a Tkinter Toplevel window for the step-by-step
        BWT protocol, The output file of the protocol will be shown at the 
        beginning.

        """
        if self.file:
            bwt_window = Toplevel(self)
            bwt_window.title("Burros-Wheeler Transform")
            bwt_window.geometry("1000x1000")
            bwt_window.configure(bg='#ebebeb')
            controller = BWEncoder(self.file)
            controller.encode()
            protocol = self.BW_output(controller)
            prot= list(protocol)

            rots = ["Step 2: Generating all rotations of the sequence" for n in range(len(prot) - 3)]
            
            names = (step for step in ["Step 1 : Visualizing the sequence",
                     *rots,
                     "Step 3: Creating the Burros-Wheeler matrix by sorting all rotations",
                     "Step 4: The Burros-Wheeler transform is the last column of the matrix",
                     "Please refer to the main menu to select another sequence"])
            
            self.step_by_step(bwt_window, iter(prot), names)
            self.program_output(bwt_window, controller.bwt_output)

        else:
            self.no_file_error()

    def DeBW_output(self: object, controller: BWDecoder) -> Iterator[str]:
        """This method is used to collect all output for the BW decoding.

        Parameters
        ----------
        controller : BWDecoder
            The given controller.

        Yields
        ------
        Iterator[str]
            The content to be shown in the interface.

        """
        yield controller.seq.read()
        for mat in controller.bwm:
            yield mat
        yield controller.original

    def debwt_window(self: object) -> None:
        """This method creates a Tkinter Toplevel window for the step-by-step
        inverse BWT protocol, The output file of the protocol will be shown at
        the beginning.

        """
        if self.file:
            debwt_window = Toplevel(self)
            debwt_window.title("Reversing Burros-Wheeler Transform")
            debwt_window.geometry("1000x1000")
            debwt_window.configure(bg='#ebebeb')
            controller = BWDecoder(self.file)
            controller.decode()
            protocol = self.DeBW_output(controller)
            prot= list(protocol)
            
            reconstructed = ["Step 2: Creating the Burros-Wheeler Matrix" for n in range(len(prot) - 2)]

            names = (step for step in ["Step 1 : Visualizing the sequence",
                     *reconstructed,
                     "Step 3: The original sequence is the one that has a $ sign as a last column",
                     "Please refer to the main menu to select another sequence"])

            self.step_by_step(debwt_window, iter(prot), names)
            self.program_output(debwt_window, controller.debwt_output)

        else:
            self.no_file_error()

    def Huff_output(self: object, controller: HuffEncoder) -> Iterator[str]:
        """This method is used to collect all output for Huffman encoding.

        Parameters
        ----------
        controller : HuffEncoder
            The given controller.

        Yields
        ------
        Iterator[str]
            The content to be shown in the interface.

        """
        yield controller.seq.read()
        yield controller.header
        yield controller.binary
        yield controller.unicode
        yield controller.compressed

    def huffcode_window(self: object) -> None:
        """This method creates a Tkinter Toplevel window for the step-by-step
        Huffman coding protocol, The output file of the protocol will be shown
        at the beginning.

        """
        if self.file:
            huff_code_window = Toplevel(self)
            huff_code_window.title("Huffman coding")
            huff_code_window.geometry("1000x1000")
            huff_code_window.configure(bg='#ebebeb')
            names = (step for step in ["Step 1 : Visualizing the sequence",
                     "Step 2: Creating Huffman tree from sequence and calculating paths",
                     "Step 3: Generating the binary sequence from paths and adding a padding",
                     "Step 4: Coding the binary in 8-bits to unicode",
                     "Step 5: Writing paths and unicode to an output file",
                     "Please refer to the main menu to select another sequence"])
            controller = HuffEncoder(self.file)
            controller.encode()
            protocol = self.Huff_output(controller)
            self.step_by_step(huff_code_window, protocol, names)
            self.program_output(huff_code_window, controller.huff_output)

        else:
            self.no_file_error()

    def deHuff_output(self: object, controller: HuffDecoder) -> Iterator[str]:
        """This method is used to collect all output for the Huff decoding.

        Parameters
        ----------
        controller : HuffDecoder
            The given controller.

        Yields
        ------
        Iterator[str]
            The content to be shown in the interface.

        """
        yield controller.seq.read()
        yield controller.header
        yield controller.unicode
        yield controller.binary 
        yield controller.decompressed

    def huffdecode_window(self: object) -> None:
        """This method creates a Tkinter Toplevel window for the step-by-step
        Huffman decoding, The output file of the protocol will be shown at the 
        beginning.

        """
        if self.file:
            huff_decode_window = Toplevel(self)
            huff_decode_window.title("Huffman decoding")
            huff_decode_window.geometry("1000x1000")
            huff_decode_window.configure(bg='#ebebeb')
            names = (step for step in ["Step 1 : Visualizing the compressed sequence",
                     "Step 2: Reading the header of the file that corresponds to Huffman codes that where created with the tree during compression",
                     "Step 3: Separating the unicode sequence",
                     "Step 4: Transforming the unicode sequence to binary using huffman codes in the header and stripping padding",
                     "Step 5: The decompressed sequence : ",
                     "Please refer to the main menu to select another sequence"])
            controller = HuffDecoder(self.file)
            controller.decode()
            protocol = self.deHuff_output(controller)
            self.step_by_step(huff_decode_window, protocol, names)
            self.program_output(huff_decode_window, controller.dehuffman_output)

        else:
            self.no_file_error()   

    def fullzip_output(self: object, controller: FullEncoder) -> Iterator[str]:
        """This method is used to collect all output for a full protocol
        encoding (BWT + Huffman compression).

        Parameters
        ----------
        controller : FullEncoder
            The given controller.

        Yields
        ------
        Iterator[str]
            The content to be shown in the interface.

        """
        yield controller.bw_encoder.seq.read()
        for rot in controller.bw_encoder.rotations:
            yield rot
        yield controller.bw_encoder.bwm
        yield controller.bw_encoder.bwt
        yield controller.huff_encoder.header
        yield controller.huff_encoder.binary
        yield controller.huff_encoder.unicode
        yield controller.huff_encoder.compressed

    def fullzip_window(self: object) -> None:
        """This method creates a Tkinter Toplevel window for the step-by-step
        Fullzip protocol (BWT+Huffman compression), The output file of the 
        protocol will be shown at the beginning.

        """
        if self.file:
            fullzip_window = Toplevel(self)
            fullzip_window.title("Burrow-Wheeler Transform + Huffman coding")
            fullzip_window.geometry("1000x1000")
            fullzip_window.configure(bg='#ebebeb')
            controller = FullEncoder(self.file)
            controller.full_zip()
            protocol = self.fullzip_output(controller)
            prot= list(protocol)

            rots = ["Step 2: Generating all rotations of the sequence" for n in range(len(prot) - 7)]
            names = (step for step in ["Step 1 : Visualizing the sequence",
                     *rots,
                     "Step 3: Creating the Burros-Wheeler matrix by sorting all rotations",
                     "Step 4: The Burros-Wheeler transform is the last column of the matrix",
                     "Step 5: Creating Huffman tree from Burros-Wheeler transform and calculating paths",
                     "Step 6: Generating the binary sequence from paths and adding a padding",
                     "Step 7: Coding the binary in 8-bits to unicode",
                     "Step 8: Writing paths and unicode to an output file",
                     "Please refer to the main menu to select another sequence"])

            self.step_by_step(fullzip_window, iter(prot), names)
            outputs = controller.bw_encoder.bwt_output + \
                '\n' + controller.huff_encoder.huff_output
            self.program_output(fullzip_window, outputs)

        else:
            self.no_file_error()

    def fullunzip_output(self: object, controller: FullDecoder) -> Iterator[str]:
        """This method is used to collect all output for a full decompression
        protocol.

        Parameters
        ----------
        controller : FullDecoder
            The given controller.

        Yields
        ------
        Iterator[str]
            The content to be shown in the interface.

        """
        yield controller.huff_decoder.seq.read()
        yield controller.huff_decoder.header
        yield controller.huff_decoder.unicode
        yield controller.huff_decoder.binary 
        yield controller.huff_decoder.decompressed
        for line in controller.bw_decoder.bwm:
            yield line
        yield controller.bw_decoder.original

    def fullunzip_window(self: object) -> None:
        """This method creates a Tkinter Toplevel window for the step-by-step
        Full unzipping protocol (HUffman decoding + inverse BWT), The output 
        file of the protocol will be shown at the beginning.

        """
        if self.file:
            fullunzip_window = Toplevel(self)
            fullunzip_window.title("Huffman decoding + reverse Burros-Wheeler transform")
            fullunzip_window.geometry("1000x1000")
            fullunzip_window.configure(bg='#ebebeb')
            controller = FullDecoder(self.file)
            controller.full_unzip()
            protocol = self.fullunzip_output(controller)
            prot= list(protocol)

            reconstructed = ["Step 6: Creating the Burros-Wheeler Matrix" for n in range(len(prot) - 6)]
            names = (step for step in ["Step 1 : Visualizing the compressed sequence",
                     "Step 2: Reading the header of the file that corresponds to Huffman codes that where created with the tree during compression",
                     "Step 3: Separating the unicode sequence",
                     "Step 4: Transforming the unicode sequence to binary using huffman codes in the header and stripping padding",
                     "Step 5: The decompressed sequence is the burros wheeler transform of the original sequence:",
                     *reconstructed,
                     "Step 7: The original sequence is the one that has a $ sign as a last column in the Burros-Wheeler Matrix",
                     "Please refer to the main menu to select another sequence"])

            self.step_by_step(fullunzip_window, iter(prot), names)
            outputs = controller.huff_decoder.dehuffman_output + \
                '\n' + controller.bw_decoder.debwt_output
            self.program_output(fullunzip_window, outputs)
        else:
            self.no_file_error()

    def create_menu(self: object) -> None:
        """Creates the menu for the interface."""
        menubar = Menu(self)
        menuFile = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Menu", menu=menuFile)
        #menubar.add_cascade(label="About", menu=menuFile)
        menuFile.add_command(label="Choose a file", command=self.open_file,
                             accelerator="Ctrl+o")
        menuFile.add_command(label="About", command=self.about)
        self.bind_all("<Control-o>", lambda e: self.open_file())
        self.config(menu=menubar)

    def no_file_error(self: object) -> None:
        """Shows an error when no file is selected."""
        messagebox.showerror("No file selected", "Please select a file")

    def program_output(self: object, window: Tk,  path: str) -> None:
        """Shows the output of a given protocol.

        Parameters
        ----------
        window : Tk
            The given window.
        path : str
            The output file path to be shown in the messagebox.

        """
        messagebox.showinfo(parent=window, title="Program output",
                            message="The output will be saved to \n %s" %(
                                path))

    def main(self: object) -> None:
        """Launches the mainloop of the interface."""
        print("[View] main")
        self.mainloop()

    def quit(self: object) -> None:
        """Quits the current interface."""
        self.destroy()
