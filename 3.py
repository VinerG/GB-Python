# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    if a < b and a < c:
        return b + c
    elif b < a and b < c:
        return a + c
    else:
        return a + b


def my_func_2(a, b, c):
    return a + b + c - min((a, b, c))


print(my_func(1, 2, 3))
print(my_func_2(1, 2, 3))
