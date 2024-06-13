#TP01 - Fundamentals
from functools import reduce

#Question 1

triple = lambda x : x * 3
print(triple(3))

est_pair = lambda x : x % 2 == 0
print(est_pair(2))

def multiplicateur(n):
    return triple(n)

print(multiplicateur(15))
print(list(filter(lambda x : x % 2 != 0, range(11))))

print([triple(x) for x in range(1,11)])

print(list(map(triple, filter(est_pair, range(1,11)))))
print([triple(x) for x in list(filter(est_pair, range(1,11)))])

produit = lambda x, y : x * y
print(reduce(produit, range(1,11)))

str_list = ['1', '2', '3']
print(reduce(produit, [int(x) for x in str_list]))

factorielle = lambda x : reduce(produit, range(1, x+1)) if x>= 0 else 0
print(factorielle(5))

str_list = ['a', 'b', 'c']
print("_".join(str_list))

int_dict = {i : est_pair(i) for i in range(10)}
print(int_dict)

def fonction(liste):
    return f"{liste[1]}: \n{liste[0]}; \t{liste[2]}!"
print(fonction(["salut", "Brigitte", "Mange"]))

def extraire_mots_longs(phrase):
    x = phrase.split()
    x = filter(lambda x : len(x) >= 3, x)
    return(f"{";".join(x)}")
print(extraire_mots_longs("je suis grand"))

def plus_petit_des_plus_grands(liste, numero):
    plus_grands = list(filter(lambda x : x > numero, liste))
    return min(plus_grands)
print(plus_petit_des_plus_grands([1,2,3,4,5,6,7],5))

def indent(phrase, tab = "\t"):
    return tab.join(phrase)

print(f"zero\n{indent(f"one\n{indent("two\nthree", "\t")}")}")
