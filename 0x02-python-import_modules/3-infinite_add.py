#!/usr/bin/python3
import sys
if __name__ == "__main__":
    my_add_num = sys.argv[1:]
    my_new_sum = 0
    for i in my_add_num:
        my_sum = int(i)
        my_new_sum += my_sum
    print(my_new_sum)
