# -*- coding: utf-8 -*-

# ==============================================================
# Universidad del Valle de Guatemala
# CC2005 semestre 1 2023
# Sección 20
#
# Erick Marroquin
# 123
#
# Uso de funciones
# 21/02/2023
# ==============================================================
def suma(n1, n2):
    """retorna la suma de 2 numeros"""
    return n1 + n2


def resta(n1, n2):
    """retorna la resta de 2 numeros"""
    return n1 - n2


def saludo(nombre="Nombre Genérico"):
    return "Hola " + nombre


sumatoria = suma(1000, 3000)
sumatoria2 = 1000 + 3000
print(sumatoria, sumatoria2)

diferencia = resta(5000, 2500)
print(diferencia)


mensaje = saludo()
print(mensaje)
