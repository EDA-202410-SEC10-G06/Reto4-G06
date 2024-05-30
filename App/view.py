"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import stack
assert cf
from tabulate import tabulate
import traceback

import folium
import os
import webbrowser
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control, flights_file, airports_file):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    data, deltaTime = controller.load_data(control, flights_file, airports_file)
    print_data(data, deltaTime)


def print_data(data, deltaTime):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
        
    print ("--------------------------------------------------------------------")
    print("Tiempo [ms]: ", f"{deltaTime:.3f}", "||")
    print ("--------------------------------------------------------------------")
    print("\n")
    print ("--------------------------------------------------------------------")
    print("Total aeropuertos cargados: ", controller.totalMapKeys(data, "AirportsInfoMap"))
    print ("--------------------------------------------------------------------")
    print("\n")
    print ("--------------------------- BY DISTANCE ----------------------------")
    print("Numero de vertices (Airports-distance): ", controller.totalNumVertex(data, "AirportDistanceConnections"))
    print("Numero de conexiones (Airports-distance): ", controller.totalConnections(data, "AirportDistanceConnections"))
    print("\n")
    print ("----------------------------- BY TIME ------------------------------")  
    print("Numero de vertices (Airports-time): ", controller.totalNumVertex(data, "AirportTimeConnections"))
    print("Numero de conexiones (Airports-time): ", controller.totalConnections(data, "AirportTimeConnections"))
    print ("--------------------------------------------------------------------")
    print("\n")
    print ("----------------------------- MILITAR ------------------------------") 
    print("Numero de aeropuertos con tipo de vuelo militar: ", controller.totalMapKeys(data, "AirportsMilitarMap"))
    print("Numero de vertices (Airports-distance): ", controller.totalNumVertex(data, "AirportMilitarConnections"))
    print("Numero de conexiones (Airports-distance): ", controller.totalConnections(data, "AirportMilitarConnections"))
    print_tabulate(data, data["AirportsMilitarList"], "CargaConcurrencia")
    print ("---------------------------- COMERCIAL -----------------------------")
    print("Numero de aeropuertos con tipo de vuelo militar: ", controller.totalMapKeys(data, "AirportsComercialMap"))
    print("Por distancia:")
    print("Numero de vertices (Airports-distance): ", controller.totalNumVertex(data, "AirportComercialConnections"))
    print("Numero de conexiones (Airports-distance): ", controller.totalConnections(data, "AirportComercialConnections"))
    print("Por tiempo: ")
    print("Numero de vertices (Airports-distance): ", controller.totalNumVertex(data, "AirportComercialTimeConnections"))
    print("Numero de conexiones (Airports-distance): ", controller.totalConnections(data, "AirportComercialTimeConnections"))
    print_tabulate(data, data["AirportsComercialList"], "CargaConcurrencia")
    print ("------------------------------ CARGA -------------------------------")
    print("Numero de aeropuertos con tipo de vuelo militar: ", controller.totalMapKeys(data, "AirportsCargaMap"))
    print("Numero de vertices (Airports-time): ", controller.totalNumVertex(data, "AirportCargaConnections"))
    print("Numero de conexiones (Airports-distance): ", controller.totalConnections(data, "AirportCargaConnections"))
    print_tabulate(data, data["AirportsCargaList"], "CargaConcurrencia")
    print ("--------------------------------------------------------------------")
    print("\n")
    print("\n")
    print("\n")
            
 
