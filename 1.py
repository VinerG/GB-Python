# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

work_hours = float(argv[1])
hour_cost = float(argv[2])
bonus = float(argv[3])

print("Выработка в часах: ", work_hours)
print("Ставка в час: ", hour_cost)
print("Премия: ", bonus)

print("Расчитаная заработная плата: ", work_hours * hour_cost + bonus)
