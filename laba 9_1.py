import random

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка! Введите целое число.")

def find_indices_in_list(element, input_list):
    indices = []

    for i, el in enumerate(input_list):
        if el == element:
            indices.append(i)

    return indices

def find_indices_in_matrix(element, matrix):
    indices = []

    for i, row in enumerate(matrix):
        for j, el in enumerate(row):
            if el == element:
                indices.append((i, j))

    return indices

def generate_random_matrix(rows, cols):
    return [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

if __name__ == "__main__":
    # Запрашиваем размеры матрицы
    rows = get_integer_input("Введите количество строк в матрице: ")
    cols = get_integer_input("Введите количество столбцов в матрице: ")

    # Генерируем случайную матрицу
    matrix = generate_random_matrix(rows, cols)

    # Выводим матрицу
    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)

    # Запрашиваем элемент для поиска
    element_to_find = get_integer_input("Введите элемент для поиска: ")

    # Ищем индексы элемента в списке и матрице
    flattened_matrix = [element for row in matrix for element in row]
    indices_in_list = find_indices_in_list(element_to_find, flattened_matrix)
    indices_in_matrix = find_indices_in_matrix(element_to_find, matrix)

    # Выводим результат
    if indices_in_list:
        print(f"Индексы элемента {element_to_find} в списке: {indices_in_list}")
    else:
        print(f"Элемент {element_to_find} не найден в списке.")

    if indices_in_matrix:
        print(f"Индексы элемента {element_to_find} в матрице: {indices_in_matrix}")
    else:
        print(f"Элемент {element_to_find} не найден в матрице.")
"""
Реализуйте поиск индекса элемента в списке и в матрице (i, j)
двумя мето-дами, используя встроенные функции и методы, представленные в 9.8., а также не используя их.
"""