def print_tabulate(data_structs, lista, condicion):

    if condicion == "listas":
        size = lt.size(lista)
        headers = ["Titulo", "Fecha", "Nombre de la empresa", "Nivel de experticie", "Pais", 'Ciudad', 'Tamaño de la compañia', 'WorkPlace', 'Skills','Salario Min']
        data = []
        data_2 = []
        i = 1
        i_2 = int(lt.size(lista)) - 4
        x = 0
        x_2 = 0    
        if size > 10:
            while x != 5:
                    current = lt.getElement(lista, i)
                    i +=1
                    x += 1
                    rta_skill = ''
                    if not isinstance(current['skills'], str):
                        for skill in lt.iterator(current['skills']):
                            rta_skill = f'{rta_skill}{skill}/'
                            rta_skill = f'{rta_skill}{skill}/'
                    else:
                        rta_skill = current['skills']
                        
                    data.append([current['title'], str(current["published_at"]), current["company_name"], current["experience_level"], current["country_code"], current['city'], current['company_size'], 
                                current['workplace_type'], rta_skill, current["employment_types"]["salary_from"]])
            while x_2 != 5:
                    current = lt.getElement(lista, i_2)
                    i_2 += 1
                    x_2 += 1
                    rta_skill = ''
                    if not isinstance(current['skills'], str):
                        for skill in lt.iterator(current['skills']):
                                rta_skill = f'{rta_skill}{skill}/'
                    else:
                        rta_skill = current['skills']
                        
                    data_2.append([current['title'], str(current["published_at"]), current["company_name"], current["experience_level"], current["country_code"], current['city'], current['company_size'], 
                                current['workplace_type'], rta_skill, current["employment_types"]["salary_from"]])
                    
            print(tabulate(data, headers=headers, tablefmt='fancy_grid'))
            print(tabulate(data_2, headers=headers, tablefmt='fancy_grid'))
            
        else:
            for job in lt.iterator(lista):

                rta_skill = ''
                if not isinstance(job['skills'], str):
                    for skill in lt.iterator(job['skills']):
                            rta_skill = f'{rta_skill}{skill}/'
                else:
                    rta_skill = job['skills']
                
                data.append([job['title'], str(job["published_at"]), job["company_name"], job["experience_level"], job["country_code"], job['city'], job['company_size'], 
                            job['workplace_type'], rta_skill, job["employment_types"]["salary_from"]])
            print(tabulate(data, headers=headers, tablefmt='fancy_grid'))
            print('\n')    
    
    elif condicion == "CargaConcurrencia":
        
        headers = ["NOMBRE", "ICAO", "CIUDAD", "CONCURRENCIA"]
        
        firstDicts = lista["elements"][0:5]
        lastDicts = lista["elements"][-5::]
        
        first5 = []
        last5 = []
        
        for dict in firstDicts:
            airportICAO = dict["airport"]
            airport = mp.get(data_structs["AirportsInfoMap"], airportICAO)["value"]
            
            first5.append([airport["NOMBRE"], airport["ICAO"], airport["CIUDAD"], dict["numeroVuelos"]])
        
        for dict in lastDicts:
            airportICAO = dict["airport"]
            airport = mp.get(data_structs["AirportsInfoMap"], airportICAO)["value"]
            
            last5.append([airport["NOMBRE"], airport["ICAO"], airport["CIUDAD"], dict["numeroVuelos"]])  
        
        print("Primeros 5: ")
        print(tabulate(first5, headers=headers, tablefmt='fancy_grid'))
        print("Ultimos 5: ")
        print(tabulate(last5, headers=headers, tablefmt='fancy_grid'))
        
    elif condicion == "ListaAirports":
        
        headers = ["NOMBRE", "ICAO", "CIUDAD"]
        
        data = lista["elements"]
        data_tabulate = []
        
        for pos in range(lt.size(lista) - 1, -1, -1):
            airport = data[pos]
            data_tabulate.append([airport["NOMBRE"], airport["ICAO"], airport["CIUDAD"]])
        
        print(tabulate(data_tabulate, headers=headers, tablefmt='fancy_grid'))
        
        
    elif condicion == "req7":
        
        headers = ["NOMBRE", "ICAO", "CIUDAD"]
        
        data = lista["elements"]
        data_tabulate = []
        
        for pos in range(lt.size(lista) - 1, -1, -1):
            edge = data[pos]
            
            vertexA = edge[0]
            vertexB = edge[1]
            
            data_tabulate.append([vertexA["NOMBRE"], vertexA["ICAO"], vertexA["CIUDAD"]])
            data_tabulate.append([vertexB["NOMBRE"], vertexB["ICAO"], vertexB["CIUDAD"]])
        
        print(tabulate(data_tabulate, headers=headers, tablefmt='fancy_grid'))  
        
        
    elif condicion == "individual":
        
        headers = ["NOMBRE", "ICAO", "CIUDAD"]
        
        data_tabulate = []
    
        while (not stack.isEmpty(lista)):
            element = stack.pop(lista)
            airport = mp.get(data_structs["AirportsInfoMap"], element)["value"]
                        
            data_tabulate.append([airport["NOMBRE"], airport["ICAO"], airport["CIUDAD"]])
        
        
        print(tabulate(data_tabulate, headers=headers, tablefmt='fancy_grid')) 
        
    elif condicion == "req6Vuelos":
        
        headers = ["ORIGEN", "DESTINO"]
        
        data_tabulate = []
    
        while (not stack.isEmpty(lista)):
            element = stack.pop(lista)
            vertexA = element[0]['ICAO']
            vertexB = element[1]['ICAO']
            
                        
            data_tabulate.append([vertexA, vertexB])
        
        
        print(tabulate(data_tabulate, headers=headers, tablefmt='fancy_grid')) 
        
    elif condicion == "req6Airport":
        
        headers = ["NOMBRE", "ICAO", "CIUDAD", 'PAIS', 'CONCURRENCIA']
        data_tabulate = []
        
        element = mp.get(data_structs['AirportsInfoMap'], lista['airport'])['value']
                        
        data_tabulate.append([element['NOMBRE'],element['ICAO'], element['CIUDAD'], element['PAIS'], lista['numeroVuelos']])
        
        print(tabulate(data_tabulate, headers=headers, tablefmt='fancy_grid'))
        
    elif condicion == "req6lstAirports":
        
        headers = ["NOMBRE", "ICAO", "CIUDAD", 'PAIS', 'CONCURRENCIA']
        data_tabulate = []
        
        for airport in lt.iterator(lista):
    
            element = mp.get(data_structs['AirportsInfoMap'], airport)['value']            
            data_tabulate.append([element['NOMBRE'],element['ICAO'], element['CIUDAD'], element['PAIS']])
            
        print(tabulate(data_tabulate, headers=headers, tablefmt='fancy_grid'))
          
    
