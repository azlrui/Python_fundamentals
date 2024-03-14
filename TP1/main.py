# TO1 - Basics
import string

# Question 1
triple = lambda x: 3 * x

print(triple(3))

# Question 2
est_pair = lambda x: x % 2 == 0
funct = [est_pair(4), est_pair(7)]
for result in funct:
    print(result)


# Question 3
def multiplicateur(n):
    return lambda x: x * n


print(multiplicateur(3)(4))

# Question 4
pair_list = [i for i in range(10) if i % 2 != 0]
print(pair_list)

# Question 5

## Liste compréhensive
div_3 = [3 * x for x in range(11)[1:]]

## Loop
div_3_2 = []
for x in range(11)[1:]:
    div_3_2.append(x * 3)

## Map
div_3_3 = list(map(lambda x: x * 3, range(11)[1:]))

print(div_3)
print(div_3_2)
print(div_3_3)

# Question 6

result_6 = [3 * x for x in range(1, 11) if x % 2 == 0]
print(result_6)

result_6 = list(filter(lambda x: x % 2 == 0, list(map(lambda x: x * 3, range(1, 11)))))
print(result_6)

# Question 7

from functools import reduce

produit = lambda x, y: x * y
number_list = ['1', '2', '3']
print(reduce(produit, list(map(int, number_list))))

# Question 8
factorielle = lambda x: reduce(lambda x, y: x * y, range(1, x + 1), 1)

print(factorielle(10))

# Question 9
string_list = ['a', 'b', 'c']

output = reduce(lambda x, y: x + "_" + y, string_list)

print(output)

output2 = "_".join(string_list)

print(output2)

# Question exmen

stringlist = ["abc", "def", "ghi", "jkl"]

for i in range(len(stringlist)):
    stringlist[i] = len(stringlist[i])

out = reduce(lambda x,y: x + y, stringlist)
print(out)

# Question 10
nblist = [1, 4, 3, 7]
dictionnaire = {i : i % 2 == 0 for i in nblist}

print(dictionnaire)


# Question 11
def writing(list):
    return print(f"{{{list[1]}}}: \n{list[0]} ; \t {list[2]}!")

writing(["ta mère", "ton chien", "ta patrie"])

# Question 12

def extraire_longs_mots(sentence):
    out = sentence.split()
    txt = []
    for i in out:
        if len(i) >= 3:
            txt.append(i.lower())

    txt.sort()
    return reduce(lambda x, y : x + ";" + y, txt)

print(extraire_longs_mots('Je Suis Content'))

# Question 13

def plus_petit_des_plus_grands(l, v):

    txt = [x for x in l if x >= v]
    return reduce(lambda x, y : min(x,y), txt) if len(txt) > 1 else None


print(plus_petit_des_plus_grands([7, 1, 4, 0], 3))
print(plus_petit_des_plus_grands([7, 1, 4, 0], 8))

# Question 14

def indent(my_string : string, my_tab : string):
    word_list = list(map(lambda x: my_tab + "-" + x, my_string.split()))
    return "\n".join(word_list)

#*******************************TP2********************************************************************************

