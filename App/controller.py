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
 """

import config as cf
import model
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = model.new_data_structs()
    return control


#========================================================
# Funciones para la carga de datos
#========================================================

def load_data(control, flights_file, airports_file):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    start_time = get_time()
    
    #Carga de datos
    print("Cargando airports...")
    load_airports(control, airports_file)
    print("Carga completa.")
    print("Cargando fligths...")
    load_flights(control, flights_file)
    
    #Indicador de carga completa
    print("-"*40)
    print("CARGA COMPLETA")
    print("-"*40)
    print("\n")
    
    #Instrucciones de tiempo de carga
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    
    return control, deltaTime

def load_flights(control, file):
    flights_file = cf.data_dir + file
    input_file = csv.DictReader(open(flights_file, encoding="utf-8"), delimiter=";")
    for flight in input_file:
        model.addFlightConnection(control,flight)
        
    #Conexiones de mapa de todos los aeropuertos por distancia
    model.addRouteConnections(control, "AirportsMap","AirportDistanceConnections")
    #Conexiones de mapa de todos los aeropuertos por tiempo
    model.addRouteConnections(control, "AirportsMap","AirportTimeConnections")
    
    #Conexiones de mapa de los aeropuertos COMERCIALES
    #Por distancia:
    model.addRouteConnections(control, "AirportsComercialMap","AirportComercialConnections")
    #Por tiempo:
    model.addRouteConnections(control, "AirportsComercialMap","AirportComercialTimeConnections")
    #Lista de aeropuertos comerciales:
    model.addAirportToList(control, "AirportsComercialMap", "AirportsComercialList")
    
    #Conexiones de mapa de los aeropuertos MILITARES
    model.addRouteConnections(control, "AirportsMilitarMap","AirportMilitarConnections" )
    #Lista de aeropuertos militares:
    model.addAirportToList(control, "AirportsMilitarMap", "AirportsMilitarList")
    
    #Conexiones de mapa de los aeropuertos CARGA
    model.addRouteConnections(control, "AirportsCargaMap","AirportCargaConnections" )
    #Lista de aeropuertos carga:
    model.addAirportToList(control, "AirportsCargaMap", "AirportsCargaList")
    
    return control

def load_airports(control, file):
    airport_file = cf.data_dir + file
    input_file = csv.DictReader(open(airport_file, encoding="utf-8"), delimiter=";")
    lastAirport = None
    for airport in input_file:
        model.addAirportToMap(control, airport, "None", "ICAO")
        if lastAirport is not  None:
            model.addAirportConnection(control, lastAirport, airport)
        lastAirport = airport
    return control
    

#========================================================
# Funciones de ordenamiento
#========================================================

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


#========================================================
# Funciones de consulta sobre el catálogo
#========================================================

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, origen_latitud, origen_longitud, destino_latitud, destino_longitud):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start_time = get_time()
    
    result = model.req_1(control, origen_latitud, origen_longitud, destino_latitud, destino_longitud)
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    
    return result, deltaTime


def req_2(control, origen_latitud, origen_longitud, destino_latitud, destino_longitud):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start_time = get_time()
    
    result = model.req_2(control, origen_latitud, origen_longitud, destino_latitud, destino_longitud)
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    
    return result, deltaTime


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = get_time()
    
    result = model.req_3(control)
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    
    return result, deltaTime


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control, origen_latitud, origen_longitud, destino_latitud, destino_longitud):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start_time = get_time()
    
    result = model.req_7(control, origen_latitud, origen_longitud, destino_latitud, destino_longitud)
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    
    return result, deltaTime


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass

#========================================================
# Funciones de consulta sobre las estructuras
#========================================================

def totalConnections(data, data_structure):
    """
    Total de enlaces entre las paradas
    """
    return model.totalConnections(data, data_structure)

def totalNumVertex(data, data_structure):
    """
    Retorna el total de estaciones (vertices) del grafo
    """
    return model.totalNumVertex(data, data_structure)

def totalMapKeys(data, data_structure):
    """
    Retorna el total de llaves en un mapa
    """
    return model.totalMapKeys(data, data_structure)

#========================================================
# Funciones para medir tiempos de ejecucion
#========================================================


def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
