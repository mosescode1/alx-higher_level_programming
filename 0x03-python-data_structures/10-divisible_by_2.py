#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    new_list = []

    for num in my_list:

        divisible_2 = num % 2 == 0

        new_list.append(divisible_2)

    return new_list
