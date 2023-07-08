from graph_manager import cargar_grafo, guardar_grafo
from BusquedaEnAnchura import BEA
from BusquedaEnProfundidad import BEP_format, BEP
import os
import networkx as nx
from matplotlib import pyplot as pyl

ruta = os.path.dirname(__file__)
ruta = f"{ruta}\grafos\grafo0.graphml"

grafo = cargar_grafo(ruta)

#Ejemplo correcto
busqueda_en_profundidad = BEP(grafo,"Valdivia","Entre Lagos")
print(BEP_format(busqueda_en_profundidad))

#Ejemplo falla busqueda no encontrada
#Esto esta fallando
busqueda_en_profundidad = BEP(grafo, "Valdivia", "NoExiste")
print(BEP_format(busqueda_en_profundidad))

# #Ejemplo falla nodo raiz no existe
busqueda_en_profundidad = BEP(grafo, "NoExiste", "Entre Lagos")
print(BEP_format(busqueda_en_profundidad))

#Ejemplo correcto
print(BEA(grafo,"Valdivia","numero","10"))

#Ejemplo falla nodo raiz no existe
print(BEA(grafo,"NoExiste","numero","10"))

#Ejemplo falla llave o atributo no existe en el nodo
print(BEA(grafo,"Valdivia","NoExiste", "10"))

#Ejemplo falla elemento no existe 
print(BEA(grafo, "Valdivia","numero","999"))

nx.draw(grafo, with_labels=True)
pyl.show()