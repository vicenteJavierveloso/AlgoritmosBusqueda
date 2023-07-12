from time import perf_counter
try:
    from .tree_manager import cargar_arbol, guardar_arbol
except ImportError:
    from tree_manager import cargar_arbol, guardar_arbol

class Arbol:
    def __init__(self, dato):
        self.dato = dato        #corresponde al dato del nodo
        self.izquierdo = None   #correspnde a un nodo izquierdo
        self.derecho = None     #correspnde a un nodo derecho
        # inician en None por que se deben agregar los datos al iniciar el programa

    def agregar_al_arbol(self, nuevodato, nodoactual): #nuevo dato es un valor que se ingresa en algun momento y puede variar
        if nuevodato < nodoactual.dato:    #si el dato es menor al dato del nodo(esto es recursivo) guardara el dato a la izquierda
            if nodoactual.izquierdo is None: #si no existe
                nodoactual.izquierdo = Arbol(nuevodato)#guarda directamente al nodo izquierdo
            else: #si existe
                self.agregar_al_arbol(nuevodato, nodoactual.izquierdo)#recorre cada vez el nodo izquierdo hasta encontrarlo vacio
        elif nuevodato > nodoactual.dato:#lo mismo pero con el derecho
            if nodoactual.derecho is None:#lo mismo pero con el derecho
                nodoactual.derecho = Arbol(nuevodato)#lo mismo pero con el derecho
            else:
                self.agregar_al_arbol(nuevodato, nodoactual.derecho)#lo mismo pero con el derecho
        else:#por si existe ya el dato
            print("El dato ya existe en el árbol.")

def buscar_en_arbol(nodo_raiz,busqueda):
    t0 = perf_counter()
    #nodo_raiz es la raiz desde la cual comenzar a buscar
    if nodo_raiz is None:
        return [None,(perf_counter()-t0)*1000] #si no hay nodo algunodirectamente salta un none
    if nodo_raiz.dato == busqueda:
        return [busqueda,(perf_counter()-t0)*1000] #retorna la busqueda despues de pasar por la recursividad de abajo
    if nodo_raiz.dato<busqueda:
        return buscar_en_arbol(nodo_raiz.derecho,busqueda) # si en el anterior ir el nodo no es igual, verifica si el
                                                        #valor es mayor al actual nodo, si lo es la nueva vuelve a inciar la busqueda empezando
                                                        #del nodo que ha comparado
    else:
        return buscar_en_arbol(nodo_raiz.izquierdo,busqueda)#lo mismo pero si la busqueda fuera menor

if __name__ == "__main__":
    num=int(input("cuantos datos desea agregar"))



    for i in range(1):#se crea un ciclo for para que despues de preguntar cuantos 
                      #datos desea insertar pregunte por la raiz contandola dentro de la cantidad                 
        a=input("ingrese el dato que quiere para la raiz")                                
        raiz=Arbol(a)
        for i in range(num-1):#aqui comienza agregar los datos con la cantidad menos un valor para que sea la cantiodad correcta
            b=input("ingrese dato para agregar")
            raiz.agregar_al_arbol(b,raiz)


    c=input(" ingrese dato que desea buscar")
    resultado=buscar_en_arbol(raiz,c)
    if resultado:
        print(f"el dato {resultado} ha sido Encontrado")
    else:

        print(f"No se encuentra el dato {resultado}")
    
    guardar_arbol(raiz)

    #busqueda(no se si todos los tipos),in orden, postordern,preorden
    #eso mustra el recorrido