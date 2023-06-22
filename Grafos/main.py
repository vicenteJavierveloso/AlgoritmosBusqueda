from BusquedaEnAnchura import BEA
import networkx as nx
import matplotlib.pyplot as pyl
import time

#Inicio de creacion del grafo de prueba
ciudades = ["Osorno", "Valdivia", "Frutillar", "Puerto Varas", "Puerto Montt", "Los Muermos", "Lago Ranco", "Futrono", "Santiago",
             "Concepcion", "Constitucion", "Arica", "La Serena", "Entre Lagos", "Iquique", "Antofagasta", "Valparaiso", "Viña del Mar", "Punta Arenas"]

mapa = nx.Graph()

mapa.add_nodes_from(ciudades)

#Añade atributos a los nodos
atributos = {"Osorno": {"numero": "1"}, "Valdivia": {"numero": "1"}, "Frutillar": {"numero": "1"}, "Puerto Varas": {"numero": "1"},
            "Puerto Montt": {"numero": "1"}, "Los Muermos": {"numero": "1"}, "Lago Ranco": {"numero": "1"}, "Futrono": {"numero": "10"},
            "Santiago": {"numero": "1"}, "Concepcion": {"numero": "1"}, "Constitucion": {"numero": "1"}, "Arica": {"numero": "1"},
            "La Serena": {"numero": "1"}, "Entre Lagos": {"numero": "1"}, "Iquique": {"numero": "1"}, 
            "Antofagasta": {"numero": "1"}, "Valparaiso": {"numero": "1"}, "Viña del Mar": {"numero": "1"}, "Punta Arenas": {"numero": "1"}}

nx.set_node_attributes(mapa,atributos)

mapa.add_edge("Osorno","Frutillar")
mapa.add_edge("Frutillar","Puerto Varas")
mapa.add_edge("Puerto Varas", "Puerto Montt")
mapa.add_edge("Puerto Varas", "Los Muermos")
mapa.add_edge("Puerto Montt", "Los Muermos")
mapa.add_edge("Osorno","Lago Ranco")
mapa.add_edge("Osorno", "Futrono")
mapa.add_edge("Osorno", "Entre Lagos")
mapa.add_edge("Futrono","Lago Ranco")
mapa.add_edge("Santiago", "Concepcion")
mapa.add_edge("Santiago", "Constitucion")
mapa.add_edge("Santiago","Valparaiso")
mapa.add_edge("Santiago","Entre Lagos")
mapa.add_edge("La Serena","Santiago")
mapa.add_edge("Frutillar","Punta Arenas")
mapa.add_edge("Iquique","Lago Ranco")
mapa.add_edge("Antofagasta","Punta Arenas")
mapa.add_edge("Arica","Punta Arenas")
mapa.add_edge("Punta Arenas","Viña del Mar")
mapa.add_edge("Iquique","Antofagasta")
mapa.add_edge("Puerto Varas","La Serena")
mapa.add_edge("Constitucion","Osorno")
mapa.add_edge("Frutillar","Santiago")
mapa.add_edge("Arica","Puerto Montt")
mapa.add_edge("Futrono","Punta Arenas")
mapa.add_edge("Entre Lagos","Frutillar")
mapa.add_edge("Valdivia", "Constitucion")

#Fin creacion grafo de prueba

#Buscar algun atributo (llave) en los nodos del grafo que contenga el elemento especificado
# comenzando desde el nodo dado
print(BEA(mapa,"Los Muermos", "numero", "10"))

nx.draw(mapa, with_labels=True)
pyl.show()