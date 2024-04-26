
if not __name__ == "__main__":
    exit(0)
class Weapon:
    __id = 0
    __register = {}

    @classmethod
    def obtain_id(cls) -> int:
        cls.__id = cls.__id + 1
        return cls.__id

    @classmethod
    def update_register(cls, id: int, object: object) -> None:
        cls.__register[id] = object

    @classmethod
    def find_id(cls, id: int) -> object:
        try:
            return cls.__register[id]
        except:
            return None

    def __init__(self, origin: str, model: str):
        self.origin = origin
        self.model = model
        self.__id = Weapon.obtain_id()
        Weapon.update_register(self.__id, self)

    def get_id(self) -> int:
        return self.__id

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.origin},{self.model},{self.__id})"


class FireWeapon(Weapon):
    def __init__(self, fabriquant: str, modele: str, calibre: float):
        super().__init__(fabriquant, modele)
        self.calibre = calibre


pistolet = Weapon("USA", "DesertEagle")
sniper = FireWeapon("France", "2000m", "45mm")
