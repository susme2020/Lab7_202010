"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller 
import csv
from ADT import list as lt
from ADT import orderedmap as map
from DataStructures import listiterator as it

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("\nBienvenido al Laboratorio 7")
    print("1- Cargar información")
    print("2- Contar nodos y enlances cargados")
    print("3- Consultar cantidad de clusters (componentes conectados)")
    print("4- Insertar un nodo (vértice)")
    print("5- Crear un enlace (arco)")
    print("6- DFS")
    print("0- Salir")


def initCatalog ():
    """
    Inicializa el catalogo
    """
    return controller.initCatalog()


def loadData (catalog):
    """
    Carga los vuelos en la estructura de datos
    """
    controller.loadData(catalog)


"""
Menu principal 
""" 
def main():
    datos_cargados = False
    while True: 
        printMenu()
        if not datos_cargados:
            print("\nTodavía no se han cargado los datos")
        inputs =input('Seleccione una opción para continuar\n')
        if int(inputs[0])==1: # 1- Cargar información
            if datos_cargados:
                print("Ya se han cargado los datos previamente")
            else:
                print("Cargando información de los archivos ....")
                catalog = initCatalog ()
                loadData (catalog)
                datos_cargados = True
        elif int(inputs[0])==2: # 2- Contar nodos y enlances cargados
            if datos_cargados:
                nodes,edges = controller.countNodesEdges(catalog) 
                print("El grafo tiene: ", nodes," nodos y", edges," enlaces")
            else:
                print("No ha cargado los datos todavía")
        elif int(inputs[0])==3: # 3- Consultar cantidad de clusters (componentes conectados)
            if datos_cargados:
                ccs = controller.countConnectedComponents(catalog)
                print("El grafo tiene :", ccs, 'componentes conectados')
            else:
                print("No ha cargado los datos todavía")
        elif int(inputs[0])==4: # 4- Insertar un nodo (vértice)
            if datos_cargados:
                vertice = input("Digite el vértice que desea agregar a los datos: ")
                controller.addFlightNode_user(catalog, vertice)
            else:
                print("No ha cargado los datos todavía")
        elif int(inputs[0])==5: # 5- Crear un enlace (arco)
            if datos_cargados:
                vertice1 = input("Digite el vértice fuente del enlace: ")
                vertice2 = input("Digite el vértice destino del enlace: ")
                valor = int(input("Digite el valor del enlace que desea crear: "))
                controller.addFlightEdge_user(catalog, vertice1, vertice2, valor)
            else:
                print("No ha cargado los datos todavía")
        elif int(inputs[0])==6: # 6- DFS
            if datos_cargados:
                vertice = input("Digite el vértice fuente del DFS: ")
                controller.DFS(catalog, vertice)
            else:
                print("No ha cargado los datos todavía")
        else:
            sys.exit(0)
    sys.exit(0)

if __name__ == "__main__":
    main()