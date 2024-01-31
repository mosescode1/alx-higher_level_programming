#!/usr/bin/python3
"""This Module That prints out the first name and last name
    Args:
        first_name(string): parameter first name
        last_name(string): parameter last_name
    """
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        print(char,end="")
        if char in [".", "?", ":"]:
            print("\n\n", end="")
