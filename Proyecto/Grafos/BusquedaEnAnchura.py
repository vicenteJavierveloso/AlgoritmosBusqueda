import networkx as nx

import time

#Se necesita un nodo raiz y tres listas donde clasificar los nodos mientras se vaya buscando
#Sacado de https://madi.nekomath.com/P5/BFS.html
#elemento tiene que ser una llave de un diccionario

#Argumentos para el funcionamiento
#grafo: el grafo a procesar
#raiz: el nodo desde el cual comenzar la busqueda
#llave: la llave en que se debe encontrar el elemento en un diccionario
#elemento: el valor de la llave que se busca
def BEA(grafo:nx.Graph, raiz:str, llave:str, elemento):
    por_procesar = [raiz] # Nodos por procesar
    encontrados = [raiz] # Nodos que se encontraron pero aun no se han procesado
    procesado = [] # Nodos que se procesaron
    # Se utiliza la variable elemento_encontrado e inicializada con False para determinar si el elemento fue encontrado
    #durante la ejecucion del algoritmo o no
    elemento_encontrado = False
    #Utilizamos perf_counter del modulo time de python para medir el tiempo con precision
    # del reloj de la cpu en segundos de la ejecucion del algoritmo
    #Tiempo 0
    t0 = time.perf_counter()

    #Mientras existan nodos en la lista por procesar, ejecutar el ciclo
    while len(por_procesar) > 0:
        #El nodo de interes para procesar siempre sera el primero en la lista por_procesar
        # por lo que utilizamos por_procesar[0]
        
        #En esta pieza de codigo se determina que hacer si se encuentra un nodo de interes
        #en nuestro caso como los nodos pueden almacenar diccionarios, buscamos dentro de este diccionario
        #una llave especificada por el usuario y un valor que debe contener esta llave para que
        #El algoritmo retorne que el elemento fue encontrado con exito
        #
        # Si la longitud del diccionario que contiene el nodo actual (por_procesar[0]) es mayor a 0
        # es potencial a tener alguna llave con valores
        if len(grafo.nodes[por_procesar[0]]) > 0:
            #Si la llave buscada existe en el diccionario del nodo (por_procesar[0]), es potencial candidato
            # a tener el valor
            if llave in grafo.nodes[por_procesar[0]]:
                #Si finalmente la llave se encuentra en el diccionario del nodo, verificar el valor de la misma
                # y si es igual al valor buscado, detener el algoritmo y cambiar la variable elemento_encontrado
                # a True
                if grafo.nodes[por_procesar[0]][llave] == elemento:
                    elemento_encontrado = True
                    break
        
        #Por cada vecino del nodo actual, 
        for i in grafo.neighbors(por_procesar[0]):
            if i not in procesado: #Si algun vecino del nodo actual no esta en los nodos procesados, candidato a añadirlo 
                                    #a por_procesar y a encontrados
                if i not in encontrados: #Si algun vecino del nodo actual no esta en los nodos encontrados, añadirlo a 
                                        # a por procesar y a encontrados
                    encontrados.append(i)
                    por_procesar.append(i)

        #Luego de que se proceso el nodo actual
        #se elimina el nodo actual de la lista por_procesar[0]
        por_procesar.remove(por_procesar[0])
        #se añade el nodo actual a la lista procesado.
        procesado.append(por_procesar[0])
    
    #Tiempo 1
    t1 = time.perf_counter()

    if elemento_encontrado == True:
        return f"El elemento '{elemento}' de la llave '{llave}' fue encontrado en el grafo en el nodo '{por_procesar[0]}'. Tiempo: {(t1-t0)*1000}ms"
    else:
        return f"El elemento '{elemento}' de la llave '{llave}' no fue encontrado en el grafo. Tiempo: {(t1-t0)*1000}ms"