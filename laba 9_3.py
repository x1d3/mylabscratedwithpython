def guess_number():
    low_limit = -1024
    high_limit = 1024
    attempts = 0

    print(f"Загадайте число от {low_limit} до {high_limit}.")

    while True:
        guess = (low_limit + high_limit) // 2
        print(f"Компьютер предполагает: {guess}")
        response = input("Введите '+++' если число угадано, '-' если оно меньше, или '+' если оно больше: ")
        attempts += 1

        if response == '+++':
            print(f"Компьютер угадал число {guess} за {attempts} попыток.")
            break
        elif response == '-':
            high_limit = guess - 1
        elif response == '+':
            low_limit = guess + 1
        else:
            print("Некорректный ввод. Введите '+', '-', или '='.")


if __name__ == "__main__":
    guess_number()
