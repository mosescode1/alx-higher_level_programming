#!/usr/bin/python3
"""A module that that write a text file (UTF8) and return nuber of character written:"""


def write_file(filename="", text=""):
    """Function That write to a txt file and retun the number of character written"""
    with open(filename, 'w', encoding="UTF8") as write_file:
        data = write_file.write(text)
        return data
