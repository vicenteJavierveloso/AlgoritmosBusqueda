import networkx as nx

import time

#Se necesita un nodo raiz y tres listas donde clasificar los nodos mientras se vaya buscando
#Actualmente esta funcion solo determina si el elemento esta o no esta en el grafo
#Sacado de https://madi.nekomath.com/P5/BFS.html
#elemento tiene que ser una llave de un diccionario
def BEA(grafo:nx.Graph, raiz:str, llave:str, elemento):
    por_procesar = [raiz] # Nodos por procesar
    encontrados = [raiz] # Nodos que se encontraron pero aun no se han procesado
    procesado = [] # Nodos que se procesaron
    elemento_encontrado = False

    #Utilizamos perf_counter del modulo time de python para medir el tiempo en segundos de la ejecucion del algoritmo
    #Tiempo 0
    t0 = time.perf_counter()

    while len(por_procesar) > 0:
        nodo_actual = por_procesar[0] 
        #antes de procesar el nodo actual determina si este corresponde al que se busca
        #En general para todo el algoritmo aqui es donde se debe verificar lo que se esta buscando

        # grafo.nodes[nodo_actual] entrega un diccionario
        if len(grafo.nodes[nodo_actual]) > 0:
            if llave in grafo.nodes[nodo_actual]:
                if grafo.nodes[nodo_actual][llave] == elemento:
                    elemento_encontrado = True
                    break

        for i in grafo.neighbors(nodo_actual): #Por cada uno de los vecinos del nodo actual
            if i not in procesado: #Si algun vecino del nodo actual no esta en los nodos procesados, añadirlo
                if i not in encontrados: #Si algun vecino del nodo actual no esta en los nodos encontrados, añadirlo
                    encontrados.append(i)
                    por_procesar.append(i)
        #Luego de que se proceso el nodo actual
        por_procesar.remove(nodo_actual)
        procesado.append(nodo_actual)
    
    #Tiempo 1
    t1 = time.perf_counter()

    if elemento_encontrado == True:
        return f"El elemento {elemento} de la llave {llave} fue encontrado en el grafo en el nodo {nodo_actual}. Tiempo: {(t1-t0)*1000}ms"
    else:
        return f"El elemento {elemento} de la llave {llave} no fue encontrado en el grafo. Tiempo: {(t1-t0)*1000}ms"