def calculate_average_and_transform_array():
    while True:
        try:
            # Ввод размера массива
            n = int(input("Введите размер массива: "))

            # Ввод элементов массива
            array = []
            for i in range(n):
                while True:
                    try:
                        element = float(input(f"Введите элемент {i + 1}: "))
                        array.append(element)
                        break  # Выход из цикла в случае успешного ввода элемента
                    except ValueError:
                        print("Ошибка: Введите число для элемента.")

            # Найти среднее арифметическое значение элементов массива
            total = sum(array)
            average = total / n

            # Преобразовать исходный массив
            for i in range(n):
                array[i] -= average

            # Вывести среднее значение
            print("Среднее значение:", average)

            # Вывести преобразованный массив
            print("Преобразованный массив:", array)

            break  # Выход из цикла в случае успешного ввода
        except ValueError:
            print("Ошибка: Введите целое число для размера массива.")


calculate_average_and_transform_array()
"""
15.	Найти среднее арифметическое значение 
элементов заданного массива. Преобразовать исходный массив, вычитая из каждого элемента среднее значение.
"""