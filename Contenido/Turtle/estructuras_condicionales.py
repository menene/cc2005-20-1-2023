# -*- coding: utf-8 -*-

# ==============================================================
# Universidad del Valle de Guatemala
# CC2005 semestre 1 2023
# Sección 20
#
# Erick Marroquin
# 123
#
# Estructuras condicionales
# 14/02/2023
# ==============================================================

numero = int(input("Ingrese un numero: "))

# if numero == 10:
#     print('El numero es 10')
# else:
#     print('El numero no es 10')


# if numero > 0:
#     print("El numero es positivo")
# elif numero == 0:
#     print("El nuemro es 0")
# elif numero == 10:
#     print("El nuemro es 10")
# else:
#     print("El numero es negativo")

# if numero > 0:
#     if numero == 10:
#         print("El numero es 10")
#     else:
#         print("El numero es positivo")
# elif numero == 0:
#     print("El nuemro es 0")
# else:
#     print("El numero es negativo")


if numero > 0 and numero != 10:
    print("El numero es positivo")
elif numero == 0:
    print("El numero es 0")
elif numero == 10:
    print("El numero es 10")
else:
    print("El numero es negativo")
