class arbol:
    def __init__(self, dato):
        self.dato = dato        #corresponde al dato del nodo
        self.izquierdo = None   #correspnde a un nodo izquierdo
        self.derecho = None     #correspnde a un nodo derecho
        # inician en None por que se deben agregar los datos al iniciar el programa

    def agregar_al_arbol(self, nuevodato, nodoactual): #nuevo dato es un valor que se ingresa en algun momento y puede variar
        if nuevodato < nodoactual.dato:    #si el dato es menor al dato del nodo(esto es recursivo) guardara el dato a la izquierda
            if nodoactual.izquierdo is None: #si no existe
                nodoactual.izquierdo = (nuevodato)#guarda directamente al nodo izquierdo
            else: #si existe
                self.agregar_al_arbol(nuevodato, nodoactual.izquierdo)#recorre cada vez el nodo izquierdo hasta encontrarlo vacio
        elif nuevodato > nodoactual.dato:#lo mismo pero con el derecho
            if nodoactual.derecho is None:#lo mismo pero con el derecho
                nodoactual.derecho = (nuevodato)#lo mismo pero con el derecho
            else:
                self.agregar_al_arbol(nuevodato, nodoactual.derecho)#lo mismo pero con el derecho
        else:#por si existe ya el dato
            print("El dato ya existe en el árbol.")


raiz=arbol(5)#crea una raiz del arbol
raiz.agregar_al_arbol(5,raiz)
def in_orden(self):
    pass
#busqueda(no se si todos los tipos),in orden, postordern,preorden
