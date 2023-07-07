import networkx as nx
import time

#Funcion que una vez retornado el diccionario que contiene los padres de cada
#Nodo en el grafo, realiza un camino y lo agrega a una lista
def Camino(padres, elemento, camino=[]):
    #padres sera un diccionario, elemento es el elemento a buscar o nodo objetivo
    #camino sera una variable auxiliar que contendra el camino durante toda la recursion
    #Si el elemento se encuentra en el diccionario padres
    if elemento in padres:
        #añadir a la lista auxiliar EL VALOR DEL ELEMENTO EN EL DICCIONARIO PADRES, este corresponde a su padre
        camino.append(padres[elemento])
        #si el valor es None, entonces ese nodo no tiene padres
        #asi que se retorna la lista
        if padres[elemento] == None:
            return camino
        #si el valor es distinto de None
        #el elemento pasa a ser el padre del elemento anterior
        #y se llama recursivamente en el mismo diccionario padres
        #pasando el nuevo elemento y la lista auxiliar
        else:    
            elemento = padres[elemento]
            Camino(padres,elemento,camino)
    #Una vez que termina el algoritmo se retorna la lista con el camino
    #se corta la lista en el ultimo elemento porque este siempre sera None
    #ya que se llega a un nodo sin padre y la funcion solo lo añadira sin mas
    return camino[:-1]


#Funcion que implementa el algoritmo principal Busqueda en profundidad
#se deben pasar varios parametros ya que se trata de un algoritmo recursivo por naturaleza
#el grafo a trabajar, la raiz o nodo raiz, el elemento a buscar, los nodos encontrados, los padres de los nodos procesados y el tiempo
#Que se guardara en una primera instancia apenas se ejecute el algoritmo por primera vez.
def BEP(grafo:nx.Graph,raiz:str, elemento:str,encontrados = [], padres={}, t0 =0):
    #si el tiempo es 0
    #cambia la variable por primera vez, luego no la cambia mas,
    #pero sera pasado a la siguiente llamada recursiva de la funcion
    if t0 == 0:
        t0 = time.perf_counter()
    try:
        #Si la lista de nodos encontrados esta vacia en primera instancia
        #se añade el nodo raiz a la lista
        #ademas el diccionario padres se le añade una llave que indicara
        #el padre del nodo raiz que esta siendo procesado
        if encontrados == []:
            encontrados = [raiz] #nodos encontrados
            #Padres del nodo raiz
            padres[raiz] = None
        #
        #por cada vecino de el nodo raiz actual, si no se encuentra en la lista de nodos
        #Encontrados, añadirlo a la lista de nodos encontrados
        for w in grafo.neighbors(raiz):
            if w not in encontrados:
                encontrados.append(w)
                #Padres del vecino w del nodo raiz
                #actualizar el padre de cada nodo vecino de la raiz actual, naturalmente
                #sera la raiz actual
                padres[w] = raiz
                #procesar de inmediato el nodo vecino, pasandolo como una nueva raiz
                #pasar tambien el grafo que se esta trabajando, el elemento que se sigue buscando para que no
                #se pierda, el diccionario de padres y el tiempo 0 (t0) para que no se pierda tambien
                BEP(grafo,w,elemento,encontrados, padres, t0)
        #finalmente se retorna una lista con los datos de interes
        #sacados del algoritmo
        #el diccionario con padres, que sera procesado luego por la funcion Camino(), el elemento que se esta buscando,
        #nuevamente para no perderlo y procesarlo en la siguiente funcion que entrega la informacion
        #procedente del algoritmo de manera entendible (BEP_format())
        #y finalmente el tiempo de ejecucion del algoritmo que tambien sera procesada en 
        #BEP_format()
        return [True, [padres,elemento, time.perf_counter()-t0]]
    except nx.exception.NetworkXError:
        return [False,time.perf_counter()-t0]


#funcion que da formato y entrega de manera entendible los datos
# obtenidos en la ejecucion del algoritmo
def BEP_format(input):
    if input[0] == True:
        #el diccionario padres es procesado con la funcion Camino()
        camino = Camino(input[1][0],input[1][1])
        #se inserta el elemento que se estaba buscando en un principio para formar un camino
        camino.insert(0,input[1][1])
        #se invierte el orden de la lista para darle el formato
        #de nodo origen -> nodo objetivo
        camino.reverse()
        #retorna la informacion y el tiempo
        if input[1][1] in input[1][0]:
            return f"El camino para llegar al nodo {input[1][1]} es {camino}. Tiempo: {input[1][2]*1000}ms"
        else:
            return f"El nodo no se encuentra en el grafo. Tiempo: {input[1][2]*1000}ms"
    else:
        return f"El nodo raiz proporcionado no existe en el grafo. Tiempo: {input[1]*1000}ms"