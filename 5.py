# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random
import functools

with open("text_5.txt", "w+", encoding="utf-8") as f_obj:
    f_obj.write(" ".join([str(random.randint(1, 99)) for el in range(200)]))
    f_obj.seek(0)
    t = functools.reduce(lambda el_1, el_2: el_1 + el_2, map(int, f_obj.read().split()))
print(t)
