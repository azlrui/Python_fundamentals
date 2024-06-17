from abc import ABC, abstractmethod

def check_type(type1, type2):
    if not isinstance(type1,type2):
        raise TypeError

class EnsembleAvecMin(ABC):
    @abstractmethod
    def get_min(self):
        pass
    def __add__(self, other):
        check_type(other, EnsembleAvecMin)
        return CompositeEnsembleAvecMin(self, other)

class CompositeEnsembleAvecMin(EnsembleAvecMin):
    def __init__(self, composite1 : EnsembleAvecMin, composite2 : EnsembleAvecMin) -> None:
        check_type(composite1, EnsembleAvecMin)
        check_type(composite2, EnsembleAvecMin)
        self.__composites = [composite1, composite2]

    def get_min(self) -> float:
        return min([x.get_min() for x in self.__composites])

class EnsembleList(EnsembleAvecMin):
    def __init__(self):
        self.__liste = []

    def add_value(self, value):
        check_type(value, int)
        self.__liste.append(value)

    def get_min(self):
        return min(self.__liste)

class EnsembleDict(EnsembleAvecMin):
    def __init__(self):
        self.__dict = {}

    def add_key_value(self, key, value):
        check_type(key, str)
        check_type(value, int)
        self.__dict[key] = value

    def get_min(self):
        return min(self.__dict.values())

if __name__ == "__main__":
    ed = EnsembleDict()
    ed.add_key_value('A', 10)
    ed.add_key_value('B', 12)
    ed.add_key_value('C', -5)

    el = EnsembleList()
    el.add_value(4)
    el.add_value(-8)
    el2 = EnsembleList()
    el2.add_value(19)
    el2.add_value(-99)

    ce = CompositeEnsembleAvecMin(el, ed)
    ce2 = CompositeEnsembleAvecMin(el2, ce)
    print(ed.get_min(), el.get_min(), ce.get_min(), ce2.get_min())
    ed.add_key_value('D', -10)
    print(ed.get_min(), el.get_min(), ce.get_min())
    res = el + ed
    print(res.get_min())