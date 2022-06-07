

class Nodo:
    def __init__(self,dato):
        self.__dato = dato


    @property #getter
    def dato(self):
        return self.__dato

    def __str__(self):
        return str(self.__dato)