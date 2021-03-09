# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

MONTH_NAMES = ("Январь",
               "Февраль",
               "Март",
               "Апрель",
               "Май",
               "Июнь",
               "Июль",
               "Август",
               "Сентябрь",
               "Октябрь",
               "Ноябрь",
               "Декабрь")

SEASON_WINTER = "Зима"
SEASON_SPRING = "Весна"
SEASON_SUMMER = "Лето"
SEASON_AUTUMN = "Осень"

SEASON_NAMES = (SEASON_WINTER, SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN)

season_months = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 0]
season_dict = {12: SEASON_WINTER, 1: SEASON_WINTER, 2: SEASON_WINTER,
               3: SEASON_SPRING, 4: SEASON_SPRING, 5: SEASON_SPRING,
               6: SEASON_SUMMER, 7: SEASON_SUMMER, 8: SEASON_SUMMER,
               9: SEASON_AUTUMN, 10: SEASON_AUTUMN, 11: SEASON_AUTUMN}
season_dict_2 = {SEASON_WINTER: (12, 1, 2),
                 SEASON_SPRING: (3, 4, 5),
                 SEASON_SUMMER: (6, 7, 8),
                 SEASON_AUTUMN: (9, 10, 11)}

month = int(input("Введите номер месяца от 1 до 12: "))
if 1 <= month <= 12:
    print(MONTH_NAMES[month - 1])
    print("Используя List:", SEASON_NAMES[season_months[month - 1]])
    print("Используя Dict:", season_dict.get(month))

    for season, months in season_dict_2.items():
        if months.count(month) > 0:
            print("Используя Dict2:", season)
            break
else:
    print("Неверный номер месяца.")
