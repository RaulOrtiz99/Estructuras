
from arboles.ArbolBinario.nodo import Nodo


class Arbol:

    def __init__(self, dato):
        self.raiz = dato

    def _agregarRecursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(dato)
            else:
                self.agregarRecursivo(nodo.izquierdo, dato)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(dato)
            else:
                self.agregarRecursivo(nodo.derecho, dato)

    def _buscar(self, nodo, dato):
        busqueda = int(busqueda)
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            print("Este elemento existe")
            return
        if busqueda < nodo.dato:
            return self._buscar(nodo.izquierdo, busqueda)
        else:
            return self._buscar(nodo.derecho, busqueda)

    # TODO: Rcorridos (travesias) estan en modo recursivos y son privadas es decir solo se acceden desde esta clase

    def _inordenRecursivo(self, nodo):
        if nodo is not None:
            self._inordenRecursivo(nodo.izquierdo)
            print(nodo.dato, end=', ')
            self._inordenRecursivo(nodo.derecho)

    def _preordenRecursivo(self, nodo):
        if nodo is None:
            print(nodo.dato, end=" ,")
            self._preordenRecursivo(nodo.izquierdo)
            self._preordenRecursivo(nodo.derecho)

    def _postordenRecursivo(self, nodo):
        if nodo is not None:
            self._postordenRecursivo(nodo.izquierdo)
            self._postordenRecursivo(nodo.derecho)
            print(nodo.dato, end=" ,")

    # TODO Funciones publicas

    def agregar(self, dato):
        self._agregarRecursivo(self.raiz, dato)

    def inorden(self):
        print("recorrido inorden: ")
        self._inordenRecursivo(self.raiz)
        print("_______________________")

    def preorden(self):
        print("imprimiendo arbol en preorden: ")
        self._preordenRecursivo(self.raiz)
        print("_______________________")

    def postorden(self):
        print("imprimiendo arbol en postorden: ")
        self._postordenRecursivo(self.raiz)
        print("_______________________")

    def buscar(self, busqueda):
        return self._buscar(self.raiz, busqueda)
