# -*- coding: utf-8 -*-

# ==============================================================
# Universidad del Valle de Guatemala
# CC2005 semestre 1 2023
# Sección 20
#
# Erick Marroquin
# Número de carné
#
# Archivos 1
# 13.04.23
# ==============================================================

filename = "/Users/erickmarroquin/code/python/cc2005-20-2023-1/Contenido/Archivos/nombre.txt"

# abrir un archivo y leer todo el contenido
# archivo = open(
#     filename, "r", encoding="utf8")
# contenido = archivo.read()

# print(contenido)

# archivo.close()

# leer un archivo linea por linea
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# escribir a un archivo, reemplazando su contenido
archivo = open("nombre2.txt", "w", encoding="utf8")

archivo.write("Este conetenido se va a escribir en el archivo.")

archivo.close()
