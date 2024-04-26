import math
from fractions import Fraction
from typing import Union


class Fraction:
    def __init__(self, numerator: int = 0, denominator: int = 1):
        numerator = int(numerator)
        denominator = int(denominator)
        self.__numerator = numerator
        self.__denominator = denominator

        if self.__denominator == 0:
            raise ZeroDivisionError("Veuillez introduire une valeur différente de 0")
        self.simplify()

    def __str__(self) -> str:
        return f"{self.__numerator}/{self.__denominator}"

    def __eq__(self, other: Union["Fraction",int, float]) -> bool:
        if isinstance(other, Fraction):
            return self.__numerator == other.get_numerator() and self.__denominator == other.get_denominator()
        elif isinstance(other, int):
            return self == Fraction(int(other))
        elif isinstance(other, float):
            return self == Fraction(int(other))
        else:
            return NotImplemented

    def __lt__(self, other: Union["Fraction",int, float]) -> bool:
        if isinstance(other, Fraction):
            return self.value() < other.value()
        elif isinstance(other, int):
            return self.value() < Fraction(int(other)).value()
        elif isinstance(other, float):
            return self < Fraction(int(other)).value()
        else:
            return NotImplemented

    def __gt__(self, other: Union["Fraction",int, float]) -> bool:
        if isinstance(other, Fraction):
            return self.value() > other.value()
        elif isinstance(other, int):
            return self.value() > Fraction(int(other)).value()
        elif isinstance(other, float):
            return self > Fraction(int(other)).value()
        else:
            return NotImplemented

    def __ge__(self, other: Union["Fraction",int, float]) -> bool:
        if isinstance(other, Fraction):
            return self.value() >= other.value()
        elif isinstance(other, int):
            return self.value() >= Fraction(int(other)).value()
        elif isinstance(other, float):
            return self >= Fraction(int(other)).value()
        else:
            return NotImplemented

    def __le__(self, other: Union["Fraction",int, float]) -> bool:
        if isinstance(other, Fraction):
            return self.value() <= other.value()
        elif isinstance(other, int):
            return self.value() <= Fraction(int(other)).value()
        elif isinstance(other, float):
            return self <= Fraction(int(other)).value()
        else:
            return NotImplemented

    def __add__(self, other: Union["Fraction",int, float]) -> "Fraction":
        if isinstance(other, Fraction):
            frac = Fraction(self.__numerator, self.__denominator)
            frac.set_numerator(self.__numerator*other.__denominator + self.__denominator*other.__numerator)
            frac.set_denominator(self.__denominator*other.__denominator)
            frac.simplify()
            return frac
        elif isinstance(other, int):
            return self + Fraction(int(other))
        elif isinstance(other, float):
            return self + Fraction(int(other))
        else:
            return NotImplemented

    def __radd__(self, other: Union["Fraction",int, float]) -> "Fraction":
        return self + other

    def __sub__(self, other: Union["Fraction",int]) -> "Fraction":
        if isinstance(other, Fraction):
            frac = Fraction(self.__numerator, self.__denominator)
            frac.set_numerator(self.__numerator*other.__denominator - self.__denominator*other.__numerator)
            frac.set_denominator(self.__denominator*other.__denominator)
            frac.simplify()
            return frac
        elif isinstance(other, int):
            return self + Fraction(int(other))
        elif isinstance(other, float):
            return self + Fraction(int(other))
        else:
            return NotImplemented

    def __rsub__(self, other: Union["Fraction", int, float]) -> "Fraction":
        return self - other

    def __mul__(self, other: Union["Fraction", int, float]) -> "Fraction":
        if isinstance(other, Fraction):
            frac = Fraction(self.__numerator, self.__denominator)
            frac.set_numerator(other.__numerator * self.__numerator)
            frac.set_denominator(other.__denominator * self.__denominator)
            frac.simplify()
            return frac
        elif isinstance(other, int):
            return self * Fraction(int(other))
        elif isinstance(other, float):
            return self * Fraction(int(other))
        else:
            return NotImplemented

    def __rmul__(self, other: Union["Fraction", int, float]) -> 'Fraction':
        return self * other

    def __pow__(self, power: Union[int,float]) -> "Fraction":
        if isinstance(power, int) or isinstance(power, float):
            return Fraction(self.__numerator ** power, self.__denominator ** power)
        else:
            return NotImplemented
    def get_numerator(self) -> int:
        return self.__numerator

    def get_denominator(self) -> int:
        return self.__denominator

    def set_numerator(self, numerator: int) -> None:
        self.__numerator = int(numerator)
        self.simplify()
    def set_denominator(self, denominator: int) -> None:
        if denominator == 0:
            raise ValueError("Division par zéro impossible!")
        self.__denominator = int(denominator)
        self.simplify()

    def value(self):
        return self.__numerator / self.__denominator

    def simplify(self):
        if self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator

        gcd = math.gcd(self.__numerator, self.__denominator)
        self.__numerator = int(self.__numerator / gcd)
        self.__denominator = int(self.__denominator / gcd)

    __repr__ = __str__

if __name__ == '__main__':
    demi = Fraction(1, 2)

    print(Fraction(5, 3).value())

    demi.set_denominator(5)

    print(demi.value())

    print(demi.get_numerator())

    singdioxides = Fraction(5, 10)
    singdioxides.simplify()
    print(singdioxides)

    exemple_a = Fraction(10,-20)
    exemple_a.simplify()
    print(exemple_a)

    print(Fraction(1, 2) == Fraction(2,4))
    print(Fraction(4,2) == 2)
    print(Fraction(2, 4) >= Fraction(5,10))
    print(Fraction(2) + Fraction(1, 2))
    print(2 + Fraction(1))
    print(Fraction(7,9)*2.563)

    l = [Fraction(1, 2), Fraction(-2,3), 1]
    print(sorted(l), min(l), max(l), sum(l))
    print(Fraction(-50) ** -1)