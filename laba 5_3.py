import sympy as sp

def integral_recursive(x, n, a, b):
    if n == 0:
        return x
    elif n == 1:
        return sp.log(sp.tan(sp.pi/4 + x/2))
    else:
        return -1/(n-1) * sp.sin(x)/sp.cos(x)**(n-1) + (n-2)/(n-1) * integral_recursive(x, n-2, a, b)

# Переменная интегрирования
x = sp.symbols('x')

# Ввод пользователя с проверкой
while True:
    try:
        n = int(input("Введите значение n (целое число >= 0): "))
        if n < 0:
            print("Пожалуйста, введите неотрицательное число.")
        else:
            break
    except ValueError:
        print("Пожалуйста, введите целое число.")

# Заданные границы интегрирования
a = 0
b = sp.pi/2

# Символьное вычисление интеграла
integral_expr = integral_recursive(x, n, a, b)

# Вычисление значения интеграла
result = sp.integrate(integral_expr, (x, a, b))

print(f"Значение интеграла: {result.evalf()}")
