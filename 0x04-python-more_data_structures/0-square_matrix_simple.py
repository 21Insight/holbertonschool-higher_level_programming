#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = matrix.copy()

    for n in range(len(matrix)):
        n_matrix[n] = list(map(lambda X: X**2, matrix[n]))

    return(n_matrix)
