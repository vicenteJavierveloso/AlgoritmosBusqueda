from graph_manager import cargar_grafo, guardar_grafo
from BusquedaEnAnchura import BEA
from BusquedaEnProfundidad import BEP_format, BEP
import os
import networkx as nx
from matplotlib import pyplot as pyl

ruta = os.path.dirname(__file__)
ruta = f"{ruta}\grafos\grafo0.graphml"

grafo = cargar_grafo(ruta)

nx.draw(grafo, with_labels=True)
pyl.show()