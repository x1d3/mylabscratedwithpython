def number_to_words(c):
    # Проверка на допустимый диапазон
    if c < 0 or c > 7:
        return "Число не входит в диапазон 0-7"

    # Словарь для числовых представлений
    words = {
        0: "ноль",
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь"
    }

    # Преобразование числа в словесную форму
    word_representation = words[c]

    return word_representation


while True:
    try:
        c = int(input("Введите число от 0 до 7: "))
        if 0 <= c <= 7:
            result = number_to_words(c)
            print("Словесное представление числа:", result)
            break  # Выход из цикла, если ввод корректен
        else:
            print("Ошибка: Число должно быть в диапазоне от 0 до 7.")
    except ValueError:
        print("Ошибка: Введите целое число.")