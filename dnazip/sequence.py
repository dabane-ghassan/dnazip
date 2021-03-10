# -*- coding: utf-8 -*-
"""
A script to read and write DNA sequences (or a list of characters) to a file.
In a MVC structure, this represents the Model of the data.

@author: Ghassan DABANE
"""
from __future__ import absolute_import
import random

class Sequence:
    """A class to represent a sequence, sequences can be read from files or
    writtes to files.

    Attributes
    ----------
    path: str
        The path of the file to be read.

    """

    def __init__(self: object, path: str) -> None:
        """Class constructor.

        Parameters
        ----------
        path : str
            The path of the file to be read.

        Returns
        -------
        None
            A class instance.

        """
        self.path = path

    def __str__(self: object) -> str:
        """This method returns a string representation of the object with
        print().

        Returns
        -------
        str
            A user friendly string representation.

        """
        return "Hey there! I'm a Sequence object"

    def __repr__(self: object) -> str:
        """This method returns a coder-friendly string representation of the
        object.

        Returns
        -------
        str
            A string representation of a sequence object.

        """
        return "Sequence(%s)" % self.path

    def read(self: object) -> str:
        """This method is used to read the contents of the file into a python
        string.

        Returns
        -------
        str
            The contents of the file, i.e. the sequence.

        """
        seq = ""
        with open(self.path, 'r') as file:
            for line in file:
                seq += line.strip("\n")
        return seq

    def read_bytes(self: object) -> str:
        """This method is used to read a file that has been written in bytes,
        it will be useful when reading files that has been compressed with
        Huffman coding.

        Returns
        -------
        str
            The contents of the file, i.e. the sequence.

        """
        seq = ""
        with open(self.path, 'rb') as file:
            for line in file:
                seq += line.decode("utf-8")
        return seq

    def write(self: object, content: str) -> None:
        """This method is used to write out to a file.

        Parameters
        ----------
        content : str
            The contents of the file.

        Returns
        -------
        None
            Writes out to a new file.

        """
        with open(self.path, 'w') as file:
            file.writelines(content)

    def write_bytes(self: object, content: str) -> None:
        """This method is used to write out to a new file into a bytes format,
        UTF-8 encoding, useful when we want to write out the contents of the
        Huffman compression to a file.

        Parameters
        ----------
        content : str
            The contents of the file.

        Returns
        -------
        None
            Writes out to a new file in a bytes format.

        """
        with open(self.path, 'wb') as file:
            file.write(content.encode("utf-8"))

class RandomSequence(Sequence):
    """This class is used to create a random sequence of DNA and write it out
    to a file, the alphabet is ATCGN.

    Attributes
    ----------
    path: str
        The path of the file to be created.
    length: int
        The length of the random DNA sequence to be created.

    """

    def __init__(self: object, path: str, length: int) -> None:
        """Class constructor.

        Parameters
        ----------
        path : str
            The name of the file for the new sequence to be created (a path).
        length : int
            The length of the random DNA sequence to be created.

        Returns
        -------
        None
            A class instance.

        """
        super().__init__(path)
        self.length = length

    def generate(self: object) -> None:
        """This method is used to generate the random DNA sequence using the
        random library and then write it out to a file using the parent class
        method.

        Returns
        -------
        None
            Generates the random DNA sequence.

        """
        seq = ''.join([random.choice('ATCGN') for _ in range(self.length)])
        self.write(seq)
