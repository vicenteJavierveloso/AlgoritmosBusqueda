class NodoArbol:
    def __init__(self, dato):
        self.dato = dato        #corresponde al dato del nodo
        self.izquierdo = None   #correspnde a un nodo izquierdo
        self.derecho = None     #correspnde a un nodo derecho
        # inician en None por que se deben agregar los datos al iniciar el programa
class Arbol:
    def __init__(self, dato):
        self.raiz = NodoArbol(dato)#con esto creamos el primer valor del arbol,el que va mas arriba

    def agregar_al_arbol(self, dato, nodo):
        if dato < nodo.dato:    #si el dato es menor al dato del nodo(esto es recursivo) guardara el dato a la izquierda
            if nodo.izquierdo is None: #si no existe
                nodo.izquierdo = NodoArbol(dato)#guarda directamente al nodo izquierdo
            else: #si existe
                self.agregar_al_arbol(dato, nodo.izquierdo)#recorre cada vez el nodo izquierdo hasta encontrarlo vacio
        elif dato > nodo.dato:#lo mismo pero con el derecho
            if nodo.derecho is None:#lo mismo pero con el derecho
                nodo.derecho = NodoArbol(dato)#lo mismo pero con el derecho
            else:
                self.agregar_al_arbol(dato, nodo.derecho)#lo mismo pero con el derecho
        else:#por si existe ya el dato
            print("El dato ya existe en el árbol.")



#busqueda(no se si todos los tipos),in orden, postordern,preorden



