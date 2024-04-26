import re

# 1
if __name__ == '__main__':
    p = re.compile(r'[A-Z]{2}$')
    output = []
    for i in ["A", "AB", "ABC", "ab"]:
        if p.match(i) != None:
            output.append(i)
    print(output)

    # 2
    p = re.compile(r'([a-z]{2}|[A-Z]{2}$)')
    output = []
    for i in ["aa", "Aa", "bb"]:
        if p.match(i) != None:
            output.append(i)
    print(output)

    # 3
    p = re.compile(r'[0-9]{1,6}$')
    output = []
    for i in ["","7","076623","12345678"]:
        if p.match(i) != None:
            output.append(i)
    print(output)

    # 4
    p = re.compile(r'[^0][0-9]{0,5}$')
    output = []
    for i in ["0", "7", "076623", "12345678", "123456"]:
        if p.match(i) != None:
            output.append(i)
    print(output)

    # 5
    def check_matricule() -> str:
        user_input = input("veuillez introduire une matricule\n")
        match = matricule_type.fullmatch(user_input)
        if match == None:
            print("ceci n'est pas une matricule, veuillez réessayer")
            return check_matricule()
        else:
            return f"{match.group('canton').upper()} {match.group('identification')} {match.group('canton').upper()}"

    d = {'AG': 'Argovie', 'AI': 'Appenzell Rhodes-Intérieures',
         'AR': 'Appenzell Rhodes-Extérieures', 'BE': 'Berne',
         'BL': 'Bâle-Campagne', 'BS': 'Bâle-Ville', 'FR': 'Fribourg',
         'GE': 'Genève', 'GL': 'Glaris', 'GR': 'Grisons', 'JU': 'Jura',
         'LU': 'Lucerne', 'NE': 'Neuchâtel', 'NW': 'Nidwald',
         'OW': 'Obwald', 'SG': 'Saint-Gall', 'SH': 'Schaffhouse',
         'SO': 'Soleure', 'SZ': 'Schwytz', 'TG': 'Thurgovie',
         'TI': 'Tessin', 'UR': 'Uri', 'VD': 'Vaud', 'VS': 'Valais',
         'ZG': 'Zoug', 'ZH': 'Zurich'}

    cantons = [str(x).upper() for x in d.keys()] + [str(x).lower() for x in d.keys()]

    n = 6
    matricule_type = re.compile(fr'(?P<canton>{"|".join(cantons)})\s*(?P<identification>[1-9][0-9]{{0,{n-1}}})\s*(?P=canton)?')
    ok = check_matricule()
    print(ok)
    print(" ".join(cantons))