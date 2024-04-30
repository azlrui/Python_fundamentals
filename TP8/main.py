import json
import urllib.parse
import urllib.request
import datetime
import googlemaps

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
# print(config['API_MDB'])
# print(type(config['API_MDB']))
#
# query = input("Quel film aimeriez-vous regarder?")
#
# params = urllib.parse.urlencode({"api_key": config['API_MDB'], "query": query})
#
# result = urllib.request.urlopen(f"https://api.themoviedb.org/3/search/movie?{params}")
#
# json_content = json.load(result)
#
# json_results = json_content['results'][:5]
#
# for indice, element in enumerate(json_results):
#     print(
#         f'{indice+1}:{element['original_title']} ({datetime.datetime.strptime(element['release_date'], "%Y-%m-%d") if element['release_date'] != "" else ""})')
#
# user_selection = int(input("Please introduce the index of your chosen movie"))
#
# print(3*"loading...\n")
#
# print(json_results[user_selection])


# Exercice 2

def answer(res):
    if res == "y":
        return res
    elif res == "n":
        trip()
    else:
        answer(str(input(f"Can you please confirm by [Y/N] that you agree with this adress? \n {res}")))
def trip():
    API = googlemaps.Client(key=config['API_GOOGLE'])
    ongoing = str(input("Veuillez introduire l'adresse de départ\n"))
    answer(str(input(f"Can your confirme the adress [Y/N] :\n {ongoing}")))
    ongoing = API.geocode(ongoing)
    print(ongoing)

    ongoing_address = ongoing[0]['formatted_address']
    ongoing_lat = ongoing[0]['geometry']['location']['lat']
    ongoing_lng = ongoing[0]['geometry']['location']['lng']
    ongoing_ = (ongoing_lat, ongoing_lng)


    arrival = str(input("Veuillez introduire l'adresse d'arrivée\n"))
    answer(str(input(f"Can your confirme the adress [Y/N] :\n {arrival}")))

    arrival = API.geocode(ongoing)
    arrival_address = arrival[0]['formatted_address']

    arrival_lat = arrival[0]['geometry']['location']['lat']
    arrival_lng = arrival[0]['geometry']['location']['lng']
    arrival_ = (arrival_lat, arrival_lng)

    result = API.distance_matrix(ongoing_, arrival_)

    return result


print(trip())

print()



