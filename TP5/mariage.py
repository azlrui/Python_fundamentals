# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
class Individu(ABC):
    liste_individu = []
    _genre: str
    _titre: str
    _titre_marie: str

    def __init__(self, prenom: str, nom: str):
        self._nom: str = str(nom)
        self._prenom: str = str(prenom)
        self._age: int = 0
        self._nom_marital: str = ''
        Individu.liste_individu.append(self)

    @classmethod
    def liste_individu_age(cls, n) -> list["Individu"]:
        return list(map(str, sorted([i for i in cls.liste_individu if i.get_age() > n])))

    def get_nom(self) -> str:
        return self._nom

    def get_age(self) -> int:
        return self._age

    def set_age(self, age) -> None:
        self._age = age

    def anniversaire(self) -> None:
        self._age += 1

    @classmethod
    def get_genre(cls) -> str:
        return cls._genre
    
    @classmethod
    def get_titre(cls) -> str:
        return cls._titre
    
    @classmethod
    def get_titre_marie(cls) -> str:
        return cls._titre_marie

    def epouse(self, conjoint) -> None:
        pass

    def verification_avant_mariage(self) -> None:
        if self.est_marie():
            raise ValueError(f"{self} est déjà marié(e). Faites le/la divorcer avant!")

    def verification_avant_divorce(self) -> None:
        if not self.est_marie():
            raise ValueError(f"{self} n'est pas marié.")

    def divorce(self) -> None:
        pass

    def est_marie(self) -> bool:
        pass

    def est_divorce(self) -> bool:
        pass

    # Si les arguments sont protégés et non privés, on peut se passer de getters.
    # Mais c'est mieux d'utiliser des getters quand même,
    # car si les attributs était censé être accede directement, ils n'aurait pas été mis comme protégé.
    def __eq__(self, other):
        return self._age == other.get_age() and self._prenom == other.get_age() and self._nom == other.get_age()

    # Comparateur <
    def __lt__(self, other):
        return self._age < other.get_age()
    
    def __le__(self, other):
        return self._age <= other.get_age()


class Enby(Individu):
    _genre = "NB"
    _titre = "Mx."
    _titre_marie = "Mx."

    def __str__(self):
        return f"{self.get_titre()} {self._prenom} {self._nom}{f'-{self._nom_marital}' if self.est_marie() else ''}"


class Femme(Individu):
    _genre = "F"
    _titre = "Mlle."
    _titre_marie = "Mme."

    def __str__(self):
        return f"{self.get_titre_marie() if self.est_marie() else self.get_titre()} {self._prenom} {self._nom}" \
               f"{f'-{self._nom_marital}' if self.est_marie() else ''}"


class Homme(Individu):
    _genre = "H"
    _titre = "M."
    _titre_marie = "M."

    def __str__(self):
        return f"{self.get_titre()} {self._prenom} {self._nom if not self.est_marie() else self._nom_marital}"


if __name__ == '__main__':
    robin = Femme('Robin', 'Scherbatsky')
    ted = Enby('Ted', 'Mosby')
    barney = Homme('Barney', 'Stinson')

    # affiche les informations complètes (str et get_historique) pour les trois individus barney, ted et robin
    print(', '.join(map(str, [robin, ted, barney])))

    robin.epouse(barney, 2013, 'Farhampton')
    print(', '.join(map(str, [robin, ted, barney])))

    robin.divorce(2014, 'New york')
    print(', '.join(map(str, [robin, ted, barney])))

    robin.epouse(ted, 2015, 'New York')
    print(', '.join(map(str, [robin, ted, barney])))

    # Lors d'une copie profonde avec copy.deepcopy(robin), tous les objets individu, mariage et divorce liés (directement ou pas) à robin seront dupliqués.
    # Ce sera donc le cas de ted, car il est lié à robin par un mariage courant, self._dernier_mariage
    # Ce sera donc le cas de barney, car il est lié à robin par un (ancien) mariage, stocké dans self._mariages_precedents
