def is_valid_matrix(matrix):
    for row in matrix:
        for cell in row:
            if cell not in ('#', '.'):
                return False
    return True

def count_matrices(matrix):
    if not any('.' in row for row in matrix):
        return 1

    total_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '.':
                # Try placing a '.' at this position
                new_matrix = [list(row) for row in matrix]
                new_matrix[i][j] = '#'
                if is_valid_matrix(new_matrix):
                    total_count += count_matrices(new_matrix)

    return total_count

def main():
    while True:
        try:
            m = int(input("Введите количество строк (m): "))
            n = int(input("Введите количество столбцов (n): "))
            if m <= 0 or n <= 0:
                raise ValueError
            break
        except ValueError:
            print("Пожалуйста, введите положительные целые числа для m и n.")

    matrix = []
    for i in range(m):
        while True:
            row = input(f"Введите строку {i+1} (длиной {n} символов, используйте '#' и '.'): ")
            if len(row) != n:
                print(f"Строка должна содержать ровно {n} символов.")
                continue
            if is_valid_matrix([list(row)]):
                matrix.append(list(row))
                break
            else:
                print("Пожалуйста, используйте только символы '#' и '.'.")

    result = count_matrices(matrix)
    print(f"Количество возможных матриц: {result}")

if __name__ == "__main__":
    main()