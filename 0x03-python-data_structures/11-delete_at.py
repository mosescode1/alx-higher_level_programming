#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    for i, index in enumerate(my_list):
        print(i,index)
        if i == idx:
            my_list.remove(my_list[i])
    return my_list
