# Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

# Вариант 1
def format_user_info_1(**kwargs):
    return " ".join(kwargs.values())


# Вариант 2
def format_user_info_2(**kwargs):
    result = ""
    for key, value in kwargs.items():
        result = result + f"{key}:{value}, "
    return result[:-2]


# Вариант 3
def format_user_info_3(name, **kwargs):
    atr_list = [kwargs.get("surname"),
                kwargs.get("birth_year"),
                kwargs.get("living_city"),
                kwargs.get("email"),
                kwargs.get("phone_number")]
    res = []
    for val in atr_list:
        if not(val is None):
            res.append(val)

    result = name
    if len(res) != 0:
        result = result + " " + " ".join(res)
    return result


# Вариант 4
def format_user_info_4(name, surname=None, birth_year=None, living_city=None, email=None, phone_number=None):
    """ Function unite user info into single string """
    return (name +
            ('' if surname is None else ' ' + surname) +
            ('' if birth_year is None else ' born in ' + birth_year) +
            ('' if living_city is None else ' lives in ' + living_city) +
            ('' if email is None else ' contact email ' + email) +
            ('' if phone_number is None else ' contact phone ' + phone_number))


print(format_user_info_1(name="Ivan",
                         surname="Ivanov",
                         birth_year="1980",
                         living_city="Moscow",
                         email="ivanov@mail.ru",
                         phone_number="(489)99493"))

print(format_user_info_2(name="Ivan",
                         surname="Ivanov",
                         birth_year="1980"))

print(format_user_info_3(name="Ivan",
                         living_city="Moscow",
                         email="ivanov@mail.ru",
                         phone_number="(489)99493"))

print(format_user_info_4(name="Ivan",
                         surname="Ivanov",
                         birth_year="1980",
                         living_city="Moscow",
                         email="ivanov@mail.ru",
                         phone_number="(489)99493"))
