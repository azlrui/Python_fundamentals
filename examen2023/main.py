if not __name__ == "__main__":
    exit(0)


class Weapon:
    _id = 0
    _register = {}

    @classmethod
    def obtain_id(cls) -> int:
        cls._id = cls._id + 1
        return cls._id

    @classmethod
    def update_register(cls, id: int, object: object) -> None:
        cls._register[id] = object

    @classmethod
    def find_id(cls, id: int) -> object:
        try:
            return cls._register[id]
        except:
            return None

    def __init__(self, origin: str, model: str):
        self.origin = origin
        self.model = model
        self._id = Weapon.obtain_id()
        Weapon.update_register(self._id, self)

    def get_id(self) -> int:
        return self._id

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.origin},{self.model},{self._id})"


class FireWeapon(Weapon):
    def __init__(self, fabriquant: str, modele: str, calibre: float):
        super().__init__(fabriquant, modele)
        self.calibre = calibre


pistolet = Weapon("USA", "DesertEagle")
sniper = FireWeapon("France", "2000m", "45mm")
