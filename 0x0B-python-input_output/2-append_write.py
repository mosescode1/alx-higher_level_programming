#!/usr/bin/python3
"""A module that that appends to a text file (UTF8) and returns number of characters added:"""


def append_write(filename="", text=""):
    """Function That appends to a txt file and retun the number of character written"""
    with open(filename, 'a', encoding="UTF8") as append_file:
        data = append_file.write(text)
        return data
