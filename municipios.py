import json
from pathlib import Path
import os
import sys

try:
    
    #def mostrar_coordenadas():

    def mostrar_municipios():
        





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
        print("6. Mostrar Municipios con mayor número de habitantes")
        print("7. Salir")

        opc = int(input("Seleccione una opción: "))
        #Ahora se deben de especificar las diferentes opciones
        if opc == 1:
            #mostrar_coordenadas()
            print("En obras")
        elif opc == 2:
            mostrar_municipios()
        elif opc == 3:
        elif opc == 4:
        elif opc == 5:
        elif opc == 6:
        elif opc == 7:
            print("Gracias por su visita")
            break
        else:
            print("La opción no se encuentra disponible")
            input("Pulse tecla para continuar...")  






except:
    print("Se ha producido un error")
