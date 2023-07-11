import networkx as nx
import os

def guardar_grafo(grafo):
    ruta_archivo = os.path.dirname(__file__)
    directorio = f"{ruta_archivo}\grafos"
    #Intenta crear la carpeta donde se almacenan por defecto los grafos
    try:
        os.mkdir(directorio)
    except FileExistsError:
        pass
    contador_archivos = len(os.listdir(directorio))
    try:
        nombre_archivo = f"grafo{contador_archivos}.graphml"
        archivo_temp = open(f"{directorio}\{nombre_archivo}","x")
        archivo_temp.close()
    except FileExistsError:
        #Si el archivo existe previamente no se puede sobreescribir directamente
        return False
    #Guardar el grafo en un archivo .graphml
    #Una vez que lo guarda retorna True
    nx.write_graphml(grafo,f"{directorio}\{nombre_archivo}")
    return True

def cargar_grafo(ruta):
    grafo = nx.read_graphml(ruta)
    return grafo