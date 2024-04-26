from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())
# On veut récupérer le texte de la balise b dans la balise p.title : The Dormouse's story
balise = soup.select("html > body > p") # liste de toutes les balises p dans la balise body -> trop général!
print(balise)
balise = soup.select("p") # retourne la liste de toutes les balises p (pas seulement celle de body) -> encore plus général
print(balise)

balise = soup.select("html > body > p.title") # liste de toutes les balises p avec comme classe title dans la balise body
print(balise)
balise = soup.select("p.title") # même chose qu'au dessus: il n'est pas nécessaire d'indique le chemin depuis le début
print(balise)
balise = soup.find_all("p", class_="title") # même chose qu'au dessus avec la méthode find_all (voir documentation)
print(balise)

# Il faut faire attention à être assez spécifique pour avoir la balise voulu! si on ne met que "b",
# la liste retournée contient aussi les autres balises "b" de p.story
balise = soup.select("p.title > b")[0] #On garde seulement le premier élément de la liste
print(balise) # retourn la balise b de p.title (de la balise body)
print(balise.text) # On veut le texte
print(balise.get_text()) # équivalent à .text

# si on veut faire des choses un peu plus complexes...
balise = soup.select("p.story > a.sister")
for b in balise:
    print(b["href"], b["id"], b.text)