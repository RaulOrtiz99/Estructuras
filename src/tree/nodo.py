class Nodo:

    def __init__(self, valor):
        self.hijo_izq = None
        self.hijo_der = None
        self.dato = valor

    #getters and setters

    def gethijoIzq(self):
        return self.hijo_izq

    def sethijoIzq(self, hijo_izq):
        self.hijo_izq = hijo_izq

    def gethijoDer(self):
        return self.hijo_der

    def sethijoDer(self, hijo_der):
        self.hijo_der = hijo_der

    def getdato(self):
        return self.dato

    def setdato(self, dato):
        self.dato = dato
