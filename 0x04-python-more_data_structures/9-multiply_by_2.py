#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for keys, value in sorted(a_dictionary.items()):
        new_dic[keys] = value * 2
    return new_dic
