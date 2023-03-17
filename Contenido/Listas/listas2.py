# -*- coding: utf-8 -*-

# ==============================================================
# Universidad del Valle de Guatemala
# CC2005 semestre 1 2023
# Sección 20
#
# Erick Marroquin
# Número de carné
#
# Listas
# 16.03.23
# ==============================================================

miLista = [75, 80, 50, 95, 100]
print(miLista)

# ordenamos una lista
# miLista.sort()
# miLista.sort(reverse=True)
# print(miLista)

# unimos dos listas
miSegundaLista = ['a', 'e', 'i', 'o', 'u']
# miLista.extend(miSegundaLista)
# print(miLista)

# cadena a lista
cadena = "Hola como les va"
listaCadena = list(cadena)

# lista a cadena
nuevaCadena = '-'.join(listaCadena)
# print(miSegundaLista)
# miSegundaLista.clear()
# print(miSegundaLista)

# validar existencia
# if 'A' in miSegundaLista:
#     print('Si existe')
# else:
#     print('No existe')

# obtener el indice dado el valor
print(miSegundaLista)
indice = miSegundaLista.index('x')
print(indice)
