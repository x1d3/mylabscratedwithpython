import math

# Функция для определения расстояния между двумя точками
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Ввод радиуса окружности
while True:
    try:
        r = float(input("Введите радиус окружности: "))
        break
    except ValueError:
        print("Ошибка: Введите числовое значение радиуса.")

# Ввод количества точек
while True:
    try:
        n = int(input("Введите количество точек: "))
        break
    except ValueError:
        print("Ошибка: Введите целое число для количества точек.")

# Инициализация счетчика пересекающихся окружностей
count = 0

# Цикл для ввода координат и проверки пересечения
for i in range(n):
    while True:
        try:
            x, y = map(float, input(f"Введите координаты точки {i + 1} (x y): ").split())
            break
        except ValueError:
            print("Ошибка: Введите числовые значения координат точки.")

    # Вычисление расстояния между центрами окружностей
    d = distance(0, 0, x, y)

    # Если расстояние меньше чем 2 * r, то окружности пересекаются
    if d < 2 * r:
        count += 1

# Вывод результата
print(f"Из {n} окружностей {count} пересекают данную окружность.")