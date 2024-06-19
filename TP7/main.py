import csv
import json
from statistics import mean
from decimal import Decimal

import unicodedata
from TP7.supermarche import Produit, ProduitFrais, ProduitInformatique
import xml.etree.ElementTree as et

def question1(file, encoding : str):
    with open(file, encoding = encoding, mode = "r") as f:
        content = f.read()
    with open("sample_unicode.txt", encoding = "utf-8", mode = "w", errors="ignore") as f:
        f.write(content)
    with open("sample_ASCII.txt", mode = "wb") as f:
        f.write(unicodedata.normalize("NFKD",content).encode('ascii', 'ignore'))

def question2(file):
    with open(file, encoding="utf-8", mode = "r") as file :
        content = csv.reader(file, delimiter=";", quotechar='"')
        dico = dict()
        for l in content:
            dico[l[0]] = l
        return dico


def question2bis(file):
    with open(file, encoding="utf-8", mode = "r") as file :
        content = csv.reader(file, delimiter=",", quotechar='"')
        dico = dict()
        state = True
        for l in content:
            if state == True:
                state = False
            else :
                dico[l[2]] = l
        return dico

def dico_joint(dicA, dicB):
    liste = list()
    for keyA, valuesA in dicA.items():
        for keyB, valuesB in dicB.items():
            if keyB == keyA:
                liste.append([valuesB[0],valuesB[1],valuesA[1]])
    return liste

def create_csv(text):
    with open("etuadiants.csv", encoding="utf-8", mode = "w", newline="") as csvfile:
        csvfile = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for p in text:
            csvfile.writerow(p)

def question3(file):
    with open(file, encoding="utf-8", mode = "r") as jsonfile:
        objet = json.load(jsonfile)
        objet = objet['produits']

    liste = []
    for item in objet:
        if item['nom classe'] == 'Produits':
            liste.append(ProduitInformatique(nom = item['nom'], prix= item['prix'], license= item['donnee migros']))
        elif item['nom classe'] == 'ProduitsFrais':
            liste.append(ProduitFrais(name=item['nom'], prix=item['prix'], date_expiration=item['donnee migros'], date_emballage=item['date']))

    return liste

def question4(file):
    tree = et.parse(file)
    root = tree.getroot()
    notes = []
    for e in root.findall('note'):
        notes.append(float(e.text))
    return round(mean(notes),2)

def question_slides(file):
    tree = et.parse(file)
    root = tree.getroot()
    prices = list()

    for e in root.findall("article"):
        price_e = e.find("price")
        price_e_value = price_e.text
        attrib_price_e = price_e.attrib

        if attrib_price_e['currency'] == "EUR":
            prices.append(float(price_e_value) * 1.02)
        else :
            prices.append(float(price_e_value))

        return sum(prices)

if __name__ == "__main__":
    question1("sample.txt", "ISO8859-1")
    dico_admin = question2("etudiants_admin.csv")
    dico_noms = question2bis("etudiants_noms.csv")
    create_csv(dico_joint(dico_noms, dico_admin))
    print(question3("produits.json"))
    print(question4("notes.xml"))
    print(question_slides("ticket.xml"))
