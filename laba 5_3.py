from scipy.integrate import quad
import numpy as np

# Запрос пользовательского ввода
n = int(input("Введите значение n (целое число): "))
a = float(input("Введите нижнюю границу интегрирования a: "))
b = float(input("Введите верхнюю границу интегрирования b: "))

# Функция, которую нужно интегрировать
def integrand(x):
    if n == 0:
        return x
    elif n == 1:
        return np.log(np.tan(np.pi/4 + x/2))
    else:
        return (1 / (n - 1)) * np.sin(x) / (np.cos(x)(n - 1) + (n - 2) / (n - 1) * (1 / np.cos(x)(n - 2)))

# Вычисление определенного интеграла
result, _ = quad(integrand, a, b)

# Вывод результата
print("Результат вычисления определенного интеграла:", result)