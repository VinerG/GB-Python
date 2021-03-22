# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего
# дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    _length = 0
    _width = 0

    def __init__(self, length_m, width_m):
        self._length = length_m
        self._width = width_m

    def get_mass(self, height_cm, mass_per_mm_cm):
        return self._length * self._width * height_cm * mass_per_mm_cm / 1000


road = Road(length_m=5000, width_m=20)
print(road.get_mass(height_cm=5, mass_per_mm_cm=25), 'т')
