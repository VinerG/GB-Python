#  Реализуйте базовый класс Car.
#  У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
#  остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#  Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#  Для классов TownCar и WorkCar переопределите метод show_speed.
#  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

import random


class Car:
    speed = None
    color = None
    name = None
    is_police = None
    _is_go = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{str(self.color).title()} {self.name} поехала.")
        self._is_go = True

    def stop(self):
        print(f"{str(self.color).title()} {self.name} остановилась.")
        self._is_go = False

    def turn(self, direction):
        print(f"{str(self.color).title()} {self.name} повернула {direction}.")

    def show_speed(self):
        if self._is_go:
            print(f'{str(self.color).title()} {self.name} едет со скоростью {self.speed} км/ч.')
        else:
            print(f"{str(self.color).title()} {self.name} стоит.")


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self._is_go and self.speed > 60:
            print("Превышении скорости!!! ", end='')
        super().show_speed()


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self._is_go and self.speed > 40:
            print("Превышении скорости!!! ", end='')
        super().show_speed()


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


car_list = [TownCar(name="городская машина", color="синяя", speed=55),
            SportCar(name="спортивная машина", color="красная", speed=200),
            WorkCar(name="городская машина", color="синяя", speed=50),
            PoliceCar(name="полицейская машина", color="белая", speed=120)]

turn_directions = ("на лево", "на право", "назад")

for car in car_list:
    print("-" * 80)
    print(f"Название: {car.name}")
    print(f"Цвет: {car.color}")
    print(f"Скорость: {car.speed}")
    print(f"Полицейская: {'Да' if car.is_police else 'Нет'}")
    print()
    car.go()
    car.show_speed()
    car.turn(turn_directions[random.randint(0, len(turn_directions) - 1)])
    car.stop()
    car.show_speed()
