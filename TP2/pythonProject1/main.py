import sys
from functools import reduce

if __name__ == '__main__':

    # Question 2

    if len(sys.argv) > 2:
        print(reduce(lambda x, y: x * y, map(int, sys.argv[1:])))
    elif len(sys.argv) == 2:
        print(sys.argv[1])
    else:
        print(None)

    # Question 3
    try:
        nb1, nb2 = int(sys.argv[1]), int(sys.argv[2])
        print(nb1/nb2)
    except (NameError, IndexError, ValueError):
        print("Veuillez entrer un nombre")

    except ZeroDivisionError:
        print('Division by zero!')

    # Question 4

    def au_carre(x : int) -> int:
        try:
            return int(x) ** 2
        except (TypeError, ValueError):
            print("Veuillez entrer un nombre")
            return au_carre(input())

    print(au_carre(input()))

    # Question 5

    try:
        txt: str = ""
        for value in range(int(sys.argv[1])):
            print("Ecrivez un mot")
            txt = txt + " " + input()

        print(txt)

    except (TypeError, ValueError):
        print("relancez le programme et insérez un chiffre")
