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
# 14.03.23
# ==============================================================

lista1 = [1, 2, 3, 4, 5]

print(lista1)

# largo de una lista
print(len(lista1))

# cambio de valor a una posicion de la lista
lista1[0] = 6
print(lista1)

# slice de listas
print(lista1[0:3])

# agregar elementos a una lista
lista1.append(7)
print(lista1)

lista1.insert(1, 9)
print(lista1)
lista1[1] = lista1[1] + 9
print(lista1)

# eliminar elementos de una lista
lista1.append(4)
print(lista1)
lista1.remove(4)
print(lista1)

elemento = lista1[-1]
print(elemento, lista1)

print(lista1)
elemento = lista1.pop(3)
print(elemento, lista1)
