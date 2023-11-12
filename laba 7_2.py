def main():
    set1 = set()
    set2 = set()
    set3 = set()

    # a) Ввод чисел и сохранение их в соответствующих множествах
    try:
        set1.add(input("Введите строку для первого множества: "))
        set2.add(input("Введите строку для второго множества: "))
        set3.add(input("Введите строку для третьего множества: "))
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите корректные данные.")

    # Вывод данных множеств
    print("\nМножество 1:", set1)
    print("Множество 2:", set2)
    print("Множество 3:", set3)

    # б) Нахождение множества строк, состоящих не только из строчных английских букв, заканчивающихся на «xyz» и длиной 4
    result_b = {string for string in set1 | set2 | set3 if string.isalpha() and string.endswith('xyz') and len(string) == 4}
    print("\nМножество строк, соответствующих условиям б):", result_b)

    # в) Нахождение самой короткой строки, состоящей только из строчных английских букв, не заканчивающихся на «xyz» и не длины 4
    result_c = min({string for string in set1 | set2 | set3 if string.isalpha() and not string.endswith('xyz') and len(string) != 4}, key=len, default=None)
    print("\nСамая короткая строка, соответствующая условиям в):", result_c)


if __name__ == "__main__":
    main()
