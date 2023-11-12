import math


def calculate_gcd(a, b):
    """Вычисление НОД двух чисел"""
    return math.gcd(a, b)


def process_files(input_filename0, input_filename1, output_filename):
    """Обработка файлов"""
    with open(input_filename0, 'r') as file0, open(input_filename1, 'r') as file1:
        lines0 = file0.readlines()
        lines1 = file1.readlines()

    with open(output_filename, 'w') as output_file:
        for line0, line1 in zip(lines0, lines1):
            # Преобразование строк в списки чисел
            numbers0 = [int(x) for x in line0.strip().split()]
            numbers1 = [int(x) for x in line1.strip().split()]

            # Вычисление НОД для каждой пары чисел
            gcd_results = [calculate_gcd(a, b) for a, b in zip(numbers0, numbers1)]

            # Запись результатов в файл
            output_file.write(" ".join(map(str, gcd_results)) + "\n")


if __name__ == "__main__":
    input_filename0 = "input0.txt"
    input_filename1 = "input1.txt"
    output_filename = "output8_2.txt"

    process_files(input_filename0, input_filename1, output_filename)
