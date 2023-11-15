import math

def input_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Пожалуйста, введите положительное число.")
            else:
                return value
        except ValueError:
            print("Пожалуйста, введите числовое значение.")

def input_coordinate(prompt):
    while True:
        value = input(prompt)
        if value.replace(".", "").replace("-", "").isdigit():  
            return float(value)
        else:
            print("Пожалуйста, введите числовое значение для координаты.")


a1 = input_coordinate("Введите координату a1: ")
a2 = input_coordinate("Введите координату a2: ")


radius = input_positive_float("Введите радиус окружности: ")

distance = math.sqrt(a1**2 + a2**2)

if distance <= radius:
    print(f"Точка A({a1}, {a2}) попадает в окружность с радиусом {radius}.")
else:
    print(f"Точка A({a1}, {a2}) не попадает в окружность с радиусом {radius}.")

"""
15.	Попадёт ли точка А(a1, a2) в окружность заданного радиуса с центром в начале координат?
"""
