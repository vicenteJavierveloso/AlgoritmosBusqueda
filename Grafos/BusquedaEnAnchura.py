import networkx as nx

import time

# print(f"{list(mapa.neighbors('Osorno'))}")

#Se necesita un nodo raiz y tres listas donde clasificar los nodos mientras se vaya buscando
#Actualmente esta funcion solo determina si el elemento esta o no esta en el grafo
#Sacado de https://madi.nekomath.com/P5/BFS.html
def BEA(grafo:nx.Graph,raiz:str, elemento:str) -> bool:
    #Cuando se llama a la funcion
    por_procesar = [raiz] # Vertices por procesar
    encontrados = [raiz] # Nodos que se encontraron pero aun no se han procesado
    procesado = [] # Nodos que se procesaron
    elemento_encontrado = False
    while len(por_procesar) > 0:
        nodo_actual = por_procesar[0]
        if nodo_actual == elemento:
            elemento_encontrado = True
            break
        #antes de procesar el nodo actual determina si este corresponde al que se busca
        #En general para todo el algoritmo aqui es donde se debe verificar lo que se esta buscando
        # if nodo_actual == elemento:
        #     elemento_encontrado = True
        # else:
        #     elemento_encontrado = False
        for i in grafo.neighbors(nodo_actual): #Por cada uno de los vecinos del nodo actual
            if i not in procesado: #Si algun vecino del nodo actual no esta en los nodos procesados, añadirlo
                if i not in encontrados: #Si algun vecino del nodo actual no esta en los nodos encontrados, añadirlo
                    encontrados.append(i)
                    por_procesar.append(i)
        #Luego de que se proceso el nodo actual
        por_procesar.remove(nodo_actual)
        procesado.append(nodo_actual)
    #Cuando va a retornar
    return elemento_encontrado

# print(BEA(mapa,"Los Muermos", "Temuco"))