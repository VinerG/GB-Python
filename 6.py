# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв
# и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

def int_func(text):
    for c in list(text):
        if c < 'a' or c > 'z':
            raise ValueError("Неверный формат входных данных!")

    return text[0].upper() + text[1:]


print(int_func("asdfasdasd"))
