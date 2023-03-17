# -*- coding: utf-8 -*-

# ==============================================================
# Universidad del Valle de Guatemala
# CC2005 semestre 1 2023
# Sección 20
#
# Erick Marroquin
# Número de carné
#
# Diccionarios
# 16.03.23
# ==============================================================

diccionario1 = {'nombre': 'Erick', 'carnet': 'mar123', 'nota1': 100}

print(diccionario1)
# print(diccionario1['carnet'])
diccionario1['nota2'] = 90
diccionario1['nota1'] = 95
# print(diccionario1)

diccionario2 = {'nombre': 'Erick', 'carnet': 'mar123'}
diccionario2['notas'] = {"nota1": 100, "nota2": 90, "nota3": 95}
print(diccionario2['notas']['nota1'])
