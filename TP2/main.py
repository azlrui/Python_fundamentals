import sys
from functools import reduce


def sort_values(liste):
    valid_values = []
    invalid_values = []

    for value in liste:
        try:
            valid_values.append(int(value))
        except Exception:
            invalid_values.append(value)

    return valid_values, invalid_values

def string_check(text):
    if isinstance(text, str):
        return text
    else:
        raise ValueError


def question2(user_entries):
    if len(user_entries) == 0:
        exit(1)

    (valid_values, invalid_values) = sort_values(user_entries)

    if len(invalid_values) > 0:
        print(f"Wallah t'es con. Ce ne sont pas des nombres zebi. Voici ce qui est faux : {" - ".join(invalid_values)}")

    out = reduce(lambda x, y: x * y, valid_values)
    print(out)


def question3(user_entries):
    if not len(user_entries):
        exit(1)
    elif len(user_entries) != 2:
        exit(2)

    (valid_values, invalid_values) = sort_values(user_entries)

    if len(invalid_values):
        raise f"Tu as des valeurs invalides. Les voici : {invalid_values}"

    try:
        return user_entries[0] / user_entries[1]
    except ZeroDivisionError:
        raise "Tu ne peux pas diviser par zéro"

def question4():
    try:
        x = int(input())
    except ValueError:
        print(f"Veuillez introduire un nombre")
        return question4()
    return x**2

def question5(user_input):
    value = int(user_input[0])
    user_values = []
    for i in range(value):
        new_txt = string_check(input())
        user_values.append(new_txt)

    return " ".join(user_values)


if __name__ == "__main__":
    print(question5(sys.argv[1]))