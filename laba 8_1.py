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
    output_filename = "output.txt"

    process_file(input_filename, output_filename)
