# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("text_3.txt", "r", encoding="utf-8") as f_obj:
    total = 0
    count = 0
    low_salary_persons = []
    for line in f_obj:
        name, salary = line.split()
        salary = float(salary)
        if salary < 20000:
            low_salary_persons.append(name)
        count += 1
        total += salary

    print(f"Сотрудники с окладом меньше 20 тыс: {low_salary_persons}")
    print(f"Средняя величина дохода сотрудников: {total / count}")
