# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

KEY_WAGE = 'wage'
KEY_BONUS = 'bonus'


class Worker:
    name = None
    surname = None
    position = None
    _income = {KEY_WAGE: 0, KEY_BONUS: 0}

    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income[KEY_WAGE] = wage
        self._income[KEY_BONUS] = bonus


# Так как в задани четко не указано что класс должен имено наследоваться от Worker.
# А также в следующих заданиях будет много примеров с наследованием.
# По этому, руководствуясь здравым смыслом будем реализовывать композицию.
# Класс Position будет принимать класс Worker в конструкторе.
class Position:
    worker = None

    def __init__(self, worker):
        self.worker = worker

    def get_full_name(self):
        return self.worker.name + ' ' + self.worker.surname

    def get_total_income(self):
        return self.worker._income[KEY_WAGE] + self.worker._income[KEY_BONUS]


worker = Worker("Ivan", "Ivanov", 5000, 1000)
print(f"Имя: {worker.name}")
print(f"Фамилия: {worker.surname}")
print(f"Доход: {worker._income}")
print()

position = Position(worker)
print(f"Полное имя: {position.get_full_name()}")
print(f"Итоговый доход: {position.get_total_income()}")
