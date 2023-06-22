import networkx as nx
import time

def Camino(padres, elemento, camino=[]):
    if elemento in padres:
        camino.append(padres[elemento])
        if padres[elemento] == None:
            return camino
        else:    
            elemento = padres[elemento]
            Camino(padres,elemento,camino)
    return camino[:-1]

def BEP(grafo:nx.Graph,raiz:str, elemento:str,encontrados = [], padres={}, t0 =0):
    if t0 == 0:
        t0 = time.perf_counter()
    if encontrados == []:
        encontrados = [raiz] #nodos encontrados
        #Padres del nodo raiz
        padres[raiz] = None
    # P = set() #nodos procesados

    for w in grafo.neighbors(raiz):
        if w not in encontrados:
            encontrados.append(w)
            #Padres del vecino w del nodo raiz
            padres[w] = raiz
            
            BEP(grafo,w,elemento,encontrados, padres, t0)
    #encontrados sera los nodos descubiertos en orden
    #padres, seran los padres de cada nodo, formando un camino
    #Falta ordenar el diccionario padres para formar una lista que determine un camino a seguir 
    #(no sera el camino optimo)

    return [padres,elemento]

def BEP_format(padres,elemento):
    return f"{Camino(padres, elemento)}"