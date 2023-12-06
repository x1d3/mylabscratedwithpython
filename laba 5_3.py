import math

def integral_value(x, n):
    if n == 0:
        return x
    elif n == 1:
        if math.cos(math.pi/4 + x/2) == 0:
            raise ValueError("Значение внутри тангенса вызывает деление на ноль. Измените ваши границы.")
        return math.log(math.tan(math.pi/4 + x/2))
    elif n > 1:
        if math.cos(x)**(n-1) == 0:
            raise ValueError("Значение внутри косинуса вызывает деление на ноль. Измените ваши границы.")
        return recursive_integral_value(x, n)
    else:
        raise ValueError("Введите значение n, равное нулю или больше.")

def recursive_integral_value(x, n):
    if n == 0:
        return x
    elif n == 1:
        return math.log(math.tan(math.pi/4 + x/2))
    else:
        if math.cos(x)**(n-1) == 0:
            raise ValueError("Значение внутри косинуса вызывает деление на ноль. Измените ваши границы.")
        first_equation = (1/(n-1)) * math.sin(x)/math.cos(x)**(n-1)
        second_equation = (n-2)/(n-1) * recursive_integral_value(x, n-2)
        return first_equation + second_equation

def main():
    while True:
        try:
            n = int(input("Введите значение n: "))
            if n < 0:
                raise ValueError("Введите значение n, равное нулю или больше.")
            a = float(input("Введите значение a: "))
            b = float(input("Введите значение b: "))
            break  # Прерываем цикл, если ввод корректен
        except ValueError as e:
            print(f"Ошибка ввода: {e}")

    try:
        result_a = integral_value(a, n)
        result_b = integral_value(b, n)
        print(f"Значение интеграла от {a} до {b} для n = {n} равно: {result_b - result_a}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
