#Recorre la lista utilizando un bucle for y verifica si cada elemento es igual al elemento buscado.
# Si encuentra una coincidencia, devuelve el índice correspondiente donde se encontró el elemento.
def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i # El índice donde se encuentra el elemento
    return -1  # Si el elemento no está en la lista

def busqueda_binaria(lista, elemento):
    lista_ordenada = sorted(lista) # Ordenar la lista antes de la búsqueda binaria
    print(lista_ordenada)
    #Se establecen los índices inicio y fin para definir la sección actual en la que se está buscando.
    inicio = 0
    fin = len(lista) - 1
    #El bucle while se ejecuta mientras inicio sea menor o igual a fin. En cada iteración
    while inicio <= fin:
        # se calcula el índice medio de la sección actual. Si el elemento buscado es igual al elemento en el índice medio, se retorna el índice.
        medio = (inicio + fin) // 2 # Calcular el índice medio de la sección actual
        if lista_ordenada[medio] == elemento:
            return medio  # El elemento buscado se encuentra en el índice medio 
        #Si el elemento buscado es mayor que el elemento en el índice medio, se actualiza el índice inicio para buscar en la mitad derecha de la sección actual.
        elif lista_ordenada[medio] < elemento:
            inicio = medio + 1 # El elemento buscado está en la mitad derecha de la sección
        #Si el elemento buscado es menor que el elemento en el índice medio, se actualiza el índice fin para buscar en la mitad izquierda de la sección actual.
        else:
            fin = medio - 1  # El elemento buscado está en la mitad izquierda de la sección
    return -1  # Si el elemento no está en la lista 

# Ejemplo de uso con lista de cadenas
lista_cadenas = ["manzana", "uva", "cereza", "banana"]
elemento_cadena = "uva"
resultado_cadena = busqueda_binaria(lista_cadenas, elemento_cadena)
if resultado_cadena != -1:
    print(f"El elemento {elemento_cadena} se encuentra en el índice {resultado_cadena}.")
else:
    print(f"El elemento {elemento_cadena} no está en la lista.")