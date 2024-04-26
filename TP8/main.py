import json
import urllib.parse
import urllib.request
import datetime

from dotenv import dotenv_values

# Requêtes HTTP simples avec urllib : Y The Movie Database (TMDB).
# 1. Demander à l’utilisateur·trice de saisir un nom de film.
# 2. Utiliser l’API web de TMDB pour rechercher ce film.
# 3. Le résultat renvoyé est au format json ; utiliser le module json pour charger le résultat renvoyé par
# l’API de TMDB.
# 4. Analyser l’objet créé à partir des données json renvoyées pour identifier les données utiles, c’est-à-
# dire les titres et années des films renvoyés.
# 5. Afficher les résultats à l’utilisateur·trice (maximum 5) avec leurs indices dans la liste des résultats.
# 6. Demander à l’utilisateur·trice de choisir un des films renvoyés, par exemple en indiquant son indice
# dans la liste des résultats (l’utilisateur·trice doit saisir "2" pour sélectionner le deuxième film dans la
# liste des résultats).
# 7. Optionnel : Afficher la liste des acteurs du film sélectionné.
# 8. Optionnel : Sauvegarder l’affiche du film dans un fichier

config = dotenv_values()
print(config['API_MDB'])
print(type(config['API_MDB']))

query = input("Quel film aimeriez-vous regarder?")

params = urllib.parse.urlencode({"api_key": config['API_MDB'], "query": query})

result = urllib.request.urlopen(f"https://api.themoviedb.org/3/search/movie?{params}")

json_content = json.load(result)

json_results = json_content['results'][:5]

for indice, element in enumerate(json_results):
    print(
        f'{indice+1}:{element['original_title']} ({datetime.datetime.strptime(element['release_date'], "%Y-%m-%d") if element['release_date'] != "" else ""})')

user_selection = int(input("Please introduce the index of your chosen movie"))

print(3*"loading...\n")

print(json_results[user_selection])








