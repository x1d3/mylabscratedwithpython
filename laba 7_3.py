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

    key = (store_name, product_name)
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

def main():
    price = {}

    while True:
        print("\nМЕНЮ:")
        print("1. Ввод данных")
        print("2. Просмотр всех данных")
        print("3. Вывод данных по ключу")
        print("4. Удаление данных по ключу")
        print("5. Поиск 1")
        print("6. Выход")

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
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите существующий пункт меню.")

if __name__ == "__main__":
    main()
