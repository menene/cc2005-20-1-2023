# -*- coding: utf-8 -*-

# ==============================================================
# Universidad del Valle de Guatemala
# CC2005 semestre 1 2023
# Sección 20
#
# Erick Marroquin
# Número de carné
#
# Agenda de contactos CSV - REPASO
# 20.04.23
# ==============================================================
import csv


def importar_contactos(nombre_archivo):
    contenido = []

    with open(nombre_archivo, mode="r") as archivo:
        lineas = csv.DictReader(archivo)
        for linea in lineas:
            contenido.append(linea)

    return contenido


def buscar_contacto(busqueda, contactos):
    resultado = 0

    for contacto in contactos:
        nombre_upper = contacto['Nombre'].upper()
        busqueda_upper = busqueda.upper()

        email_lower = contacto['E-mail'].lower()
        busqueda_lower = busqueda.lower()

        if nombre_upper == busqueda_upper or email_lower == busqueda_lower:
            resultado = contacto

    return resultado


def escribir_archivo(nombre_archivo, contactos):
    with open(nombre_archivo, mode='w') as archivo_csv:
        columnas = ['Mes en que nos conocimos',
                    'Profesión', 'Nombre', 'Lugar', 'E-mail']
        escritor = csv.DictWriter(archivo_csv, fieldnames=columnas)

        escritor.writeheader()

        for contacto in contactos:
            escritor.writerow(contacto)

    return


nombre_archivo = "AgendaContactos.csv"
contactos = importar_contactos(nombre_archivo)
opcion = "0"

# for contacto in contactos:
#     print(contacto)

while opcion != "6":
    print("=== AGENDA ===")
    print(" 1. Agregar contacto")
    print(" 2. Buscar contacto")
    print(" 3. Editar contacto")
    print(" 4. Eliminar contacto")
    print(" 5. Listar contactos")
    print(" 6. Salir")
    print("")

    opcion = input("Ingrese una opcion: ")

    # insertar contacto
    if opcion == "1":
        nombre = input("¿Como se llama el contacto? ")
        email = input("¿Cuál es el email? ")
        profesion = input("¿Cuál es la profesión? ")
        mes = input("¿En qué mes lo conociste? ")
        lugar = input("¿En donde lo conociste? ")

        contacto = {}
        contacto['Mes en que nos conocimos'] = mes
        contacto['Profesión'] = profesion
        contacto['Nombre'] = nombre
        contacto['Lugar'] = lugar
        contacto['E-mail'] = email

        contactos.append(contacto)

        print('El contacto fue creado exitosamente')

    # buscar contacto
    if opcion == "2":
        busqueda = input("Ingrese el nombre o email del contacto a buscar: ")
        resultado = buscar_contacto(busqueda, contactos)

        if resultado == 0:
            print('El contacto no fue encontrado')
        else:
            print("Datos del contacto: ")
            print(resultado)

    # editar contacto
    if opcion == "3":
        busqueda = input("Ingrese el nombre o email del contacto a editar: ")
        resultado = buscar_contacto(busqueda, contactos)

        if resultado == 0:
            print('El contacto no fue encontrado, por lo que no se puede editar')
        else:
            indice_contacto = contactos.index(resultado)
            print("Valores viejos: ")
            print(resultado)
            print("")

            nombre_viejo = resultado['Nombre']
            nombre_nuevo = input(
                "¿Cuál es el nuevo nombre (enter para conservar)? ")
            if nombre_nuevo == "":
                nombre_nuevo = nombre_viejo

            contactos[indice_contacto]['Mes en que nos conocimos'] = input(
                "¿Cuál es el nuevo mes? ")
            contactos[indice_contacto]['Profesión'] = input(
                "¿Cuál es la nueve profesión? ")
            contactos[indice_contacto]['Nombre'] = nombre_nuevo
            contactos[indice_contacto]['Lugar'] = input(
                "¿Cuál es el nuevo lugar? ")
            contactos[indice_contacto]['E-mail'] = input(
                "¿Cuál es el nuevo email? ")

            print('El contacto fue editado exitosamente')

    # eliminar contacto
    if opcion == "4":
        busqueda = input("Ingrese el nombre o email del contacto a eliminar: ")
        resultado = buscar_contacto(busqueda, contactos)

        if resultado == 0:
            print('El contacto no fue encontrado, por lo que no se puede eliminar')
        else:
            contactos.remove(resultado)
            print('El contacto fue eliminado exitosamente')

    if opcion == "5":
        for contacto in contactos:
            print(contacto['Nombre'], contacto['E-mail'],
                  contacto['Profesión'])

    print("")
    print("")

escribir_archivo(nombre_archivo, contactos)
