import math
from itertools import product
from typing import List
import unicodedata
import csv
import json
from supermarche import Produit, ProduitFrais, ProduitInformatique
import xml.etree.ElementTree as et

# Exercice 1

if __name__ == "__main__":
    with open("sample.txt","r",encoding = "ISO8859-1") as file:
        content = file.read()

    with open("sample_unicode.txt", "w", encoding = "utf-8") as file_utf:
        file_utf.write(content)

    with open("sample_ascii.txt", "wb") as file_ascii:
        file_ascii.write(unicodedata.normalize('NFKD', content).encode('ASCII', 'ignore'))

    with open("sample.txt", "r", encoding="Mac Roman") as f:
        content = f.read()
        print(content)

    # Exercice 2

    with open("etudiants_admin.csv", "r", newline="") as csvfile:
        reader_1 = csv.reader(csvfile, delimiter=";", quotechar='"')
        for column in reader_1:
            print(column)

    with open("etudiants_noms.csv", "r", newline="", encoding="utf-8") as csvfile:
        reader_2 = csv.reader(csvfile, delimiter=",", quotechar='"')
        for column in reader_2:
            print(column)

    with open("etudiants_admin.csv", "r", newline="", encoding="utf-8") as csvfile:
        reader_3 = csv.reader(csvfile, delimiter=";", quotechar='"')
        dict_etudiants_admin_id = {}
        for row in reader_3:
            dict_etudiants_admin_id[row[0]] = row

    with open("etudiants_noms.csv", "r", newline="", encoding="utf-8") as csvfile:
        reader_4 = csv.reader(csvfile, delimiter=",", quotechar='"')
        dict_etudiants_noms = {}
        for column in reader_4:
            dict_etudiants_noms[column[2]] = column

        del dict_etudiants_noms['id']

        print(dict_etudiants_admin_id)
        print(dict_etudiants_noms)

    print("=======================================================================")

    liste_etudiants = []
    for key_noms,value_noms in dict_etudiants_noms.items():
        for key_admin,value_admin in dict_etudiants_admin_id.items():
            if key_admin == key_noms:
                liste_etudiants.append([value_noms[0],value_noms[1],value_admin[1]])

    print(liste_etudiants)
    with open("liste_etudiants.csv", "w", newline='', encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar= '"', quoting = csv.QUOTE_MINIMAL)
        for p in liste_etudiants:
            csvwriter.writerow(p)

    print(50*"====")

    # Exercice 3


    with open("produits.json", "r", encoding="utf-8") as jsonfile:
        jsoncontent = json.load(jsonfile)

        list_all_products = jsoncontent["produits"]
        list_produits = []
        list_produits_frais = []

        for element in list_all_products:
            if element["nom classe"] == "Produits":
                list_produits.append(ProduitInformatique(nom = element["nom"], prix = element['prix'], license = element['donnee migros']))
            elif element["nom classe"] == "ProduitsFrais":
                list_produits_frais.append(ProduitFrais(element["nom"], element['prix'], element['donnee migros'], element['date']))
            else:
                pass

        print(list_produits)
        print(list_produits_frais)

    # Exercice 4

    print("\n" + 50*"=")

    tree = et.parse("./notes.xml").getroot()
    liste_notes = list(map(lambda x : float(x.text), tree.findall("note")))
    mean = sum(liste_notes)/len(liste_notes)
    print(f"La moyenne des notes est de : {mean:.2f}")
    print("La moyenne des notes est de : {:.2f}".format(mean))








