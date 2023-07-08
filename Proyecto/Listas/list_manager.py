import csv
import os

def guardar_lista(lista:list):
    ruta_archivo = os.path.dirname(__file__)
    directorio = f"{ruta_archivo}\listas"
    #Intenta crear la carpeta donde se almacenan por defecto las listas
    try:
        os.mkdir(directorio)
    except FileExistsError:
        pass
    contador_archivos = len(os.listdir(directorio))
    try:
        nombre_archivo = f"lista{contador_archivos}.csv"
        archivo_temp = open(f"{directorio}\{nombre_archivo}","x")
        archivo_temp.close()
    except FileExistsError:
        #Si el archivo existe previamente no se puede sobreescribir directamente
        return False
    #Guarda la lista en formato csv
    archivo = open(f"{directorio}\{nombre_archivo}","w")
    writer = csv.writer(archivo)
    writer.writerow(lista)
    archivo.close()
    return True

def cargar_lista(ruta):
    archivo = open(ruta, "r")
    #lee la la lista contenida en el archivo csv
    lista = archivo.read()
    #limpia la lista de saltos de linea
    lista = lista.replace("\n","")
    #divide la lista basado en las comas
    lista = list(lista.split(","))
    return lista

if __name__ == "__main__":
    listaa = ["hola","como","estas"]
    guardar_lista(listaa)
    aux = cargar_lista(f"{os.path.dirname(__file__)}/listas/lista0.csv")
    print(aux)