def print_req_1(data_structs, results, deltaTime, condicion):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    
    if condicion == "FOUNDPATH":
        print ("--------------------------------------------------------------------")
        print("Tiempo [ms]: ", f"{deltaTime:.3f}", "||")
        print ("--------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------")
        print("Total distancia recorrida: ", results[0], "KM.")
        print("Tiempo total: ", results[5], "minutos.")
        print("Numero de aeropuertos recorridos: ", results[1])
        print("Aeropuerto ORIGEN: ", results[3])
        print("Aeropuerto DESTINO: ", results[4])
        print("--------------------------------------------------------------------")
        print("RECORRIDO: ")
        print_tabulate(data_structs, results[2], "ListaAirports")

    elif (condicion == "NOPATH"): 
        
        print ("--------------------------------------------------------------------")
        print("Tiempo [ms]: ", f"{deltaTime:.3f}", "||")
        print ("--------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------")
        print("---- NO EXISTE NINGUN CAMINO ENTRE LOS AEROPUERTOS ENCONTRADOS -----")
        print("--------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------")
        print("Aeropuerto origen más cercano: ", results[0], "a ", results[2] ," KM.")
        print("Aeropuerto destino más cercano: ", results[1], "a ", results[3] ," KM.")
        print("--------------------------------------------------------------------")
    
    else:
        
        print ("--------------------------------------------------------------------")
        print("Tiempo [ms]: ", f"{deltaTime:.3f}", "||")
        print ("--------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------")
        print("---- NO SE ENCONTRO UN AEROPUERTO DENTRO DE UN RANGO DE 30 KM ------")
        print("--------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------")
        print("Aeropuerto origen más cercano: ", results[0], "a ", results[2] ," KM.")
        print("Aeropuerto destino más cercano: ", results[1], "a ", results[3] ," KM.")
        print("--------------------------------------------------------------------")
        

def print_req_2(data_structs, results, deltaTime, condicion):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    
    if condicion == "FOUNDPATH":
        
        print ("--------------------------------------------------------------------")
        print("Tiempo [ms]: ", f"{deltaTime:.3f}", "||")
        print ("--------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------")
        print("Total distancia recorrida: ", results[0], "KM.")
        print("Tiempo total: ", results[5], "minutos.")
        print("Numero de aeropuertos recorridos: ", results[1])
        print("Aeropuerto ORIGEN: ", results[3])
        print("Aeropuerto DESTINO: ", results[4])
        print("--------------------------------------------------------------------")
        print("RECORRIDO: ")
        print_tabulate(data_structs, results[2], "ListaAirports")

    elif (condicion == "NOPATH"): 
        
        print ("--------------------------------------------------------------------")
        print("Tiempo [ms]: ", f"{deltaTime:.3f}", "||")
        print ("--------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------")
        print("---- NO EXISTE NINGUN CAMINO ENTRE LOS AEROPUERTOS ENCONTRADOS -----")
        print("--------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------")
        print("Aeropuerto origen más cercano: ", results[0], "a ", results[2] ," KM.")
        print("Aeropuerto destino más cercano: ", results[1], "a ", results[3] ," KM.")
        print("--------------------------------------------------------------------")
    
    else:
        
        print ("--------------------------------------------------------------------")
        print("Tiempo [ms]: ", f"{deltaTime:.3f}", "||")
        print ("--------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------")
        print("-- NO SE ENCONTRO NINGUN AEROPUERTO DENTRO DE UN RANGO DE 30 KM ----")
        print("--------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------")
        print("Aeropuerto origen más cercano: ", results[0], "a ", results[2] ," KM.")
        print("Aeropuerto destino más cercano: ", results[1], "a ", results[3] ," KM.")
        print("--------------------------------------------------------------------")
    
    
