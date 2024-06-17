from abc import ABC, abstractmethod

def check_type(type1, type2):
    if not isinstance(type1,type2):
        raise TypeError
class Observer(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def notify(self):
        pass

class Tabloid(Observer):
    def __init__(self, nom : str):
        check_type(nom, str)
        self.__nom = nom

    def notify(self, message):
        return f"[{self.__nom}] Scoop! " + message

class Observable(Observer):
    def __init__(self):
        self.__followers = []

    def add_observer(self, observer):
        check_type(observer, Observer)
        self.__followers.append(observer)

    def remove_observer(self, observer):
        check_type(observer, Observer)
        self.__followers.pop(observer)

    def notify_all(self, message):
        return "\n".join([x.notify(message) for x in self.__followers])

class Individu(Observable):
    def __init__(self, nom: str, prenom:str):
        super().__init__()
        for value in [nom, prenom]:
            check_type(value, str)
        self.__lastname = nom
        self.__firstname = prenom

    def marry(self):
        return self.notify_all(f"Je me marie ! ({self.__firstname} {self.__lastname})")

if __name__ == "__main__":
    robin = Individu('Scherbatsky', 'Robin')
    public = Tabloid('Public')
    sun = Tabloid('Sun')
    robin.add_observer(public)
    robin.add_observer(sun)
    # Lorsque Robin se marie, tous les tabloids qui le suivent sont notifiés
    print(robin.marry())
    ted = Individu('Ted', 'Mosby')
    ted.add_observer(sun)
    print(ted.marry())
