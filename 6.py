# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

ITEM_NAME = "название"
ITEM_PRICE = "цена"
ITEM_QTY = "количество"
ITEM_UNIT = "eд"

data = []

while True:
    # Грязный способ очистить консоль - выводим 100 пустых строк
    print("\n" * 100)

    print("Товары:")
    # print(data)
    print("[")
    for data_item in data:
        print(f"  {data_item},")
    print("]")

    print("\n1 - Добавить новый товар")
    print("2 - Заполнить словарь данными из примера")
    print("3 - Вывести аналитику")
    print("0 - Завершить работу")
    try:
        command = int(input("Выберите действие: "))
    except ValueError:
        continue

    if command == 0:
        break
    elif command == 1:
        # Добавление нового товара
        print("Добавление нового товара")
        # небольшое отступление от задания - номер будем генерировать инкрементально
        item_number = len(data) + 1
        item_name = input("  Введите название: ")
        item_price = int(input("  Введите цену: "))
        item_qty = int(input("  Введите количество: "))
        item_unit = input("  Введите единицу измерения: ")
        data.append((item_number, {ITEM_NAME: item_name,
                                   ITEM_PRICE: item_price,
                                   ITEM_QTY: item_qty,
                                   ITEM_UNIT: item_unit}))
    elif command == 2:
        data.clear()
        data.append((1, {ITEM_NAME: "компьютер",
                         ITEM_PRICE: 20000,
                         ITEM_QTY: 5,
                         ITEM_UNIT: "шт."}))
        data.append((2, {ITEM_NAME: "принтер",
                         ITEM_PRICE: 6000,
                         ITEM_QTY: 2,
                         ITEM_UNIT: "шт."}))
        data.append((3, {ITEM_NAME: "сканер",
                         ITEM_PRICE: 2000,
                         ITEM_QTY: 7,
                         ITEM_UNIT: "шт."}))
    elif command == 3:
        print("\nАналитика о товарах")
        # Уникальные значения собираются через множества.
        # Соответственно, порядок может не совпадать с примером.
        # Далее множества преобразуются в списки, для соответствия примеру.
        unique_item_names = set()
        unique_item_prices = set()
        unique_items_qty = set()
        unique_items_units = set()
        for item in data:
            unique_item_names.add(item[1].get(ITEM_NAME))
            unique_item_prices.add(item[1].get(ITEM_PRICE))
            unique_items_qty.add(item[1].get(ITEM_QTY))
            unique_items_units.add(item[1].get(ITEM_UNIT))

        data_statistics = {ITEM_NAME: list(unique_item_names),
                           ITEM_PRICE: list(unique_item_prices),
                           ITEM_QTY: list(unique_items_qty),
                           ITEM_UNIT: list(unique_items_units)}

        # print(data_statistics)
        print("{")
        for key, value in data_statistics.items():
            print(f'  "{key}": {value}')
        print("}")
        input("\nНажмите ENTER для продолжения.")
