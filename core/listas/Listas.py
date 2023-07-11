import time
#Recorre la lista utilizando un bucle for y verifica si cada elemento es igual al elemento buscado.
# Si encuentra una coincidencia, devuelve el índice correspondiente donde se encontró el elemento.
def busqueda_lineal(lista, elemento):
    t0 = time.perf_counter()
    for i in range(len(lista)):
        if lista[i] == elemento:
            return [i,(time.perf_counter()-t0)*1000] # El índice donde se encuentra el elemento
    return [-1,(time.perf_counter()-t0)*1000]  # Si el elemento no está en la lista
                                                # retorna -1 y el tiempo del algoritmo

def busqueda_binaria(lista, elemento):
    t0 = time.perf_counter()
    lista_ordenada = sorted(lista) # Ordenar la lista antes de la búsqueda binaria
    #Se establecen los índices inicio y fin para definir la sección actual en la que se está buscando.
    inicio = 0
    fin = len(lista) - 1
    #El bucle while se ejecuta mientras inicio sea menor o igual a fin. En cada iteración
    while inicio <= fin:
        # se calcula el índice medio de la sección actual. Si el elemento buscado es igual al elemento en el índice medio, se retorna el índice.
        medio = (inicio + fin) // 2 # Calcular el índice medio de la sección actual
        if lista_ordenada[medio] == elemento:
            return [medio,(time.perf_counter()-t0)*1000, lista_ordenada]  # El elemento buscado se encuentra en el índice medio 
        #Si el elemento buscado es mayor que el elemento en el índice medio, se actualiza el índice inicio para buscar en la mitad derecha de la sección actual.
        elif lista_ordenada[medio] < elemento:
            inicio = medio + 1 # El elemento buscado está en la mitad derecha de la sección
        #Si el elemento buscado es menor que el elemento en el índice medio, se actualiza el índice fin para buscar en la mitad izquierda de la sección actual.
        else:
            fin = medio - 1  # El elemento buscado está en la mitad izquierda de la sección
    return [-1,(time.perf_counter()-t0)*1000, lista_ordenada]  # Si el elemento no está en la lista 

# # Ejemplo de uso con datos numéricos
# lista_numerica = [5, 8, 2, 10, 1, 7, 3]
# elemento_numerico = 7

# resultado_lineal = busqueda_lineal(lista_numerica, elemento_numerico)
# resultado_binario = busqueda_binaria(lista_numerica, elemento_numerico)

# if resultado_lineal != -1:
#     print(f"La búsqueda lineal encontró el elemento {elemento_numerico} en el índice {resultado_lineal}.")
# else:
#     print(f"La búsqueda lineal no encontró el elemento {elemento_numerico} en la lista.")

# if resultado_binario != -1:
#     print(f"La búsqueda binaria encontró el elemento {elemento_numerico} en el índice {resultado_binario}.")
# else:
#     print(f"La búsqueda binaria no encontró el elemento {elemento_numerico} en la lista.")
    
# # Ejemplo de uso con datos de cadenas
# lista_cadenas = ["manzana", "banana", "cereza", "dátil", "uva", "zarzamora"]
# elemento_cadena = "banana"

# resultado_lineal = busqueda_lineal(lista_cadenas, elemento_cadena)
# resultado_binario = busqueda_binaria(lista_cadenas, elemento_cadena)

# if resultado_lineal != -1:
#     print(f"La búsqueda lineal encontró el elemento {elemento_cadena} en el índice {resultado_lineal}.")
# else:
#     print(f"La búsqueda lineal no encontró el elemento {elemento_cadena} en la lista.")

# if resultado_binario != -1:
#     print(f"La búsqueda binaria encontró el elemento {elemento_cadena} en el índice {resultado_binario}.")
# else:
#     print(f"La búsqueda binaria no encontró el elemento {elemento_cadena} en la lista.")