def print_individuales(data_structs, results, deltaTime):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    
    print ("--------------------------------------------------------------------")
    print("Tiempo [ms]: ", f"{deltaTime:.3f}", "||")
    print ("--------------------------------------------------------------------")
    print("\n")
    print("--------------------------------------------------------------------")
    print("Total distancia recorrida: ", results[0], "KM.")
    print("Numero de trayectos: ", results[2])
    print("Aeropuerto de mayor concurrencia: ", results[1])
    print("--------------------------------------------------------------------")
    print("TRAYECTOS: ")
    print("\n")
    
    data = results[3]["elements"]
    
    print("--------------------------------------------------------------------")
    print("                       PRIMEROS 5 TRAYECTOS                         ")
    print("--------------------------------------------------------------------")
    for trayecto in data[:5]:
    
        print("--------------------------------------------------------------------")
        print("Aeropuerto origen: ", results[1])
        print("Destino: ", trayecto["destino"])
        print("Distancia: ", trayecto["distance"], " KM.")
        print("Tiempo total: ", trayecto["time"], " min.")
        print_tabulate(data_structs, trayecto["path"], "individual")
        print("--------------------------------------------------------------------")
    
    
    print("\n")
    print("--------------------------------------------------------------------")
    print("                       ULTIMOS 5 TRAYECTOS                         ")
    print("--------------------------------------------------------------------")
    
    for trayecto in data[-5:]:
        
        print("--------------------------------------------------------------------")
        print("Aeropuerto origen: ", results[1])
        print("Destino: ", trayecto["destino"])
        print("Distancia: ", trayecto["distance"], " KM.")
        print("Tiempo total: ", trayecto["time"], " min.")
        print_tabulate(data_structs, trayecto["path"], "individual")
        print("--------------------------------------------------------------------")


