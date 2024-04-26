class ConfigSingleton:
    _instance = None
    _dico = {}
    def __init__(self):
        raise RuntimeError("It's a Singleton! Use get_instance() instead")


    @classmethod
    def get_instance(cls):
        if cls._instance == None :
            cls._instance = cls.__new__(cls)

        return cls._instance

    def add_value(cls, key:str, value) -> dict:
        cls._dico[key] = value

        return cls._dico

    def search_key(cls, key:str):
        print(cls._dico[key])

c2 = ConfigSingleton.get_instance()
c3 = ConfigSingleton.get_instance()

print(c2 == c3)

c3.add_value("Prénom", "Rui")
c3.search_key("Prénom")