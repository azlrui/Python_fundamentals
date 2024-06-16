import math


class Fraction():
    def __init__(self, numerateur : int = 0, denominateur : int = 1):
        self.__int_check(numerateur)
        self.__int_check(denominateur)
        self.__num = numerateur
        self.__den = denominateur
        self.__zero_check()
        self.simplify()

    def __zero_check(self):
        if self.__den == 0:
            raise ValueError("Le dénominateur ne peut être égal à zéro")

    def __int_check(self, value):
        if isinstance(value, int):
            return value
        else :
            return ValueError

    def get_float_value(self):
        return f"{self.__num / self.__den}"

    def get_den(self):
        return self.__den

    def get_num(self):
        return self.__num

    def set_den(self, value):
        self.__int_check(value)
        self.__den = value
        self.simplify()
        return self.__den

    def set_num(self, value):
        self.__int_check(value)
        self.__num = value
        self.simplify()
        return self.__num

    def simplify(self):
        gcd = math.gcd(int(self.get_num()), int(self.get_den()))
        self.__den = self.__den / gcd
        self.__num = self.__num / gcd

    def __str__(self):
        if self.__den == 1:
            return f"{self.__num}"
        else:
            return f"{self.__num}/{self.__den}"

    def __eq__(self, other):
        if isinstance(other, int):
            return self == Fraction(other)

        if not isinstance(other, Fraction):
            return NotImplemented
        else:
            return self.__num == other.get_num() and self.__den == other.get_den()

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            new_num = self.__num * other.__den + other.__num * self.__den
            new_den = self.__den * other.__den
            return Fraction(new_num, new_den)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            new_num = self.__num * other.__den - other.__num * self.__den
            new_den = self.__den * other.__den
            return Fraction(new_num, new_den)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            new_num = self.__num * other.__num
            new_den = self.__den * other.__den
            return Fraction(new_num, new_den)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            new_num = self.__num * other.__den
            new_den = self.__den * other.__num
            return Fraction(new_num, new_den)
        else:
            return NotImplemented

if __name__ == "__main__":
    f1 = Fraction(1, 2)
    print(f1)
    f2 = Fraction()
    print(f2)
    f3 = Fraction(5,3)
    print(f3.get_float_value())
    f4 = Fraction(2,4)
    print(f1 == f3)
    print(f1 == 3)
    f5 = Fraction(2,1)
    print(f5)
    f6 = Fraction(4,2)
    print(f6)
    print(f6 == 2)
    print(f6!=2)
    print(f6!=f1)
    print(f6 + f1)
    print(f6 + 1)
    print(Fraction(1,2) / Fraction(3,2))