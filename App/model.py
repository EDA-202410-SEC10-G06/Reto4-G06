"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import graph as gr
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Algorithms.Graphs import bellmanford as bf
from DISClib.Algorithms.Graphs import bfs
from DISClib.Algorithms.Graphs import dfs
from DISClib.Algorithms.Graphs import prim
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

from DISClib.Utils import error as error
import math

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    
    try:
        data_structs = {
            'Airports': None,
            'AirportsMap': None,
            'AirportsComercialMap': None,
            'AirportsCargaMap': None,
            'AirportsMilitarMap': None,
            'AirportDistanceConnections': None,
            'AirportTimeConnections': None,
            'AirportComercialConnections': None,
            'AirportComercialTimeConnections': None,
            'AirportCargaConnections': None,
            'AirportMilitarConnections': None
        }

        #Mapa de informacion de Aeropuertos
        data_structs["AirportsInfoMap"] = mp.newMap(numelements = 14000,
                                                maptype="PROBING",
                                                cmpfunction = compareKeysId)
        
        #Mapas para determinar la importancia del aeropuerto. 
        data_structs["AirportsComercialMap"] = mp.newMap(numelements = 14000,
                                                maptype="PROBING",
                                                cmpfunction = compareKeysId)
        
        data_structs["AirportsCargaMap"] = mp.newMap(numelements = 14000,
                                                maptype="PROBING",
                                                
                                                cmpfunction = compareKeysId)
        
        data_structs["AirportsMilitarMap"] = mp.newMap(numelements = 14000,
                                                maptype="PROBING",
                                                cmpfunction = compareKeysId)
        
        data_structs["AirportsMap"] = mp.newMap(numelements = 14000,
                                                maptype="PROBING",
                                                cmpfunction = compareKeysId)
        
        #---------------------------------------
        #Gragos con conexiones entre aeropuertos
        #---------------------------------------
        
        #Grafo de TODOS los aeropuertos. Peso: distance
        data_structs["AirportDistanceConnections"] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=False,
                                              size=14000,
                                              cmpfunction=compareKeysId)
        
        #Grafo de TODOS los aeropuertos. Peso: time
        data_structs["AirportTimeConnections"] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=False,
                                              size=14000,
                                              cmpfunction=compareKeysId)
        
        
        
        
        #Req 3, Peso: distance
        data_structs["AirportComercialConnections"] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=False,
                                              size=14000,
                                              cmpfunction=compareKeysId)
        
        #Req 7, Peso: tiempo
        data_structs["AirportComercialTimeConnections"] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=False,
                                              size=14000,
                                              cmpfunction=compareKeysId)
        
        #Req 4, Peso: distance
        data_structs["AirportCargaConnections"] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=False,
                                              size=14000,
                                              cmpfunction=compareKeysId)
        #Req 5, Peso: distance
        data_structs["AirportMilitarConnections"] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=False,
                                              size=14000,
                                              cmpfunction=compareKeysId)
        
        
        
        
        #Esta estructura es provicional: se ejecuta con el documento de aeropuertos.
        data_structs["AirportDistanceConnectionsAirportsDoc"] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=False,
                                              size=14000,
                                              cmpfunction=compareKeysId)
        
        return data_structs
    except Exception as exp:
        error.reraise(exp, 'model:new_data_structs')
    
    pass

#========================================================
# Funciones para calculos complejos
#========================================================

def haversine(lat1, lon1, lat2, lon2):
    """
    Funcion que calcula la distancia entre dos coordenadas
    Tomado de: https://upcommons.upc.edu/bitstream/handle/2117/82817/Annex%205.pdf?sequence=7&isAllowed=y
    
    """

    # Convertir grados a radianes
    lat1 = math.radians(float(lat1))
    lon1 = math.radians(float(lon1))
    lat2 = math.radians(float(lat2))
    lon2 = math.radians(float(lon2))
    
    # Diferencias de latitud y longitud
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1
    
    # Calcular 'a' usando la fórmula de Haversine
    a = math.sin(delta_lat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2)**2
    
    # Calcular 'c'
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Radio de la Tierra en kilómetros (aproximadamente)
    R = 6371.0
    
    # Calcular la distancia
    distance = R * c
    
    return distance

#========================================================
# Funciones para agregar informacion al modelo
#========================================================

