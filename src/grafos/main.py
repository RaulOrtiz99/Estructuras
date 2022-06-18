

from grafos.arista import AristaNoDirigida
from grafos.grafo import Grafo
from grafos.nodo import Nodo


n1 = Nodo(10)
n2 = Nodo(15)


print(n1, n2)

#esto es para aristas generales
# arista = Arista(n1, n2)
# arista2 = Arista(Nodo((50,60)), Nodo((200,150)))
#
# print(arista)
#
# print(arista2)

#Arista no dirigidas
arista1 = AristaNoDirigida(n1, n2)
arista2 = AristaNoDirigida(Nodo((50,60)), Nodo((200,150)))
# print(arista1)
# print(arista2)


## grafo

g = Grafo()

g.agregar_arista(arista1)
g.agregar_arista(arista2)

print("GRAFO:")
print(g)







