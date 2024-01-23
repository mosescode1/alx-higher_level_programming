#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    listing = []
    i = 0
    try:
        listing = my_list[:x]
        for element in listing:
            
            if isinstance(element, int):
               print("{:d}".format(element), end="")
               i += 1
        print()
        return i
    except IndexError as e:
        return e
