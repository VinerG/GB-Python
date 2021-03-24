# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def calc_material_count(self):
        pass


class Coat(Clothes):

    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    def __str__(self):
        return f"{self.name} размера {self.v}"

    def calc_material_count(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    def __str__(self):
        return f"{self.name} роста {self.h}"

    def calc_material_count(self):
        return self.h * 2 + 0.3


coat = Coat("Пальто жаккард", 52)
suit = Suit("Костюм элегант", 182)

print(f"{coat}. Расхода ткани {coat.calc_material_count()}")
print(f"{suit}. Расхода ткани {suit.calc_material_count()}")
