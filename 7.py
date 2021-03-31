# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"({self.a} + {self.b}i)"

    def __add__(self, other):
        if not isinstance(other, Complex):
            raise TypeError(f"unsupported operand type(s) for +: 'Compl' and '{type(other)}'")
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        if not isinstance(other, Complex):
            raise TypeError(f"unsupported operand type(s) for +: 'Compl' and '{type(other)}'")
        t_a = self.a * other.a - self.b * other.b
        t_b = self.a * other.b + self.b * other.a
        return Complex(t_a, t_b)


a = Complex(5, 2)
b = Complex(3, 5)
print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {a + b}")
print(f"a * b = {a * b}")
