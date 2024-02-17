#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for _ in range(len(matrix)):
        row = []
        for _ in range(len(matrix[0])):
            row.append(0)
        new_matrix.append(row)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_matrix[i][j] = matrix[i][j] ** 2
    return (new_matrix)



