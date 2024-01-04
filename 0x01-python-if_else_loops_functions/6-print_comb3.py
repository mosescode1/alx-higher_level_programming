#!/usr/bin/python3
for a in range(0, 10):
    for y in range(a + 1, 10):
        if a == 8 and y == 9:
            print('89')
        else:
            print('{}{}, '.format(a, y), end='')
