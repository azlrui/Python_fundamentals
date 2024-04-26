# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import Union

import json
class Produit(ABC):
    __reduction_generale = 0  # en %
    _delai_expiration_reduction = 1  # en jours

    @abstractmethod
    def __init__(self, nom: str, prix: float, date_expiration: int):
        self.nom = nom
        if prix < 0.0:
            raise ValueError(f"Les prix doivent être supérieurs à zéro. Reçu prix: {prix}")
        self.__prix = float(prix)
        self.date_expiration = date_expiration
        self.reduction = 0

    def est_expire(self, date: int) -> bool:
        return self.date_expiration < date

    def expire_bientot(self, date: int) -> bool:
        return self.date_expiration - date <= self.__class__._delai_expiration_reduction

    def get_prix_courant(self) -> float:
        return self.__prix * (1.0 - Produit.__reduction_generale / 100) * (1.0 - self.reduction / 100)

    def get_prix_initial(self) -> float:
        return self.__prix

    def __str__(self) -> str:
        pc = self.get_prix_courant()
        pi = self.get_prix_initial()
        return f"[{self.__class__.__name__}] {self.nom} ({pc} CHF{f', était à {pi} CHF' if pi != pc else ''})"

    __repr__ = __str__

    def set_reduction(self, reduction: float) -> None:
        self._verification_reduction(reduction)
        self.reduction = float(reduction)

    @classmethod
    def set_reduction_generale(cls, reduction: float) -> None:
        cls.__reduction_generale = float(reduction)

    @classmethod
    def set_expiration_reduction(cls, delai: int) -> None:
        delai = int(delai)
        if delai < 0:
            raise ValueError(f"Le délai d'expiration des réductions doit être supérieur à 0. Reçu delai: {delai}")
        cls._delai_expiration_reduction = delai

    @staticmethod
    def _verification_reduction(reduction: float) -> None:
        if reduction < 0:
            raise ValueError(f"Les réductions doivent être supérieures à zéro. Reçu réduction: {reduction}")


class ProduitFrais(Produit):
    _delai_expiration_reduction = 3

    def __init__(self, name: str, prix: float, date_expiration: int, date_emballage: int):
        super().__init__(name, prix, date_expiration)
        self._date_emballage = date_emballage

    def __str__(self):
        return f"{super().__str__()}, date d'Emballage: {self._date_emballage}"


class ProduitInformatique(Produit):
    _delai_expiration_reduction = 0

    def __init__(self, nom, prix, license: str):
        # Les produits informatiques ne peuvent pas périmer
        # float("inf") correspond  l'infinité positive
        super().__init__(nom, prix, float("inf"))  
        self.__license = license


class Supermarche:
    __expiration_reduction = 50

    def __init__(self):
        self.__produits: list[Union[ProduitFrais, ProduitInformatique]] = []

    def __str__(self):
        return f"[{self.__class__.__name__}]\n{"\n".join([f"- {produit}" for produit in self.__produits])}"

    __repr__ = __str__

    def mettre_a_jour(self, date: int) -> None:
        # Ici, on enlève les produits expirés
        self.__produits = [produit for produit in self.__produits if not produit.est_expire(date)]
        # On ajoute une réduction aux produits sur le point d'expirer
        for produit in self.__produits:
            if produit.expire_bientot(date):
                produit.set_reduction(Supermarche.__expiration_reduction)

    def ajouter(self, produit: Produit) -> None:
        if not isinstance(produit, Produit):
            raise TypeError("Seuls les produits peuvent être ajoutés au supermarché")
        self.__produits.append(produit)


if __name__ == '__main__':
    rayon = Supermarche()
    pf = ProduitFrais("Saumon", 10.0, 6, 2)
    print(pf)
    rayon.ajouter(ProduitFrais("Saumon", 10.0, 6, 2))  # la réduction pour le saumon devrait apparaître dès le jour 3
    rayon.ajouter(ProduitFrais("Pain", 3.0, 2, 1))
    rayon.ajouter(ProduitInformatique("Office 365", 160.0, "1234567890123456789"))
    print(rayon)
    print()
    for date in range(12):
        print(f"Day {date}")
        if date == 4:
            Produit.set_reduction_generale(20)
        if date == 7:
            Produit.set_reduction_generale(0)
        rayon.mettre_a_jour(date)
        print(rayon)
