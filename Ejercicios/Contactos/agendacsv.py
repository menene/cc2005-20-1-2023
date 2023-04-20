# -*- coding: utf-8 -*-

# ==============================================================
# Universidad del Valle de Guatemala
# CC2005 semestre 1 2023
# Sección 20
#
# Erick Marroquin
# Número de carné
#
# Agenda telefónica csv
# 18.03.23
# ==============================================================

import csv

with open("AgendaContactos.csv", mode="r") as archivo:
    lineas = csv.DictReader(archivo)
    for linea in lineas:
        print(linea['Nombre'])
        #   print(linea["COL1"], linea["COL2"], linea["COL3"])

        # print(lineas)
