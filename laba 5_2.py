def find_arithmetic_progression_elements(a1, d, n):
    elements = []
    for i in range(2, n + 1):
        an = a1 + (i - 1) * d
        elements.append(an)

    return elements


while True:
    try:
        a1 = float(input("Введите первый элемент арифметической прогрессии (a1): "))
        break  # Выход из цикла, если ввод корректен
    except ValueError:
        print("Ошибка: Введите числовое значение для a1.")

while True:
    try:
        d = float(input("Введите разность (d): "))
        break  # Выход из цикла, если ввод корректен
    except ValueError:
        print("Ошибка: Введите числовое значение для d.")

n = 7  # Мы ищем второй, третий, четвертый и седьмой элементы, поэтому n = 7

elements = find_arithmetic_progression_elements(a1, d, n)

print("Второй элемент:", elements[0])
print("Третий элемент:", elements[1])
print("Четвертый элемент:", elements[2])
print("Седьмой элемент:", elements[5])

sum_elements = sum(elements)
print("Сумма найденных элементов:", sum_elements)
"""
15. 	Дана арифметическая прогрессия an,, a1 – первый ее элемент, d – разность. 
 Найти второй, третий, четвертый и седьмой элементы и их сумму. 
"""