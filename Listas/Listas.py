def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i  
    return -1  

def busqueda_binaria(lista, elemento):
    lista_ordenada = sorted(lista)
    print(
        lista_ordenada
    )
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista_ordenada[medio] == elemento:
            return medio  
        elif lista_ordenada[medio] < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1  

# Ejemplo de uso con lista de cadenas
lista_cadenas = ["manzana", "uva", "cereza", "banana"]
elemento_cadena = "uva"
resultado_cadena = busqueda_binaria(lista_cadenas, elemento_cadena)
if resultado_cadena != -1:
    print(f"El elemento {elemento_cadena} se encuentra en el índice {resultado_cadena}.")
else:
    print(f"El elemento {elemento_cadena} no está en la lista.")