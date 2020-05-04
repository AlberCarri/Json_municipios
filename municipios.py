import json
from pathlib import Path
import os
import sys

try:
    
    #def mostrar_coordenadas():

    def mostrar_municipios(datos):
        nom_provincia=input("Introduce el nombre de la provincia: ")

        for prov in datos:
            if prov["Provincia"]==nom_provincia:
                print(prov['Municipio'])
        input("Pulse para continuar...")


    def mostrar_provincia(datos):
        nom_municipio=input("Introduce el nombre del municipio: ")
        
        for mun in datos:
            if mun["Municipio"]==nom_municipio:
                print("Provincia: %s"%mun['Provincia'])
        input("Pulse para continuar...")

    def mostrar_municipios_mancomunidad(datos):
        nom_mancomunidad=input("Introduce el nombre de la mancomunidad: ")

        for man in datos:
            if man["Mancomunidades"]==nom_mancomunidad:
                print(man['Municipio'])
        input("Pulse para continuar...")

    def num_municipios(datos):
        nom_provincia=input("Introduce el nombre de la provincia: ")
       
        for prov in datos:
            if prov["Provincia"]==nom_provincia:
                numero=len(prov)
        print("Numero de municipios en la provincia: ",numero)

    def mostrar_municipio_menor_habitantes(datos):
        num_habitantes=int(input("Introduce el número de habitantes: "))

        for hb in datos:
            if hb["Población"]<num_habitantes:
                print(hb['Municipio'])
        input("Pulse para continuar...")

    def mostrar_municipio_mayor_habitantes(datos):
        num_habitantes=int(input("Introduce el número de habitantes: "))

        for hb in datos:
            if hb["Población"]>num_habitantes:
                print(hb['Municipio'])
        input("Pulse para continuar...")

#abro el fichero json en el que se van a encontrar los municipios de Castilla y León
    base_path = Path(__file__).parent
    file_path = (base_path / "MunicipiosCyL.json").resolve()
    with open(file_path,'r',encoding='utf-8') as file:
        #json.load. devuelve un objeto de tipo diccionario sobre el que se puede iterar.
        datos = json.load(file)


#Creo el menú con el que el usuario va a interactuar
    while True:
        #Poner un cls, para borrar toda la pantalls

        print("1. Mostrar latitud y longitud de un Municipio")
        print("2. Mostrar Municipios de una Provincia")
        print("3. Mostrar Provincia de un municipio")
        print("4. Mostrar Municipios pertenecientes a una Mancomunidad")
        print("5. Número de Municipios de una Provincia")
        print("6. Mostrar Municipios con menor número de habitantes")
        print("7. Mostrar Municipios con mayor número de habitantes")
        print("8. Salir")

        opc = int(input("Seleccione una opción: "))
        #Ahora se deben de especificar las diferentes opciones
        if opc == 1:
            #mostrar_coordenadas()
            print("En obras")
        elif opc == 2:
            mostrar_municipios(datos)
        elif opc == 3:
            mostrar_provincia(datos)
        elif opc == 4:
            mostrar_municipios_mancomunidad(datos)
        elif opc == 5:
            num_municipios(datos)
        elif opc == 6:
            mostrar_municipio_menor_habitantes(datos)
        elif opc == 7:
            mostrar_municipio_mayor_habitantes(datos)
        elif opc == 8:
            print("Gracias por su visita")
            break
        else:
            print("La opción no se encuentra disponible")
            input("Pulse tecla para continuar...")  






except:
    print("Se ha producido un error")
