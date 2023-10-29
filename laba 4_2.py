import math

def control_function(x):
    return -math.log(2 * math.sin(x / 2))

def calculate_series(x, eps):
    n = 1
    S = 0
    term = math.cos(x)  # Первый член ряда

    while abs(term) >= eps:
        S += term
        n += 1
        term = math.cos(n * x) / n

    return S

x = math.pi
eps = 0.0001
y = control_function(x)
S = calculate_series(x, eps)

print(f"Значение контрольной функции y: {y:.4f}")
print(f"Сумма ряда S с точностью {eps:.4f}: {S:.4f}")