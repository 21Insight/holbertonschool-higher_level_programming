#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda X: list(map(lambda Y: Y**2, X)), matrix)))
