from googlemaps import Client

import apikey
import urllib.parse
import urllib.request
import json
import googlemaps

def themoviedb(query : str):

    url = "https://api.themoviedb.org/3/search/movie?"
    params = urllib.parse.urlencode({'query' : query, 'api_key': apikey.TheMovieDatabase})
    r = urllib.request.urlopen(f"{url}{params}")

    object = json.load(r)
    res = ""
    for index, result in enumerate(object['results'][:5]):
        res = res + f"{index} - {result['title']} - ({result['release_date']})\n"

    user_film_select = 2
    for index, result in enumerate(object['results'][:5]):
        if index == user_film_select:
            res = f"{index} - {result['title']} - ({result['release_date']})"
    return res

def ask_adress():
    user_location_wish = input("Veuillez-introduire une adresse svp")
    user_confirmation = input("Est-ce vraiment l'adresse que vous voulez? Appuyez sur [Y] ou [N]")
    if user_confirmation == "y" or "Y":
        adresse = client.geocode(user_location_wish)
    else:
        ask_adress()
    print(f"Adresse identifiée : {adresse[0]['formatted_address']}")
    return adresse[0]['formatted_address']

def time_of_travelling(departure : str, arrival : str):
    modes = ['driving', 'walking', 'transit', 'bicycling']
    results = []
    time_travel = {}
    for mode in modes :
        requests = client.distance_matrix(origins = departure, destinations = arrival, mode = mode)
        time_travel[mode] = requests['rows'][0]['elements'][0]['duration']['text']
        results.append(requests)

    return (f"Voici le trajet le plus rapide entre {departure} et {arrival} : durée {min(time_travel.values())} "
            f"en {[i for i in time_travel if time_travel[i] == min(time_travel.values())][0]}")

if __name__ == "__main__":
    print(themoviedb("titanic"))

    client = googlemaps.Client(key=apikey.GoogleMaps)
    departure = ask_adress()
    arrival = ask_adress()
    print(time_of_travelling(departure, arrival))