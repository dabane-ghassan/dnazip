#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main script to launch the GUI.

@author: Ghassan Dabane
"""
from __future__ import absolute_import
from dnazip.interface import Interface

def main() -> None:
    """Launches the GUI."""
    GUI = Interface()
    GUI.main()

if __name__ == "__main__":
    main()
