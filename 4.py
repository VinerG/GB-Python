# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

TRANSLATE_DICT = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_4.txt", "r", encoding="utf-8") as f_obj, open("text_4_out.txt", "w", encoding="utf-8") as f_obj_out:
    for line in f_obj:
        for s_org, s_translate in TRANSLATE_DICT.items():
            line = line.replace(s_org, s_translate)
        f_obj_out.write(line)
