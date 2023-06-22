import time

class Buscador:
    def __init__(self, lista):
        self.lista = lista

    def busqueda_lineal(self, elementos):
        resultados = []
        inicio = time.time()

        for elemento in elementos:
            for i, item in enumerate(self.lista):
                if item == elemento:
                    resultados.append((elemento, i))
                    break

        tiempo_ejecucion = time.time() - inicio
        return resultados, tiempo_ejecucion

    def busqueda_binaria(self, elementos):
        resultados = []
        inicio = time.time()

        for elemento in elementos:
            inicio = 0
            fin = len(self.lista) - 1

            while inicio <= fin:
                medio = (inicio + fin) // 2
                if self.lista[medio] == elemento:
                    resultados.append((elemento, medio))
                    break
                elif self.lista[medio] < elemento:
                    inicio = medio + 1
                else:
                    fin = medio - 1

        tiempo_ejecucion = time.time() - inicio
        return resultados, tiempo_ejecucion
mi_lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
buscador = Buscador(mi_lista)

elementos = [12, 6, 18]

resultados_lineal, tiempo_lineal = buscador.busqueda_lineal(elementos)
print("Resultados de búsqueda lineal:")
for elemento, indice in resultados_lineal:
    print(f"El elemento {elemento} fue encontrado en el índice {indice}")
print(f"Tiempo de ejecución (búsqueda lineal): {tiempo_lineal} segundos")

resultados_binaria, tiempo_binaria = buscador.busqueda_binaria(elementos)
print("Resultados de búsqueda binaria:")
for elemento, indice in resultados_binaria:
    print(f"El elemento {elemento} fue encontrado en el índice {indice}")
print(f"Tiempo de ejecución (búsqueda binaria): {tiempo_binaria} segundos")
