import re


def question1(txt : str):
    re_double_caps = re.compile(rf"[A-Z]{{2}}")
    match = re_double_caps.fullmatch(txt)
    return match

def question2(txt : str):
    re_double_letters = re.compile(rf"([A-Z]|[a-z]){{2}}")
    match = re_double_letters.fullmatch(txt)
    return match

def question3(txt : str):
    re_six_serie = re.compile(rf"[0-6]+")
    match = re_six_serie.fullmatch(txt)
    return match

def question4(txt : str):
    re_six_serie_nozero = re.compile(rf"(0){{0}}[0-6]+")
    match = re_six_serie_nozero.fullmatch(txt)
    return match

def question5(txt : str, cantons : str):
    n = 6
    re_matricule = re.compile(fr"(?P<canton>{"|".join(cantons)})\s*(?P<id>[1-9][0-9]{{0,{n-1}}})\s*(?P=canton)?")
    match = re_matricule.fullmatch(txt)

    return match


if __name__ == "__main__":

    d = {'AG': 'Argovie', 'AI': 'Appenzell Rhodes-Intérieures',
         'AR': 'Appenzell Rhodes-Extérieures', 'BE': 'Berne',
         'BL': 'Bâle-Campagne', 'BS': 'Bâle-Ville', 'FR': 'Fribourg',
         'GE': 'Genève', 'GL': 'Glaris', 'GR': 'Grisons', 'JU': 'Jura',
         'LU': 'Lucerne', 'NE': 'Neuchâtel', 'NW': 'Nidwald',
         'OW': 'Obwald', 'SG': 'Saint-Gall', 'SH': 'Schaffhouse',
         'SO': 'Soleure', 'SZ': 'Schwytz', 'TG': 'Thurgovie',
         'TI': 'Tessin', 'UR': 'Uri', 'VD': 'Vaud', 'VS': 'Valais',
         'ZG': 'Zoug', 'ZH': 'Zurich'}

    test = ['AB123456', 'VD011111', 'VD 1234567', 'VD123456', 'vd123456', 'Vd123456','VD 123456', 'VD 123456', 'VD \t 123456']
    tests_plaque2 = ['VD 123456', 'VD 123456 VS', 'VD 123045 VD', 'VD 123456vd', 'vd 123456 VD']
    cantons = [str(x).upper() for x in d.keys()] + [str(x).lower() for x in d.keys()]

    for x in tests_plaque2:
        res = question5(x, cantons)
        if res is None:
            pass
        else:
            print(f"Matricule : {res.group("canton").upper()} {res.group("id")}")


