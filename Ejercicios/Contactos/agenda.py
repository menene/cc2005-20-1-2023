# -*- coding: utf-8 -*-

# ==============================================================
# Universidad del Valle de Guatemala
# CC2005 semestre 1 2023
# Sección 20
#
# Erick Marroquin
# Número de carné
#
# Agenda telefónica
# 14.03.23
# ==============================================================

def cargar_contactos(nombre_archivo):
    contactos = []
    with open(nombre_archivo) as file_object:
        for line in file_object:
            linea_contacto = line.rstrip()
            contacto_lista1 = linea_contacto.split('|')
            telefonos_lista1 = contacto_lista1[1].split('-')

            diccionario_contacto = {}
            diccionario_contacto['nombre'] = contacto_lista1[0].upper()
            diccionario_contacto['telefonos'] = telefonos_lista1
            contactos.append(diccionario_contacto)

    return contactos


path_contactos = "contactos.txt"
lista_contactos = cargar_contactos(path_contactos)
opcion = 0

while opcion != "4":
    print("=== AGENDA ===")
    print(" 1. Agregar contacto")
    print(" 2. Buscar contacto")
    print(" 3. Listar contactos")
    print(" 4. Salir")
    print("")
    opcion = input("Ingrese una opcion: ")

    # agregar contacto
    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto nuevo: ")
        cantidad_telefonos = int(
            input("Cuantos telefonos tiene " + nombre + ": "))

        lista_telefonos = []
        for i in range(cantidad_telefonos):
            telefono = input("Ingrese el teléfono " + str(i + 1) + ": ")
            lista_telefonos.append(telefono)

        diccionario_contacto = {}
        diccionario_contacto['nombre'] = nombre
        diccionario_contacto['telefonos'] = lista_telefonos

        lista_contactos.append(diccionario_contacto)

    # buscar un contacto por nombre
    if opcion == "2":
        busqueda = input("Ingrese el nombre para buscar: ")
        busqueda = busqueda.upper()

        for contacto in lista_contactos:
            if contacto['nombre'] == busqueda:
                print("Contacto encontrado... ")
                print(contacto['telefonos'])
                print("")

    # listar todos los contactos
    if opcion == "3":
        print("")
        print("- Lista de contactos -")
        for contacto in lista_contactos:
            print(contacto)

        print("")
        print("")

# guardar contactos
print("Guardando contactos...")
print("")

str_contactos = ""
for contacto in lista_contactos:
    telefonos = "-".join(contacto['telefonos'])
    str_contactos += contacto['nombre'] + "|" + telefonos + "\n"

archivo = open(path_contactos, "w", encoding="utf8")
archivo.write(str_contactos)
archivo.close()
