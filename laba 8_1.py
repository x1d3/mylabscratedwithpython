import re

def calculate_expression(expression):
    """Вычисление результата математического выражения"""
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Ошибка вычисления: {str(e)}"

def process_file(input_filename, output_filename):
    """Обработка файла"""
    with open(input_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        for line in lines:
            # Поиск арифметического выражения в строке
            match = re.search(r'\d+\s*[\+\-\*/]\s*\d+', line)
            if match:
                expression = match.group()
                # Вычисление результата
                result = calculate_expression(expression)
                # Вывод результата на экран
                print(f"{expression} = {result}")
                # Запись результата в файл
                output_file.write(f"{expression} = {result}\n")
            else:
                print("Арифметическое выражение отсутствует.")

if __name__ == "__main__":
    input_filename = "input.txt"
    output_filename = "output8_1.txt"

    process_file(input_filename, output_filename)

    """
1.	Создать в Блокноте следующий текстовый файл:
У меня спросили: сколько будет x Опер y ? 
А я не знаю! А n Опер k ? Тоже!
Помогите!
Например:
У меня спросили: сколько будет 7 * 2 ? 
А я не знаю! А 9 / 4 ? Тоже!
Помогите!
2.	Вам известна структура файла. Вывести содержимое файла на экран, 
а в выходной файл записать результаты:
x Опер y = Рез1
n Опер k = Рез2
Например:
7 * 2 = 14
9 / 4 = 2.25
В нашем случае задание выглядит так: 18 * 4 7 + 55
    """
