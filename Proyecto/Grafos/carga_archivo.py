import networkx as nx
from matplotlib import pyplot as pyl

# grafo = nx.read_pajek("datos/grafo.net")
# grafo = nx.read_graphml("datos/grafo.graphml")

#Formato graphml guarda atributos

grafo = nx.read_graphml("datos/grafo.graphml")

#verificar que los atributos continuan en los nodos correctos
print(grafo.nodes["Futrono"])

nx.draw(grafo, with_labels = True)
pyl.show()
