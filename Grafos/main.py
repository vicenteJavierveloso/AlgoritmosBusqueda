from BusquedaEnAnchura import BEA
import networkx as nx
import matplotlib.pyplot as pyl
import time

ciudades = ["Osorno", "Valdivia", "Frutillar", "Puerto Varas", "Puerto Montt", "Los Muermos", "Lago Ranco", "Futrono", "Santiago",
             "Concepcion", "Constitucion", "Arica", "La Serena", "Entre Lagos", "Iquique", "Antofagasta", "Valparaiso", "Viña del Mar", "Punta Arenas"]

mapa = nx.Graph()

mapa.add_nodes_from(ciudades)

mapa.add_edge("Osorno","Frutillar")
mapa.add_edge("Frutillar","Puerto Varas")
mapa.add_edge("Puerto Varas", "Puerto Montt")
mapa.add_edge("Puerto Varas", "Los Muermos")
mapa.add_edge("Puerto Montt", "Los Muermos")
mapa.add_edge("Osorno","Lago Ranco")
mapa.add_edge("Osorno", "Futrono")
mapa.add_edge("Osorno", "Valdivia")
mapa.add_edge("Futrono","Lago Ranco")
mapa.add_edge("Santiago", "Concepcion")
mapa.add_edge("Santiago", "Constitucion")
mapa.add_edge("Santiago","Valparaiso")
mapa.add_edge("Santiago","Entre Lagos")
mapa.add_edge("La Serena","Santiago")
mapa.add_edge("Entre Lagos","Punta Arenas")
mapa.add_edge("Iquique","Lago Ranco")
mapa.add_edge("Antofagasta","Punta Arenas")
mapa.add_edge("Arica","Punta Arenas")
mapa.add_edge("Punta Arenas","Viña del Mar")
mapa.add_edge("Iquique","Antofagasta")
mapa.add_edge("Puerto Varas","La Serena")
mapa.add_edge("Constitucion","Osorno")
mapa.add_edge("Frutillar","Santiago")
mapa.add_edge("Arica","Puerto Montt")
mapa.add_edge("Futrono","Arica")
mapa.add_edge("Entre Lagos","Punta Arenas")
mapa.add_edge("Valdivia", "Entre Lagos")

inicio = time.time()
print(BEA(mapa,"Los Muermos", "Concepcion"))
fin = time.time()
print(fin,inicio, fin-inicio)

nx.draw(mapa, with_labels=True)
pyl.show()