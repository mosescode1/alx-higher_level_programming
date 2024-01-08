#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None
    elif idx > (len(my_list) - 1):
        return my_list
    for i in my_list:
        if i == idx:
            my_list[idx] = element
            return my_list
