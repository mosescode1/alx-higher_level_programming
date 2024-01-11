#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for item, values in sorted(a_dictionary.items()):
        print(f"{item}: {values}")
