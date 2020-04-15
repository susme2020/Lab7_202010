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
from ADT import list as lt
from ADT import graph as g
from ADT import map as map
from ADT import list as lt
from DataStructures import listiterator as it
from datetime import datetime

"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo y retorna el catalogo inicializado.
    """
    rgraph = g.newGraph(5500,compareByKey)
    catalog = {'reviewGraph':rgraph}    
    return catalog


def addReviewNode (catalog, row):
    """
    Adiciona un nodo para almacenar un libro o usuario 
    """
    if not g.containsVertex(catalog['reviewGraph'], row['book_id']):
        g.insertVertex (catalog['reviewGraph'], row['book_id'])
    if not g.containsVertex(catalog['reviewGraph'], row['user_id']):
        g.insertVertex (catalog['reviewGraph'], row['user_id'])

def addReviewEdge (catalog, row):
    """
    Adiciona un enlace para almacenar una revisión
    """
    g.addEdge (catalog['reviewGraph'], row['book_id'], row['user_id'], row['rating'])


def countNodesEdges (catalog):
    """
    Retorna la cantidad de nodos y enlaces del grafo de revisiones
    """
    nodes = g.numVertex(catalog['reviewGraph'])
    edges = g.numEdges(catalog['reviewGraph'])

    return nodes,edges

def countConnectedComponents (catalog):
    """
    Retorna la cantidad de componentes conectados del grafo de revisiones
    """
    pass




# Funciones de comparacion

def compareByKey (key, element):
    return  (key == element['key'] )  

