# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

counter = []

# file processing
with open("text_2.txt", "r", encoding="utf-8") as f_obj:
    for line in f_obj:
        counter.append(len(line.split()))

# print results
print(f"Строк в файле: {len(counter)}")
for i, cnt in enumerate(counter, 1):
    print(f"В {i} строке слов: {cnt}")