def addFlightConnection(data_structs,flight):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    
    #lastFlight, flight = setAirportData(lastFlight, flight)
    try:
                
        origin = flight["ORIGEN"]
        destination = flight["DESTINO"]
        
        timeFlight = flight["TIEMPO_VUELO"]
        
        entry = mp.get(data_structs["AirportsInfoMap"], flight["ORIGEN"])
        origenInfo = me.getValue(entry)
        
        entry = mp.get(data_structs["AirportsInfoMap"], flight["DESTINO"])
        destinoInfo = me.getValue(entry)
        
        distance = haversine(origenInfo["LATITUD"],origenInfo["LONGITUD"],destinoInfo["LATITUD"],destinoInfo["LONGITUD"])
        distance = abs(distance)
        
        #Grafo con TODOS los vuelos por tiempo  
        addAirportToGraph(data_structs, origin, "AirportTimeConnections")
        addAirportToGraph(data_structs, destination, "AirportTimeConnections")
        
        #Grafo con TODOS los vuelos por distancia
        addAirportToGraph(data_structs, origin, "AirportDistanceConnections")
        addAirportToGraph(data_structs, destination, "AirportDistanceConnections")
        
        #Añade al mapa con todos los aeropuertos
        addAirportToMap(data_structs, origin, flight, "AIRPORTS")
        addAirportToMap(data_structs, destination, flight, "AIRPORTS")
        
        #Grafo con vuelos MILITARES
        if flight["TIPO_VUELO"] == "MILITAR":
            addAirportToGraph(data_structs, origin, "AirportMilitarConnections")
            addAirportToGraph(data_structs, destination, "AirportMilitarConnections")
            
            addAirportToMap(data_structs, origin, flight, "MILITAR")
            addAirportToMap(data_structs, destination, flight, "MILITAR")
            
            addTimeConnectionToAirports(data_structs, origin, destination, distance, "AirportMilitarConnections")
        
        #Grafo con vuelos COMERCIALES
        elif flight["TIPO_VUELO"] == "AVIACION_COMERCIAL":
            #Por distancia
            addAirportToGraph(data_structs, origin, "AirportComercialConnections")
            addAirportToGraph(data_structs, destination, "AirportComercialConnections")
            
            #Por tiempo
            addAirportToGraph(data_structs, origin, "AirportComercialTimeConnections")
            addAirportToGraph(data_structs, destination, "AirportComercialTimeConnections")
            
            addAirportToMap(data_structs, origin, flight, "COMERCIAL")
            addAirportToMap(data_structs, destination, flight, "COMERCIAL")
            
            #Por distancia
            addTimeConnectionToAirports(data_structs, origin, destination, distance, "AirportComercialConnections")
            
            #Por tiempo
            addTimeConnectionToAirports(data_structs, origin, destination, timeFlight, "AirportComercialTimeConnections")
        
        #Vuelos con vuelos de CARGA
        elif flight["TIPO_VUELO"] == "AVIACION_CARGA":
            addAirportToGraph(data_structs, origin, "AirportCargaConnections")
            addAirportToGraph(data_structs, destination, "AirportCargaConnections")
            
            addAirportToMap(data_structs, origin, flight, "CARGA")
            addAirportToMap(data_structs, destination, flight, "CARGA")
            
            addTimeConnectionToAirports(data_structs, origin, destination, distance, "AirportCargaConnections")
        
        #Añade una conexion por tiempo
        addTimeConnectionToAirports(data_structs, origin, destination, timeFlight, "AirportTimeConnections")
        
        #Añade una conexion por distancia
        addDistanceConnectionToAirports(data_structs, origin, destination, distance, "AirportDistanceConnections")
        
        #Se añade al mapa de rutas
        #addRouteAirport(data_structs, origen)
        #addRouteAirport(data_structs, destino)
        
        return data_structs
    except Exception as exp:
        error.reraise(exp, 'model:addAirportTimeConnection')


def addAirportConnection(data_structs, lastAirportP, airportP):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    
    lastAirport, airport = setAirportData(lastAirportP, airportP)
    
    try:
        LastAirportCoordinates = f'{lastAirport["LATITUD"]}/{lastAirport["LONGITUD"]}' 
        airportCoordinates = f'{airport["LATITUD"]}/{airport["LONGITUD"]}' 
        
        #Vertices: coordenadas (latitud-longitud)
        origin = LastAirportCoordinates
        destination = airportCoordinates
        
        #Vertices Airports
        #origin = lastAirport["ICAO"]
        #destination = airport["ICAO"]
    
        distance = haversine(airport["LATITUD"],airport["LONGITUD"],lastAirport["LATITUD"],lastAirport["LONGITUD"])
        distance = abs(distance)
        
        addAirportToGraph(data_structs, origin, "AirportDistanceConnectionsAirportsDoc")
        addAirportToGraph(data_structs, destination, "AirportDistanceConnectionsAirportsDoc")
        
        addDistanceConnectionToAirports(data_structs, origin, destination, distance,"AirportDistanceConnectionsAirportsDoc")

        return data_structs
    except Exception as exp:
        error.reraise(exp, 'model:addAirportConnection')


