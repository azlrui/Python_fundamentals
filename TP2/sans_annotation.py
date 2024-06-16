var1 : str = "ecopo"

ma_fonction = lambda x: x / 2

autre_fonction = lambda y: y + 1

ma_liste : list[str] = ["j'aime", "les", "annotations", "de", "type"]

autre_liste : list[int] = [1, 2, 3, 4, 5, 6]

mon_dico : dict[int, str]= {1: "un", 2: "deux", 3: "trois", 4: "quatre"}

autre_dico dict[str, int] = {"premier": [1, 2, 3], 2: {"cle": "valeur"}}

def remplacer_espace(texte : str, nouveau_charactere : str) -> str:
    temp_texte = texte.split(" ")
    nouveau_texte = nouveau_charactere.join(temp_texte)
    return nouveau_texte


# f1 et f2 doivent être des fonctions, n doit être un parameter qui les correspondent
def mon_enchaineur(f1 : object, f2 : object, n : int):
    return f1(f2(n))

enchaine = mon_enchaineur(ma_fonction, autre_fonction, 2)
print(enchaine)  # devrait valoir 1.5


# x et n doivent être des nombres
def multiplicateur(n : int):
    def mult(x):
        return x * n
    return mult

mult_func = multiplicateur(3)
print(mult_func(2))  # devrait valoir 6


# l doit être une liste de chaines de caractères
def derniere_fonction(l, n):
    if len(l) > n:
        return l[n]
    elif len(l) == n:
        return "egale"
    else:
        print("plus petit que n")


print(derniere_fonction(ma_liste, 2))  # devrait valoir 'annotations'
