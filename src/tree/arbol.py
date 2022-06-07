from src.tree.nodo import Nodo


class Arbol:

    def __init__(self, valor):
        self.raiz = Nodo(valor)
        pass

    # METODOS DE LOS ARBOLES BINARIOS

    # INSERTAR -> insertar un valor en el arbol binario
    def insertar(self, datoainsertar): #esto es recursivo
        raiz = self.raiz
        nodoainsertar = Nodo(datoainsertar)
        if (self.raiz == None):
            nodoainsertar = raiz
        elif (nodoainsertar.getdato() < raiz.getdato()):
            raiz.hijo_izq = self.insertar(datoainsertar)
        else:
            raiz.hijo_der = self.insertar(datoainsertar)
        return raiz

        # ES VACIO -> Devuelte TRUE si esta vacio
    def esVacio(self,raiz):
        raiz = self.raiz
        return raiz== None

    # Es HOJA -> Devuelve TRUE si el arbol no tiene ni hijo izquierdo ni hijo derecho eso quiere decir que es hoja

    # BUSCAR -> Busca un nodo por su valor

    # RECORRIDO POST ORDEN

    # RECORRIDO PRE ORDEN

    # RECORRIDO INORDEN

    # METODO ES RAMA -> Devuelve verdadero si es una rama
