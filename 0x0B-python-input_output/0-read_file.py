#!/usr/bin/python3
"""A module that that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """Function That reads a txt file"""
    with open(filename, 'r') as f:
        file_read = f.read()
    print(file_read)