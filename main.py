from core.listas.list_manager import cargar_lista
from core.listas.Listas import busqueda_lineal, busqueda_binaria
from core.grafos.graph_manager import cargar_grafo

from core.grafos.BusquedaEnAnchura import BEA
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QStackedLayout, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QWidget, QFileDialog, QLineEdit, QComboBox, QGroupBox, 
                             QPlainTextEdit, QMessageBox)
import networkx as nx
import matplotlib.pyplot as pyl

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Programa de Algoritmos de busqueda")
        self.setFixedSize(900,600)

        #Ventnas adicionales

        #Ventana listas
        #
        #
        #
        #
        #
        #

        ventana_listas = QWidget()

        label_1_listas = QLabel("Archivo de entrada")

        self.archivo_listas = QFileDialog()
        examinar_listas = QPushButton("Examinar")
        examinar_listas.clicked.connect(lambda: self.archivo_listas.show())

        self.archivo_listas.fileSelected.connect(self.actualizar_ruta_listas)

        self.label_ruta_listas = QLabel("")
        self.label_ruta_listas.setFrameStyle(1)
        self.label_ruta_listas.setStyleSheet("QLabel { border: 1px solid gray; color: black; background-color: white }")

        label_2_listas = QLabel("Elemento a buscar")

        self.elemento_listas = QLineEdit()

        self.algoritmo_listas = QComboBox()
        self.algoritmo_listas.addItems(["Busqueda Binaria", "Busqueda Lineal"])

        boton_buscar_listas = QPushButton("Buscar")
        boton_buscar_listas.clicked.connect(self.buscar_listas)

        salida_listas = QGroupBox("Salida")

        self.output_listas = QPlainTextEdit()
        self.output_listas.setReadOnly(True)

        output_listas_layout = QVBoxLayout()
        output_listas_layout.addWidget(self.output_listas)

        salida_listas.setLayout(output_listas_layout)

        #layout
        layout_principal_listas = QGridLayout()

        layout_principal_listas.addWidget(label_1_listas,0,0)
        layout_principal_listas.addWidget(examinar_listas,0,2)
        layout_principal_listas.addWidget(self.label_ruta_listas,0,1)
        layout_principal_listas.addWidget(label_2_listas,1,0)
        layout_principal_listas.addWidget(self.elemento_listas,1,1)
        layout_principal_listas.addWidget(self.algoritmo_listas,2,1)
        layout_principal_listas.addWidget(boton_buscar_listas,3,1)

        layout_principal_listas.addWidget(salida_listas,4,1)
        

        ventana_listas.setLayout(layout_principal_listas)

        #ventana grafos
        #
        #
        #
        #
        #
        #
        #
        ventana_grafos = QWidget()
        #elementos

        label_1_grafos = QLabel("Archivo de entrada")

        self.archivo_grafos = QFileDialog()
        examinar_grafos = QPushButton("Examinar")
        examinar_grafos.clicked.connect(lambda: self.archivo_grafos.show())

        self.archivo_grafos.fileSelected.connect(self.actualizar_ruta_grafos)

        self.label_ruta_grafos = QLabel("")
        self.label_ruta_grafos.setFrameStyle(1)
        self.label_ruta_grafos.setStyleSheet("QLabel { border: 1px solid gray; color: black; background-color: white }")

        label_2_BEP = QLabel("Elemento a buscar")
        label_3_raiz_BEP = QLabel("Raiz")
        label_2_BEA = QLabel("Elemento a buscar")
        label_2_BEA_llave = QLabel("Llave donde buscar")
        label_3_raiz_BEA = QLabel("Raiz")


        self.elemento_BEP = QLineEdit()
        self.elemento_BEA = QLineEdit()
        self.llave_BEA = QLineEdit()

        self.raiz_BEP = QLineEdit()
        self.raiz_BEA = QLineEdit()

        self.algoritmo_grafos = QComboBox()
        self.algoritmo_grafos.addItems(["Busqueda en Profundidad", "Busqueda en Anchura"])

        self.algoritmo_grafos.currentTextChanged.connect(self.cambiar_layout_busqueda)

        boton_buscar_grafos = QPushButton("Buscar")
        boton_buscar_grafos.clicked.connect(self.buscar_grafos)

        salida_grafos = QGroupBox("Salida")

        self.output_grafos = QPlainTextEdit()
        self.output_grafos.setReadOnly(True)

        output_grafos_layout = QVBoxLayout()
        output_grafos_layout.addWidget(self.output_grafos)

        salida_grafos.setLayout(output_grafos_layout)

        #layout
        layout_principal_grafos = QGridLayout()

        #Busqueda en profundidad busca un nodo -> elemento sera nodo a buscar
        #busqueda en anchura busca un elemento en una llave de un nodo -> elemento y llave seran dos a buscar

        self.layout_busqueda = QStackedLayout()

        layout_BEA = QHBoxLayout()
        layout_BEA.addWidget(label_2_BEA)
        layout_BEA.addWidget(self.elemento_BEA)
        layout_BEA.addWidget(label_2_BEA_llave)
        layout_BEA.addWidget(self.llave_BEA)
        layout_BEA.addWidget(label_3_raiz_BEA)
        layout_BEA.addWidget(self.raiz_BEA)
        layout_BEA_widget = QWidget()
        layout_BEA_widget.setLayout(layout_BEA)

        layout_BEP = QHBoxLayout()
        layout_BEP.addWidget(label_2_BEP)
        layout_BEP.addWidget(self.elemento_BEP)
        layout_BEP.addWidget(label_3_raiz_BEP)
        layout_BEP.addWidget(self.raiz_BEP)
        layout_BEP_widget = QWidget()
        layout_BEP_widget.setLayout(layout_BEP)

        self.layout_busqueda.addWidget(layout_BEP_widget) #0
        self.layout_busqueda.addWidget(layout_BEA_widget) #1

        layout_busqueda_widget = QWidget()
        layout_busqueda_widget.setLayout(self.layout_busqueda)

        layout_principal_grafos.addWidget(label_1_grafos,0,0)
        layout_principal_grafos.addWidget(self.label_ruta_grafos,0,1)
        layout_principal_grafos.addWidget(examinar_grafos,0,2)
        layout_principal_grafos.addWidget(layout_busqueda_widget,1,1)
        layout_principal_grafos.addWidget(self.algoritmo_grafos,2,1)
        layout_principal_grafos.addWidget(boton_buscar_grafos,3,1)

        layout_principal_grafos.addWidget(salida_grafos,4,1)


        ventana_grafos.setLayout(layout_principal_grafos)

        #ventana arboles
        #
        #
        #
        #
        #
        #
        #
        #
        #
        ventana_arboles = QWidget()

        label_1_arboles = QLabel("Archivo de entrada")

        self.archivo_arboles = QFileDialog()
        examinar_arboles = QPushButton("Examinar")
        examinar_arboles.clicked.connect(lambda: self.archivo_arboles.show())

        self.archivo_arboles.fileSelected.connect(self.actualizar_ruta_arboles)

        self.label_ruta_arboles = QLabel("")
        self.label_ruta_arboles.setFrameStyle(1)
        self.label_ruta_arboles.setStyleSheet("QLabel { border: 1px solid gray; color: black; background-color: white }")

        label_2_arboles = QLabel("Elemento a buscar")

        elemento_arboles = QLineEdit()

        algoritmo_arboles = QComboBox()
        algoritmo_arboles.addItems(["Busqueda Binaria"])

        boton_buscar_arboles = QPushButton("Buscar")
        boton_buscar_arboles.clicked.connect(self.buscar_arboles)

        salida_arboles = QGroupBox("Salida")

        output_arboles = QPlainTextEdit()
        output_arboles.setReadOnly(True)

        output_arboles_layout = QVBoxLayout()
        output_arboles_layout.addWidget(output_arboles)

        salida_arboles.setLayout(output_arboles_layout)

        #layout
        layout_principal_arboles = QGridLayout()

        layout_principal_arboles.addWidget(label_1_arboles,0,0)
        layout_principal_arboles.addWidget(examinar_arboles,0,2)
        layout_principal_arboles.addWidget(self.label_ruta_arboles,0,1)
        layout_principal_arboles.addWidget(label_2_arboles,1,0)
        layout_principal_arboles.addWidget(elemento_arboles,1,1)
        layout_principal_arboles.addWidget(algoritmo_arboles,2,1)
        layout_principal_arboles.addWidget(boton_buscar_arboles,3,1)

        layout_principal_arboles.addWidget(salida_arboles,4,1)

        ventana_arboles.setLayout(layout_principal_arboles)

        
        #Elementos 
        #Botones
        self.boton_listas = QPushButton("Listas")
        self.boton_grafos = QPushButton("Grafos")
        self.boton_arboles = QPushButton("Arboles")

        self.boton_listas.clicked.connect(lambda: self.cambiar_indice_layout("listas"))
        self.boton_grafos.clicked.connect(lambda: self.cambiar_indice_layout("grafos"))
        self.boton_arboles.clicked.connect(lambda: self.cambiar_indice_layout("arboles"))

        #Labels
        titulo_subtitulo = QLabel("Bienvenido\nSeleccione la estructura a trabajar")
        #Config labels
        titulo_subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Layouts
        botones = QHBoxLayout()
        botones.addWidget(self.boton_listas)
        botones.addWidget(self.boton_grafos)
        botones.addWidget(self.boton_arboles)
        botones_widget = QWidget()

        botones_widget.setLayout(botones)

        #ventanas
        #Stack con diferentes ventanas para interactuar con el programa
        self.ventanas = QStackedLayout()

        #ventana de bienvenida al abrir el programa
        ventanas_bienvenida = QVBoxLayout()
        ventanas_bienvenida.addWidget(titulo_subtitulo)

        ventanas_bienvenida_widget = QWidget()
        ventanas_bienvenida_widget.setLayout(ventanas_bienvenida)
        
        #Aqui se añaden los layouts en forma de widgets
        self.ventanas.addWidget(ventanas_bienvenida_widget) #0
        self.ventanas.addWidget(ventana_listas) #1
        self.ventanas.addWidget(ventana_grafos) #2
        self.ventanas.addWidget(ventana_arboles) #3

        ventanas_widget = QWidget()
        ventanas_widget.setLayout(self.ventanas)

        #Layout principal
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(botones_widget)
        layout_principal.addWidget(ventanas_widget)
        
        layout_principal_widget = QWidget()
        layout_principal_widget.setLayout(layout_principal)

        self.setCentralWidget(layout_principal_widget)

    def cambiar_indice_layout(self,modo):
        if modo == "listas":
            self.ventanas.setCurrentIndex(1)
        elif modo == "grafos":
            self.ventanas.setCurrentIndex(2)
        elif modo == "arboles":
            self.ventanas.setCurrentIndex(3)

    def cambiar_layout_busqueda(self):
        if self.algoritmo_grafos.currentText() == "Busqueda en Profundidad":
            self.layout_busqueda.setCurrentIndex(0)
        elif self.algoritmo_grafos.currentText() == "Busqueda en Anchura":
            self.layout_busqueda.setCurrentIndex(1)

    def actualizar_ruta_listas(self):
        self.label_ruta_listas.setText(self.archivo_listas.selectedFiles()[0])

    def actualizar_ruta_grafos(self):
        self.label_ruta_grafos.setText(self.archivo_grafos.selectedFiles()[0])
    
    def actualizar_ruta_arboles(self):
        self.label_ruta_arboles.setText(self.archivo_arboles.selectedFiles()[0])

    #las siguientes funciones permiten utilizar los algoritmos de busqueda, la salida o resultados se escriben en el widget
    #QPlainText de cada seccion (lista, grafo o arbol)
    def buscar_listas(self):
        lista = cargar_lista(self.archivo_listas.selectedFiles()[0])
        if self.algoritmo_listas.currentText() == "Busqueda Lineal":
            if self.elemento_listas.isModified() == True:
                busqueda = busqueda_lineal(lista,self.elemento_listas.text())
                if busqueda[0] != -1:
                    self.output_listas.setPlainText(f"La lista ingresada fue: {lista}\nEl algoritmo encontro el elemento en la lista en el indice {busqueda[0]}. Tiempo de ejecucion {busqueda[1]}ms")
                else:
                    self.output_listas.setPlainText(f"La lista ingresada fue: {lista}\nEl elemento no fue encontrado en la lista. Tiempo de ejecucion: {busqueda[1]}ms")
            else:
                QMessageBox.warning(self,"Error", "Debe ingresar un elemento a buscar")

        elif self.algoritmo_listas.currentText() == "Busqueda Binaria":
            if self.elemento_listas.isModified() == True:
                busqueda = busqueda_binaria(lista,self.elemento_listas.text())
                if busqueda[0] != -1:
                    self.output_listas.setPlainText(f"La lista ingresada fue: {lista}\nLa lista ordenada segun el algoritmo es: {busqueda[2]}\nEl algoritmo encontro el elemento en la lista en el indice {busqueda[0]}. Tiempo de ejecucion {busqueda[1]}ms")
                else:
                    self.output_listas.setPlainText(f"La lista ingresada fue: {lista}\nLa lista ordenada segun el algoritmo es: {busqueda[2]}\nEl elemento no fue encontrado en la lista. Tiempo de ejecucion: {busqueda[1]}ms")
            else:
                QMessageBox.warning(self,"Error", "Debe ingresar un elemento a buscar")

    def buscar_grafos(self):
        grafo = cargar_grafo(self.archivo_grafos.selectedFiles()[0])
        if self.algoritmo_grafos.currentText() == "Busqueda en Profundidad":
            #Para solucionar resultados erroneos al ejecutar nuevamente el algoritmo se importa el mismo algoritmo aqui
            import core.grafos.BusquedaEnProfundidad
            busqueda = core.grafos.BusquedaEnProfundidad.BEP(grafo,self.raiz_BEP.text(),self.elemento_BEP.text())
            busqueda_formatted = core.grafos.BusquedaEnProfundidad.BEP_format(busqueda)
            self.output_grafos.setPlainText(busqueda_formatted)

            #Una vez que se utilizo y se entrego un resultado se desimporta el modulo
            sys.modules.pop('core.grafos.BusquedaEnProfundidad')

            nx.draw(grafo,with_labels=True)
            pyl.show()
        elif self.algoritmo_grafos.currentText() == "Busqueda en Anchura":
            busqueda = BEA(grafo,self.raiz_BEA.text(),self.llave_BEA.text(),self.elemento_BEA.text())
            self.output_grafos.setPlainText(busqueda)

            nx.draw(grafo,with_labels=True)
            pyl.show()

    def buscar_arboles(self):
        archivo = open(self.archivo_arboles.selectedFiles()[0])
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    app.exec()
        
