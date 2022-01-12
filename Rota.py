import logging

class Rota:

    def __init__(self, origem, destino, data, id):
        self.__origem = origem
        self.__destino = destino
        self.__data = data
        self.__id = id

        self.log = logging.getLogger(__name__)
        self.log.debug("Rota inicializado")

    def get_rota(self):
        print("(" + self.__id + ") " + self.__origem + " - " + self.__destino + " | Data: " + self.__data)


