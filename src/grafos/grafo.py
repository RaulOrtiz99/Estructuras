

from grafos.arista import Arista


class Grafo:
    def __init__(self):
        self.__aristas = []

    #TODO: METODOS PARA AGREGAR Y ELIMINAR ARTISTAS

    def agregar_arista(self,arista:Arista):
        if arista not in self.__aristas:
            self.__aristas.append(arista)


    def __str__(self) -> str:
        return str([str(arista)for arista in self.__aristas]) #esto simplemente es para imprimir las aristas
