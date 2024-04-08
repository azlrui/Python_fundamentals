#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import abstractmethod


class Observer:
    def notify_action(self):
        return NotImplemented

class Observable:
    def __init__(self):
        self.__observateurs = []

    def ajouter_observer(self, observateur: Observer)-> None:
        self.__observateurs.append(observateur)

    def retirer_observer(self, observateur: Observer)-> None:
        self.__observateurs.remove(observateur)

    def notifyAll(self,action:str) -> None:
        for i in self.__observateurs:
            i.notify_action(action)

class Tabloid(Observer):
    def __init__(self, name: str):
        self.__name = name

    def notify_action(self, news:str) -> str:
        print(f"[{self.__name}] Scoop! {news}")

class Individu(Observable):
    def __init__(self, prenom: str, nom: str):
        super().__init__()
        self.__prenom = prenom
        self.__nom = nom

    def epouse(self):
        self.notifyAll('Je me marie ! (' + self.__prenom + ' ' + self.__nom + ')')


if __name__ == "__main__":
    robin = Individu('Scherbatsky', 'Robin')

    # Public et Sun veulent être notifié lorsqu'un évènement important survient dans la vie de Robin Scherbatsky
    public = Tabloid('Public')
    sun = Tabloid('Sun')

    # Pour rappel, Individu doit hériter d'Observable
    # Les magazines Public et Sun doivent suivre Robin Scherbatsky pour pouvoir être notifiés
    robin.ajouter_observer(public)
    robin.ajouter_observer(sun)

    # Lorsque Robin se marie, tous les tabloids qui le suivent sont notifiés
    robin.epouse()
