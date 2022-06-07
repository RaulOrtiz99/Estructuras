class Nodo:
    
    def __init__(self,dato):
        
        self.dato = dato 
        self.izquierdo= None
        self.derecho = None 
    
    def setDato(self,dato):
        self.dato = dato 
    
    def getDato(self):
        return self.dato
    
    def setIzq(self,nodo):
        self.izq = nodo 
    
    def getIzq(self):
        return self.izquierdo
    
    def getDer(self):
        return self.derecho 
    
    def setDer(self,nodo):
        self.derecho = nodo
    
    def esHoja(self):
        return self.izquierdo ==None and self.derecho ==None 
            