def print_req_6(data_structs, results, deltaTime):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    
    print ("--------------------------------------------------------------------")
    print("Tiempo [ms]: ", f"{deltaTime:.3f}", "||")
    print ("--------------------------------------------------------------------")
    print("\n")
    print("--------------------------------------------------------------------")
    print("Aeropuerto de mayor concurrencia comercial: ", results[0]['airport'])
    print_tabulate(data_structs, results[0], "req6Airport")
    print("--------------------------------------------------------------------")
    print("\n")
    print("TRAYECTOS: ")
    
    data = results[1]["elements"]
    
    if lt.size(results[1]) >= 10:
    
        print("--------------------------------------------------------------------")
        print("                       PRIMEROS 5 TRAYECTOS                         ")
        print("--------------------------------------------------------------------")
        for trayecto in data[:5]:

            print("--------------------------------------------------------------------")
            print("Aeropuerto origen: ", results[0]["airport"])
            print("Aeropuertos visitados: ", lt.size(trayecto["lstAirports"]) + 1)
            print("Destino: ", trayecto["destino"]["airport"])
            print("Distancia: ", round(trayecto["distance"], 3), " KM.")
            print("Tiempo total: ", round(trayecto["time"], 3), " min.")
            print("--------------------------------------------------------------------")
            print("AEROPUERTOS: ")
            print_tabulate(data_structs, trayecto["lstAirports"], "req6lstAirports")
            print("--------------------------------------------------------------------")
            print("VUELOS: ")
            print_tabulate(data_structs, trayecto["path"], "req6Vuelos")
            print("--------------------------------------------------------------------")
            print("\n")
            
            
        print("\n")
        
        print("--------------------------------------------------------------------")
        print("                       ULTIMOS 5 TRAYECTOS                         ")
        print("--------------------------------------------------------------------")
        for trayecto in data[-5:]:
        
            print("--------------------------------------------------------------------")
            print("Aeropuerto origen: ", results[0]["airport"])
            print("Aeropuertos visitados: ", lt.size(trayecto["lstAirports"]) + 1)
            print("Destino: ", trayecto["destino"]["airport"])
            print("Distancia: ", round(trayecto["distance"], 3), " KM.")
            print("Tiempo total: ", round(trayecto["time"], 3), " min.")
            print("--------------------------------------------------------------------") 
            print("AEROPUERTOS: ")
            print_tabulate(data_structs, trayecto["lstAirports"], "req6lstAirports")
            print("--------------------------------------------------------------------")
            print("VUELOS: ")
            print_tabulate(data_structs, trayecto["path"], "req6Vuelos")
            print("--------------------------------------------------------------------")
            print("\n")
    
    else:
         
        for trayecto in data:
 
            print("--------------------------------------------------------------------")
            print("Aeropuerto origen: ", results[0]["airport"])
            print("Aeropuertos visitados: ", lt.size(trayecto["lstAirports"]) + 1)
            print("Destino: ", trayecto["destino"]["airport"])
            print("Distancia: ", round(trayecto["distance"], 3), " KM.")
            print("Tiempo total: ", round(trayecto["time"], 3), " min.")
            print("--------------------------------------------------------------------")
            print("AEROPUERTOS: ")
            print_tabulate(data_structs, trayecto["lstAirports"], "req6lstAirports")
            print("--------------------------------------------------------------------")
            print("VUELOS: ")
            print_tabulate(data_structs, trayecto["path"], "req6Vuelos")
            print("--------------------------------------------------------------------")
            print("\n")
            

def print_req_7(data_structs, results, deltaTime, condicion):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    
    if condicion == "FOUNDPATH":
        print ("--------------------------------------------------------------------")
        print("Tiempo [ms]: ", f"{deltaTime:.3f}", "||")
        print ("--------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------")
        print("Total distancia recorrida: ", results[0], "KM.")
        print("Tiempo total: ", results[5], "minutos.")
        print("Numero de aeropuertos recorridos: ", results[1])
        print("Aeropuerto ORIGEN: ", results[3])
        print("Aeropuerto DESTINO: ", results[4])
        print("--------------------------------------------------------------------")
        print("RECORRIDO: ")
        print_tabulate(data_structs, results[2], "req7")
        

    elif (condicion == "NOPATH"): 
        
        print ("--------------------------------------------------------------------")
        print("Tiempo [ms]: ", f"{deltaTime:.3f}", "||")
        print ("--------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------")
        print("---- NO EXISTE NINGUN CAMINO ENTRE LOS AEROPUERTOS ENCONTRADOS -----")
        print("--------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------")
        print("Aeropuerto origen más cercano: ", results[0], "a ", results[2] ," KM.")
        print("Aeropuerto destino más cercano: ", results[1], "a ", results[3] ," KM.")
        print("--------------------------------------------------------------------")
    
    else:
        
        print ("--------------------------------------------------------------------")
        print("Tiempo [ms]: ", f"{deltaTime:.3f}", "||")
        print ("--------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------")
        print("-- NO SE ENCONTRO ALGUN AEROPUERTO DENTRO DE UN RANGO DE 30 KM ----")
        print("--------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------")
        print("Aeropuerto origen más cercano: ", results[0], "a ", results[2] ," KM.")
        print("Aeropuerto destino más cercano: ", results[1], "a ", results[3] ," KM.")
        print("--------------------------------------------------------------------")


