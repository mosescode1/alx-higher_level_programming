#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    listing = my_list[:x]
    i = 0
    try:
        for _ in listing:
            i += 1
        print("".join(map(str,listing)))
        return i
    except Exception as e:
        pass
