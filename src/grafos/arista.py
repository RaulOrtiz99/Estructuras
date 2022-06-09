from src.grafos.nodo import Nodo


class Arista:
    def __init__(self,nodo1:Nodo,nodo2:Nodo):
        self.__par = [nodo1,nodo2]

    def dirigido(self) -> bool:
        return False

    def ponderada(self)-> bool:
        return False

    def get_par(self)-> list: #return [Nodo,Nodo]
        return self.__par

    def __str__(self)-> str: #esto simplemente es para imprimir
        return f"(Nodo: {self.get_par()[0]} ?---Arista----? Nodo: {self.get_par()[1]})"


class AristaNoDirigida(Arista): #puede o no ir a ambos lados

    def __init__(self,nodo1:Nodo,nodo2:Nodo):
        super().__init__(nodo1,nodo2)

    def dirigido(self) -> bool:
        return False

    def getNodo1(self) -> Nodo:
        return self.get_par()[0]

    def getNodo2(self) -> Nodo:
        return self.get_par()[1]

    def __eq__(self,o:object)->bool: #esto es para comparar 2 objetos en este caso el par arista con el otro objeto que inserto a la hora de agregar un nodo
         if self.get_par()[0] == o.get_par()[0] and self.get_par()[1] == o.get_par()[1]:
             return True
         else:
             return False

    def __str__(self)-> str: #esto simplemente es para imprimir
        return f"((Nodo: {self.getNodo1()})) <----Arista---> ((Nodo: {self.getNodo2()}))"