def print_req_8(data_structs, airports, condicion):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    
    print("\n")
    print("-"*40)

    directorio_actual = os.path.dirname(os.path.abspath(__file__))

    mapa = folium.Map(location = (4.71, -74.07), zoom_start = 6)
    
    print("Construyendo mapa...")
    print("\n")
    """
        if lt.size(airports) > 200:
        for airport in airports["elements"][:100]:
            folium.Marker(location = (airport["LATITUD"],airport["LONGITUD"]),popup = airport["ICAO"], icon = folium.Icon("red")).add_to(mapa)
        
        for airport in airports["elements"][-100::]:
            folium.Marker(location = (airport["LATITUD"],airport["LONGITUD"]),popup = airport["ICAO"], icon = folium.Icon("red")).add_to(mapa)
            
    else:
        for airport in lt.iterator(airports):
            folium.Marker(location = (airport["LATITUD"],airport["LONGITUD"]),popup = airport["ICAO"], icon = folium.Icon("red")).add_to(mapa)
    """
        
    if condicion == "basico":
        
        trail_coordinates = []
        
        for airport in lt.iterator(airports):
            trail_coordinates.append((airport["LATITUD"], airport["LONGITUD"]))
            folium.Marker(location = (airport["LATITUD"],airport["LONGITUD"]), popup = airport["ICAO"], icon = folium.Icon("red")).add_to(mapa)
            
        folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(mapa)
    
    if condicion == "individual":
        
        trail_coordinates = []
        
        for element in lt.iterator(airports):
            while (not stack.isEmpty(element["path"])):
                icao = stack.pop(element["path"])
                
                airport = mp.get(data_structs["AirportsInfoMap"], icao)["value"]
                
                trail_coordinates.append((airport["LATITUD"], airport["LONGITUD"]))
                folium.Marker(location = (airport["LATITUD"],airport["LONGITUD"]), popup = airport["ICAO"], icon = folium.Icon("red")).add_to(mapa)
                
                
        folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(mapa)
                
    if condicion == "req6":
        
        trail_coordinates = []
        
        for path in lt.iterator(airports):
            
            if lt.size(path["path"]) != 0:
            
                for edge in lt.iterator(path["path"]):
                    
                    vertexA = edge[0]
                    vertexB = edge[1]
                    
                    trail_coordinates.append((vertexA["LATITUD"], vertexA["LONGITUD"]))             
                    trail_coordinates.append((vertexB["LATITUD"], vertexB["LONGITUD"]))
                    
                    folium.Marker(location = (vertexA["LATITUD"],vertexA["LONGITUD"]), popup = vertexA["ICAO"], icon = folium.Icon("red")).add_to(mapa)
                    folium.Marker(location = (vertexB["LATITUD"],vertexB["LONGITUD"]), popup = vertexB["ICAO"], icon = folium.Icon("red")).add_to(mapa)

            else:
                
                origen = mp.get(data_structs["AirportsInfoMap"], path["origen"]["airport"])["value"]
                destino = mp.get(data_structs["AirportsInfoMap"], path["destino"]["airport"])["value"]
                
                trail_coordinates.append((origen["LATITUD"], origen["LONGITUD"]))
                trail_coordinates.append((destino["LATITUD"], destino["LONGITUD"]))
                    
                folium.Marker(location = (origen["LATITUD"],origen["LONGITUD"]), popup = origen["ICAO"], icon = folium.Icon("red")).add_to(mapa)
                folium.Marker(location = (destino["LATITUD"],destino["LONGITUD"]), popup = destino["ICAO"], icon = folium.Icon("red")).add_to(mapa)
                

        folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(mapa)
    
    if condicion == "req7":
        
        trail_coordinates = []
        
        for edge in lt.iterator(airports):
               
            vertexA = edge[0]
            vertexB = edge[1]
            
            trail_coordinates.append((vertexA["LATITUD"], vertexA["LONGITUD"]))             
            trail_coordinates.append((vertexB["LATITUD"], vertexB["LONGITUD"]))
            
            folium.Marker(location = (vertexA["LATITUD"],vertexA["LONGITUD"]), popup = vertexA["ICAO"], icon = folium.Icon("red")).add_to(mapa)
            folium.Marker(location = (vertexB["LATITUD"],vertexB["LONGITUD"]), popup = vertexB["ICAO"], icon = folium.Icon("red")).add_to(mapa)

        folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(mapa)
        
        
    folium.LayerControl().add_to(mapa)
    print("Mapa completado.")
    print("\n")

    nombre_archivo = "MapReq8.html"
    ruta_completa = os.path.join(directorio_actual, nombre_archivo)
    mapa.save(ruta_completa)
    print("\n")
    print("El archivo se guardó correctamente en:", ruta_completa)
    print("\n")

    print("Intentando abrir el archivo en el navegador...")
    print("\n")
    webbrowser.open("file://" + ruta_completa)
    print("Archivo abierto.")
    print("-"*40)


# Se crea el controlador asociado a la vista
control = new_controller()

