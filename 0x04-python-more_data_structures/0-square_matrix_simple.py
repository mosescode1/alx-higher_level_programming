#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []

    for rows in matrix:
        new_rows = []
        for value in rows:
            new_rows.append(value ** 2)
        res.append(new_rows)
    return res
