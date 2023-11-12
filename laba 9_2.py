import random
import numpy as np

def generate_random_matrix(rows, cols):
    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

def flatten_matrix(matrix):
    return [element for row in matrix for element in row]

def sort_matrix_with_functions(matrix):
    flattened_matrix = flatten_matrix(matrix)
    sorted_flattened_matrix = sorted(flattened_matrix)
    sorted_matrix = [sorted_flattened_matrix[i:i+len(matrix[0])] for i in range(0, len(sorted_flattened_matrix), len(matrix[0]))]
    return sorted_matrix

def sort_matrix_without_functions(matrix):
    flattened_matrix = flatten_matrix(matrix)
    for i in range(len(flattened_matrix)):
        for j in range(0, len(flattened_matrix)-i-1):
            if flattened_matrix[j] > flattened_matrix[j+1]:
                flattened_matrix[j], flattened_matrix[j+1] = flattened_matrix[j+1], flattened_matrix[j]
    sorted_matrix = [flattened_matrix[i:i+len(matrix[0])] for i in range(0, len(flattened_matrix), len(matrix[0]))]
    return sorted_matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

if __name__ == "__main__":
    rows = int(input("Введите количество строк в матрице: "))
    cols = int(input("Введите количество столбцов в матрице: "))

    matrix = generate_random_matrix(rows, cols)

    print("Исходная матрица:")
    print_matrix(matrix)

    # Сортировка с использованием функций
    sorted_matrix_with_functions = sort_matrix_with_functions(matrix)
    print("\nСортировка с использованием функций:")
    print_matrix(sorted_matrix_with_functions)

    # Сортировка без использования функций
    sorted_matrix_without_functions = sort_matrix_without_functions(matrix)
    print("\nСортировка без использования функций:")
    print_matrix(sorted_matrix_without_functions)
