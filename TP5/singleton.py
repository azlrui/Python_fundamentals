class ConfigurationSingleton:
    __isintance = None

    def __init__(self):
        self.__dic = {}

    def set_value(self, key, value):
        self.__dic[key] = value
    @classmethod
    def get_instance(cls):
        if cls.__isintance is None:
            cls.__isintance = ConfigurationSingleton()

        return cls.__isintance

    def get_value(self, key):
        return self.__dic[key]

if __name__ == '__main__':
    conf = ConfigurationSingleton.get_instance()
    conf.set_value('verbose', True)

    conf2 = ConfigurationSingleton.get_instance()

    print(conf.get_value('verbose'), conf2.get_value('verbose'))
    print(hex(id(conf)), hex(id(conf2)))  # L’adresse mémoire est la meme pour les deux objets