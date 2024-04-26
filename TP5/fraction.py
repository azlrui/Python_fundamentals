class Fraction:
    def __init__(self, numerateur=0, denominateur=1):
        if denominateur == 0:
            raise ZeroDivisionError('Le dénominateur doit être différent de zéro!')

        self.__numerateur = int(numerateur)
        self.__denominateur = int(denominateur)

    def get_numerateur(self):
        return self.__numerateur

    def get_denominateur(self):
        return self.__denominateur

    def add(self, f):
        den = f.get_denominateur()
        num = f.get_numerateur()
        self.__numerateur = self.__numerateur * den + num * self.__denominateur
        self.__denominateur = self.__denominateur * den

    def plus(self, f):
        res = Fraction(self.__numerateur, self.__denominateur)
        res.add(f)
        return res

    def __str__(self):
        return f"{self.__numerateur}/{self.__denominateur}"


if __name__ == '__main__':
    f1 = Fraction(2, 5)
    f2 = Fraction(1, 2)
    f3 = f1.plus(f2)
