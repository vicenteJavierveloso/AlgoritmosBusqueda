import os
import dill

def guardar_arbol(arbol):
    ruta_archivo = os.path.dirname(__file__)
    directorio = f"{ruta_archivo}/arboles"
    #Intenta crear la carpeta donde se almacenan por defecto los arboles
    try:
        os.mkdir(directorio)
    except FileExistsError:
        pass
    contador_archivos = len(os.listdir(directorio))
    try:
        nombre_archivo = f"arbol{contador_archivos}.pkl"
        archivo_temp = open(f"{directorio}/{nombre_archivo}","x")
        archivo_temp.close()
    except FileExistsError:
        #Si el archivo existe previamente no se puede sobreescribir directamente
        return False
    #Guarda la lista en formato csv
    archivo = open(f"{directorio}\{nombre_archivo}","wb")
    dill.dump(arbol,archivo)
    archivo.close()
    return True

def cargar_arbol(ruta):
    archivo = open(ruta, "rb")
    arbol = dill.load(archivo)
    return arbol