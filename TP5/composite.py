#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import abstractmethod

def verifier_type(type1,type2):
    if not isinstance(type1,type2):
        raise TypeError(f"{type2.__name__} is the right type, not '{type(type1).__name__}'")

class EnsembleAvecMin:
    @abstractmethod
    def get_min(self):
        return NotImplemented
    def __add__(self, other):
        verifier_type(other,EnsembleAvecMin)
        return CompositeEnsembleAvecMin(self,other)
class EnsembleList(EnsembleAvecMin):
    def __init__(self):
        self.__ensemble = []

    def ajouter_valeur(self, value: int) -> list:
        verifier_type(value,int)
        self.__ensemble.append(value)

        return self.__ensemble

    def get_min(self):
        return min(self.__ensemble)


class EnsembleDict(EnsembleAvecMin):
    def __init__(self):
        self.__ensemble = {}

    def ajouter_cle_valeur(self, cle: str, value: int) -> dict:
        verifier_type(cle, str)
        verifier_type(value, int)
        self.__ensemble[cle] = value

        return self.__ensemble

    def get_min(self) -> int:
        return min(self.__ensemble.values())


class CompositeEnsembleAvecMin(EnsembleAvecMin):
    def __init__(self, composant_1 : EnsembleAvecMin, composant_2 : EnsembleAvecMin):
        verifier_type(composant_1, EnsembleAvecMin)
        verifier_type(composant_2, EnsembleAvecMin)
        self.composant_1 = composant_1
        self.composant_2 = composant_2

    def get_min(self):
        return min(self.composant_1.get_min(), self.composant_2.get_min())


if __name__ == "__main__":
    ed = EnsembleDict()
    ed.ajouter_cle_valeur('A', 10)
    ed.ajouter_cle_valeur('B', 12)
    ed.ajouter_cle_valeur('C', -5)

    el = EnsembleList()
    el.ajouter_valeur(4)
    el.ajouter_valeur(-8)

    el2 = EnsembleList()
    el2.ajouter_valeur(19)
    el2.ajouter_valeur(-99)

    ce = CompositeEnsembleAvecMin(el, ed)
    ce2 = CompositeEnsembleAvecMin(el2, ce)
    print(ed.get_min(), el.get_min(), ce.get_min(), ce2.get_min())

    ed.ajouter_cle_valeur('D', -10)
    print(ed.get_min(), el.get_min(), ce.get_min())

    test = ed + ce
    print(test.get_min())
