# Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
# ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell:
    def __init__(self, num):
        self._num = num

    def __str__(self):
        return f"Cell[{self._num}]"

    @property
    def num(self):
        return self._num

    def __add__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(f"Unsupported operand type(s) for +: 'Cell' and '{type(other)}'")
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(f"Unsupported operand type(s) for -: 'Cell' and '{type(other)}'")
        if self.num < other.num:
            raise Exception("Subtraction result cannot be less than 0")
        return Cell(self.num - other.num)

    def __mul__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(f"Unsupported operand type(s) for *: 'Cell' and '{type(other)}'")
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(f"Unsupported operand type(s) for /: 'Cell' and '{type(other)}'")
        # Будет порождено исключение "ZeroDivisionError: division by zero" чего вполне достаточно.
        # Нет необходимости делать дополнительную проверку деления на 0.
        return Cell(self.num % other.num)

    def make_order(self, cell_per_line):
        s = ""
        cell_in_line = 0
        count = self.num
        while count > 0:
            if cell_in_line == cell_per_line:
                s += '\n'
                cell_in_line = 0
            s += '*'
            cell_in_line += 1
            count -= 1
        return s

cell_1 = Cell(10)
cell_2 = Cell(4)
print(f"cell_1 = {cell_1}")
print(cell_1.make_order(4))
print(f"cell_2 = {cell_2}")
print(cell_2.make_order(3))
print(f"{cell_1} + {cell_2} = {cell_1 + cell_2}")
print(f"{cell_1} - {cell_2} = {cell_1 - cell_2}")
print(f"{cell_1} * {cell_2} = {cell_1 * cell_2}")
print(f"{cell_1} / {cell_2} = {cell_1 / cell_2}")
