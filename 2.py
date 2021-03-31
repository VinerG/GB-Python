# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    if b == 0:
        raise MyZeroDivisionError("Деление на ноль!")
    print(f"{a} / {b} = {a / b}")
except (ValueError, MyZeroDivisionError) as err:
    print(err)