airports_file = "airports-2022.csv"
flights_file = "flights-2022.csv"

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    lst_req_8 = [0,0,0,0,0,0,0,0,0,0,0,0]
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control, flights_file, airports_file )
        elif int(inputs) == 2:
            origen_latitud = float(input('Ingrese la latitud de origen: '))
            origen_longitud = float(input('Ingrese la longitud de origen: '))
            
            destino_latitud = float(input('Ingrese la latitud de destino: '))
            destino_longitud = float(input('Ingrese la longitud de destino: '))
            
            #origen_latitud, origen_longitud, destino_latitud, destino_longitud = float("4.601992771389502"), float("-74.06610470441926"), float("10.507688799813222"), float("-75.4706488665794")
            results, deltaTime = controller.req_1(control, origen_latitud, origen_longitud, destino_latitud, destino_longitud)
            data = results[1]
            
            if results[0] == "FOUNDPATH":
                lst_req_8[1] = data[2]
            
            print_req_1(control, data, deltaTime, results[0])
            
        elif int(inputs) == 3:
            origen_latitud = float(input('Ingrese la latitud de origen: '))
            origen_longitud = float(input('Ingrese la longitud de origen: '))          #Polo sur: 90.0000° S, 45.0000° E
            
            destino_latitud = float(input('Ingrese la latitud de destino: '))          #Antartida: float("82.8628"), float("135.0000")
            destino_longitud = float(input('Ingrese la longitud de destino: '))        #float("10.507688799813222"), float("-75.4706488665794")
            
            #origen_latitud, origen_longitud, destino_latitud, destino_longitud = float("4.601992771389502"), float("-74.06610470441926"), float("10.507688799813222"), float("-75.4706488665794")
            results, deltaTime = controller.req_2(control, origen_latitud, origen_longitud, destino_latitud, destino_longitud)
            data = results[1]
            
            if results[0] == "FOUNDPATH":
                lst_req_8[2] = data[2]
            
            print_req_2(control, data, deltaTime, results[0])

        elif int(inputs) == 4:
            data, deltaTime = controller.req_3(control)
            
            lst_req_8[3] = data[3]
            
            print_individuales(control, data, deltaTime)

        elif int(inputs) == 5:
            data, deltaTime = controller.req_4(control)
            
            lst_req_8[4] = data[3]
            
            print_individuales(control, data, deltaTime)

        elif int(inputs) == 6:
            data, deltaTime = controller.req_5(control)
            
            lst_req_8[5] = data[3]
            
            print_individuales(control, data, deltaTime)

        elif int(inputs) == 7:
            numAirports = int(input("Digite el numero de aeropuertos que desea analizar: "))
            results, deltaTime = controller.req_6(control, numAirports)

            lst_req_8[6] = results[1]
            
            print_req_6(control, results, deltaTime)

        elif int(inputs) == 8:
            origen_latitud = float(input('Ingrese la latitud de origen: '))
            origen_longitud = float(input('Ingrese la longitud de origen: '))          #Polo sur: 90.0000° S, 45.0000° E
            
            destino_latitud = float(input('Ingrese la latitud de destino: '))          #Antartida: float("82.8628"), float("135.0000")
            destino_longitud = float(input('Ingrese la longitud de destino: '))        #float("10.507688799813222"), float("-75.4706488665794")
            
            #origen_latitud, origen_longitud, destino_latitud, destino_longitud = float("4.601992771389502"), float("-74.06610470441926"), float("10.507688799813222"), float("-75.4706488665794")
            #origen_latitud, origen_longitud, destino_latitud, destino_longitud = float("4.71159"), float("-74.2469"), float("8.63333"), float("-77.35")
            results, deltaTime = controller.req_7(control, origen_latitud, origen_longitud, destino_latitud, destino_longitud)
            data = results[1]
            
            
            if results[0] == "FOUNDPATH":
                lst_req_8[7] = data[2]
            
            print_req_7(control, data, deltaTime, results[0])

        elif int(inputs) == 9:
            opcion = int(input("Digite el requerimiento que desea observar en el mapa: "))
            
            if lst_req_8[opcion] == 0:
                print("\n")
                print("---------------------------------------")
                print("No ha cargado el requerimiento todavia.")
                print("---------------------------------------")
                print("\n")
            else:
                
                condicion = controller.req_8(control, opcion)
                        
                print_req_8(control, lst_req_8[opcion], condicion)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
            
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
