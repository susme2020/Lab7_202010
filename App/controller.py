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
import model
import csv
from ADT import list as lt
from ADT import map as map


from DataStructures import listiterator as it
from Sorting import mergesort as sort
from time import process_time


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Funcionaes utilitarias

def printList (lst):
    iterator = it.newIterator(lst)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
        print (result)


# Funciones para la carga de datos 

def loadBookReviews (catalog, sep=';'):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por 
    cada uno de ellos, se crea un arbol de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    t1_start = process_time() #tiempo inicial
    booksfile = cf.data_dir + 'GoodReads/book_reviews.csv'
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(booksfile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            model.addReviewNode(catalog, row)
            model.addReviewEdge(catalog, row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución carga de grafo de revisiones de libros:",t1_stop-t1_start," segundos")

def loadFlights (catalog, sep=';'):
    """
    Carga los vuelos del archivo.
    """
    t1 = process_time() #tiempo inicial
    flightsfile = cf.data_dir + 'Flights/flights_nodes.csv'
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(flightsfile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            addFlightNode(catalog, row)
    t2 = process_time() #tiempo final para vértices
    print("Tiempo de ejecución carga de vértices en el grafo de vuelos:",t2-t1," segundos") 

    t3 = process_time() #tiempo inicial para arcos
    flightsfile = cf.data_dir + 'Flights/flights_edges.csv'
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(flightsfile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            addFlightEdge(catalog, row)
    t4 = process_time() #tiempo final para carga de vértices y arcos
    print("Tiempo de ejecución carga de arcos en el grafo de vuelos:",t4-t3," segundos")

    print("Tiempo de ejecución total para carga del grafo de vuelos:",t4-t1," segundos")

def initCatalog ():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

def loadData (catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    #loadBookReviews(catalog)
    loadFlights(catalog)   

# Funciones llamadas desde la vista y enviadas al modelo


def countNodesEdges(catalog):
    t1_start = process_time() #tiempo inicial
    nodes, edges = model.countNodesEdges(catalog)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución de conteo de componentes conectados:",t1_stop-t1_start," segundos")
    return nodes, edges


def countConnectedComponents(catalog):
    t1_start = process_time() #tiempo inicial
    ccs = model.countConnectedComponents(catalog) 
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución de conteo de componentes conectados:",t1_stop-t1_start," segundos")
    return ccs

def addFlightNode(catalog, row):
    return model.addFlightNode(catalog, row)

def addFlightEdge (catalog, row):
    return model.addFlightEdge(catalog, row)

def addFlightNode_user(catalog, vertice):
    t1_start = process_time() #tiempo inicial
    estaba = model.addFlightNode_user(catalog, vertice)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución de la inserción del vértice:",t1_stop-t1_start," segundos")
    if estaba:
        print("El vértice no fue agregado debido a que ya existe")
    else:
        print("El vértice fue agregado exitosamente")

def addFlightEdge_user(catalog, vertice1, vertice2, valor):
    t1_start = process_time() #tiempo inicial
    model.addFlightEdge_user(catalog, vertice1, vertice2, valor)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución de la creación del enlace:",t1_stop-t1_start," segundos")

def DFS (catalog, vertice):
    t1_start = process_time() #tiempo inicial
    dfs = model.DFS(catalog, vertice)
    if dfs == False:
        print("El vértice ingresado no existe")
    else:
        print("El DFS se terminó exitosamente: \n")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución del DFS:",t1_stop-t1_start," segundos")