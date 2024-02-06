#!/usr/bin/python3
"""A module that that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """Function That reads a txt file"""
    with open(filename, 'r+', encoding="UTF8") as f:
        for line in f:
            print(line, end="")
        print()