import json

def add_data(price):
    """Добавление данных в словарь"""
    store_name = input("Введите наименование магазина: ")
    product_name = input("Введите наименование товара: ")

    # Защита ввода для количества товара
    while True:
        try:
            quantity = int(input("Введите количество товара на складе: "))
            break
        except ValueError:
            print("Ошибка! Введите целое число для количества товара.")

    # Защита ввода для стоимости товара
    while True:
        try:
            cost = float(input("Введите стоимость товара: "))
            break
        except ValueError:
            print("Ошибка! Введите число для стоимости товара.")

    key = f"{store_name}_{product_name}"  # Используем строку в качестве ключа
    value = {
        'store_name': store_name,
        'product_name': product_name,
        'quantity': quantity,
        'cost': cost
    }

    price[key] = value
    print("Данные успешно добавлены!")

def view_all_data(price):
    """Просмотр всех данных в словаре"""
    for key, value in price.items():
        print(f"Ключ: {key}, Значение: {value}")

def view_data_by_key(price, search_key):
    """Вывод данных по ключу"""
    if search_key in price:
        print(f"Найденные данные по ключу {search_key}: {price[search_key]}")
    else:
        print("Данные не найдены.")

def delete_data_by_key(price, search_key):
    """Удаление данных по ключу"""
    if search_key in price:
        del price[search_key]
        print(f"Данные по ключу {search_key} успешно удалены.")
    else:
        print("Данные не найдены.")

def search_data_by_name_and_cost(price):
    """Поиск информации о магазинах и товарах по заданным критериям"""
    product_name = input("Введите название товара для поиска: ")
    max_cost = float(input("Введите максимальную стоимость товара: "))

    found_data = [(key, value) for key, value in price.items() if
                  value['product_name'] == product_name and value['cost'] <= max_cost]

    if found_data:
        print("Найденные данные:")
        for key, value in found_data:
            print(f"Ключ: {key}, Значение: {value}")
    else:
        print("Данные не найдены.")

def save_to_file(data, filename):
    """Сохранение данных в файл"""
    converted_data = {str(key): value for key, value in data.items()}
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(converted_data, file, ensure_ascii=False, indent=2)
    print("Данные успешно сохранены в файл.")

def load_from_file(filename):
    """Загрузка данных из файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        converted_data = {tuple(key.split('_')): value for key, value in data.items()}
        print("Данные успешно загружены из файла.")
        return converted_data
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return {}
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {filename}.")
        return {}

def main():
    price = {}
    filename = "price_data.json"

    while True:
        print("\nМЕНЮ:")
        print("1. Ввод данных")
        print("2. Просмотр всех данных")
        print("3. Вывод данных по ключу")
        print("4. Удаление данных по ключу")
        print("5. Поиск 1")
        print("6. Сохранение данных в файл")
        print("7. Загрузка данных из файла")
        print("8. Выход")

        choice = input("Выберите действие (введите номер): ")

        if choice == '1':
            add_data(price)
        elif choice == '2':
            view_all_data(price)
        elif choice == '3':
            search_key_input = input("Введите ключ в формате (наименование магазина, наименование товара): ")
            search_key = tuple(search_key_input.split(', '))
            view_data_by_key(price, search_key)
        elif choice == '4':
            search_key_input = input("Введите ключ в формате (наименование магазина, наименование товара): ")
            search_key = tuple(search_key_input.split(', '))
            delete_data_by_key(price, search_key)
        elif choice == '5':
            search_data_by_name_and_cost(price)
        elif choice == '6':
            save_to_file(price, filename)
        elif choice == '7':
            price = load_from_file(filename)
        elif choice == '8':
            save_to_file(price, filename)
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите существующий пункт меню.")

if __name__ == "__main__":
    main()
