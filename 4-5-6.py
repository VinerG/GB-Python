# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

from abc import ABC


class StoreHouseQtyException(Exception):
    def __init__(self, txt):
        self.txt = txt


class StoreHouse:
    def __init__(self):
        self._items = dict()

    def __str__(self):
        s = '['
        for item, qty in self._items.items():
            s = s + f"'{item}' = {qty}, "
        s = s.rstrip(", ") + ']'
        return s

    def add(self, item, qty):
        if not isinstance(item, StoreItem):
            raise TypeError(f"Item must be StoreItem class object")
        if type(qty) != int or qty <= 0:
            raise TypeError(f"Quantity must be positive int value")
        store_qty = self._items.get(item, 0)
        self._items[item] = store_qty + qty

    def remove(self, item, qty):
        if not isinstance(item, StoreItem):
            raise TypeError(f"Item must be StoreItem class object")
        if type(qty) != int or qty <= 0:
            raise TypeError(f"Quantity must be positive int value")

        store_qty = self._items.get(item, 0)
        if store_qty < qty:
            raise StoreHouseQtyException(f"Не достаточное количество.")
        elif store_qty == qty:
            self._items.pop(item)
        else:
            self._items[item] = store_qty - qty


class StoreItem(ABC):

    def __init__(self, type_name, name):
        self.type_name = type_name
        self.name = name

    def __str__(self):
        return self.type_name + " " + self.name


class StoreItemPrinter(StoreItem):
    def __init__(self, name):
        super().__init__("Принтер", name)


class StoreItemMonitor(StoreItem):
    def __init__(self, name, size):
        super().__init__("Монитор", name)
        self.size = size

    def __str__(self):
        return super().__str__() + f" диагональ {self.size}\""


class StoreItemHDD(StoreItem):
    def __init__(self, name, capacity):
        super().__init__("Жесткий диск", name)
        self.capacity = capacity

    def __str__(self):
        return super().__str__() + f" объем {self.capacity} Gb"

try:
    storage = StoreHouse()
    print(storage)

    item_printer = StoreItem("Принтер", "HP LaserJey")
    item_monitor = StoreItemMonitor("Samsung H124f", 24)
    item_hdd_wd = StoreItemHDD("WD Red", 1000)
    item_hdd_seagete = StoreItemHDD("Seagate IronWolf", 2000)
    storage.add(item_printer, 3)
    storage.add(item_monitor, 5)
    storage.add(item_hdd_wd, 10)
    storage.add(item_hdd_seagete, 7)
    print(storage)

    storage.add(item_printer, 2)
    storage.remove(item_monitor, 4)
    storage.remove(item_hdd_wd, 10)
    print(storage)

    storage.remove(item_hdd_seagete, 10)
    print(storage)

except StoreHouseQtyException as err:
    print(err)
