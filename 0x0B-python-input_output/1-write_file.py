#!/usr/bin/python3
"""A module that that reads a text file (UTF8) and prints it to stdout:"""


def write_file(filename="", text=""):
    """Function That write to a txt file and retun the number of character written"""
    with open(filename, 'w', encoding="UTF8") as write_file:
        data = write_file.write(text)
        return data
