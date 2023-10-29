from math import sqrt

def main():
    while True:
        try:
            x = float(input("Введите значение x = "))

            if -7 <= x < -6:
                y = 1
                print(f"y = {y:.3f}")
            elif -6 <= x < -4:
                y = -0.5 * x - 2
                print(f"y = {y:.3f}")
            elif -4 <= x < 0:
                y = sqrt(4 - (x + 2)**2)  # для верхней полуплоскости
                print(f"y = {y:.3f}")
            elif 0 <= x <= 2:
                y = -sqrt(1 - (x - 1)**2)  # для нижней полуплоскости
                print(f"y = {y:.3f}")
            elif 2 <= x <= 3:
                y = -x + 2
                print(f"y = {y:.3f}")
            else:
                print("Вы ввели значение x вне допустимого диапазона!")
                continue  # Перезапуск цикла для нового ввода
        except ValueError:
            print("Вы ввели некорректное значение x. Пожалуйста, введите число.")
            continue  # Перезапуск цикла для нового ввода

if __name__ == "__main__":
    main()