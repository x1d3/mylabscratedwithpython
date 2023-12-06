def arithmetic_progression(a1, d, n):
    # Функция для вычисления n-го элемента арифметической прогрессии по формуле an = a1 + (n-1)*d
    return a1 + (n - 1) * d

def calculate_progression_elements(a1, d):
    # Вычисление второго, третьего, четвертого и седьмого элементов
    elements = [arithmetic_progression(a1, d, i) for i in range(2, 8) if i != 5 if i != 6]
    return elements

def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите числовое значение.")

# Входные данные с проверкой ввода
a1 = get_valid_input("Введите первый элемент прогрессии (a1): ")
d = get_valid_input("Введите разность прогрессии (d): ")

# Вычисление элементов с использованием функции
progression_elements = calculate_progression_elements(a1, d)

# Вычисление суммы элементов
sum_of_elements = sum(progression_elements)

# Вывод результатов
print("Элементы прогрессии:", progression_elements)
print(f"Сумма элементов: {sum_of_elements}")


"""
15. 	Дана арифметическая прогрессия an,, a1 – первый ее элемент, d – разность. 
 Найти второй, третий, четвертый и седьмой элементы и их сумму. 
"""