def addAirportToMap (data_structs, airport, flight, index):
    """
    Función para agregar nuevos elementos al mapa de Aiports
    """
    if index == "ICAO":
        mp.put(data_structs["AirportsInfoMap"], airport["ICAO"], airport)
        
    elif index == "CARGA":

        entry = mp.get(data_structs['AirportsCargaMap'], airport)
        if entry is None:
            lstflights = lt.newList(cmpfunction=compareroutes)
            mp.put(data_structs['AirportsCargaMap'], airport, lstflights)
        else:
            lstflights = entry['value']
        lt.addLast(lstflights, flight)
            
    elif index == "COMERCIAL":
        
        #Por distancia
        entry = mp.get(data_structs['AirportsComercialMap'], airport)
        if entry is None:
            lstflights = lt.newList(cmpfunction=compareroutes)
            mp.put(data_structs['AirportsComercialMap'], airport, lstflights)
        else:
            lstflights = entry['value']
        lt.addLast(lstflights, flight)
        
    elif index == "MILITAR":
    
        entry = mp.get(data_structs['AirportsMilitarMap'], airport)
        if entry is None:
            lstflights = lt.newList(cmpfunction=compareroutes)
            mp.put(data_structs['AirportsMilitarMap'], airport, lstflights)
        else:
            lstflights = entry['value']
        lt.addLast(lstflights, flight)
    
    elif index == "AIRPORTS":
        
        entry = mp.get(data_structs['AirportsMap'], airport)
        if entry is None:
            lstflights = lt.newList(cmpfunction=compareroutes)
            mp.put(data_structs['AirportsMap'], airport, lstflights)
        else:
            lstflights = entry['value']
        lt.addLast(lstflights, flight)
        
        
    
def addAirportToGraph(data_structs, airport, graph_str):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista

    try:
        if not gr.containsVertex(data_structs[graph_str], airport):
            gr.insertVertex(data_structs[graph_str], airport)
        return data_structs
    except Exception as exp:
        error.reraise(exp, 'model:addAirport')


def addDistanceConnectionToAirports(data_structs, origin, destination, distance, graph):
    """
    Adiciona un arco entre dos estaciones
    """
    edge = gr.getEdge(data_structs[graph], origin, destination)
    if edge is None:
        gr.addEdge(data_structs[graph], origin, destination, distance)
    return data_structs


def addTimeConnectionToAirports(data_structs, origin, destination, distance, graph):
    """
    Adiciona un arco entre dos estaciones
    """
    edge = gr.getEdge(data_structs[graph], origin, destination)
    if edge is None:
        gr.addEdge(data_structs[graph], origin, destination, distance)
    return data_structs

def addRouteConnections(data_structs, map, graph):
    """
    Por cada vertice (cada Airport) se recorre la lista
    de rutas servidas en dicha estación y se crean
    arcos entre ellas para representar el cambio de ruta
    que se puede realizar en una estación.
    """
    lstairports = mp.keySet(data_structs[map])
    for key in lt.iterator(lstairports):
        lstflights = mp.get(data_structs[map], key)['value']
        prevflight = None
        prevAirport = None
        for flight in lt.iterator(lstflights):
            
            if flight["DESTINO"] != key:
                airport = flight["DESTINO"]
            elif flight["ORIGEN"] != key:
                airport = flight["ORIGEN"]
            
            if prevflight is not None:
                addDistanceConnectionToAirports(data_structs, prevAirport, airport, 0, graph)
                addDistanceConnectionToAirports(data_structs, airport, prevAirport, 0, graph)
            prevflight = flight
            prevAirport = airport


#========================================================
# Funciones para creacion de datos
#========================================================


def setAirportData(lastAirport, airport):
    
    #Convierte las coordenadas a sistema decimal con punto
    #Nota: solo es necesario cambiar la caracteristica "LONGITUD". 
    if "," in str(lastAirport["LONGITUD"]):  
        lastAirport["LONGITUD"] = float(lastAirport["LONGITUD"].replace(",", "."))
        lastAirport["LATITUD"] = float(lastAirport["LATITUD"].replace(",", "."))                         
    
    if "," in str(airport["LONGITUD"]):  
        airport["LONGITUD"] = float(airport["LONGITUD"].replace(",", "."))
        airport["LATITUD"] = float(airport["LATITUD"].replace(",", "."))  
    
    return lastAirport, airport


def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


#========================================================
# Funciones de consulta
#========================================================

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


#========================================================
# Funciones de consulta sobre las estructuras
#========================================================

def totalConnections(analyzer, data_structure):
    """
    Retorna el total arcos del grafo
    """
    return gr.numEdges(analyzer[data_structure])


def totalNumVertex(data, data_structure):
    """
    Retorna el total de estaciones (vertices) del grafo
    """
    return gr.numVertices(data[data_structure])

def totalMapKeys(data, data_structure):
    """
    Retorna el total de llaves en un mapa.
    """
    keys = mp.keySet(data[data_structure])
    return lt.size(keys)


#======================================================================
# Funciones utilizadas para comparar elementos dentro de una estructura
#======================================================================

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

def compareKeysId(element, keyvalue):
    """
    Compara dos estaciones
    """
    key = keyvalue['key']
    if (element == key):
        return 0
    elif (element > key):
        return 1
    else:
        return -1

def compareroutes(route1, route2):
    """
    Compara dos rutas
    """
    if (route1 == route2):
        return 0
    elif (route1 > route2):
        return 1
    else:
        return -1

#======================================================================
# Funciones de ordenamiento
#======================================================================

def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
