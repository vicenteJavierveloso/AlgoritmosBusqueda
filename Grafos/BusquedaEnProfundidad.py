import networkx as nx

def BEP(grafo:nx.Graph,raiz:str, encontrados = [], padres={}):
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
            
            BEP(grafo,w,encontrados, padres)
    #encontrados sera los nodos descubiertos en orden
    #padres, seran los padres de cada nodo, formando un camino
    #Falta ordenar el diccionario padres para formar una lista que determine un camino a seguir 
    #(no sera el camino optimo)
    return f"{padres}"