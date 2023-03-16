# -*- coding: utf-8 -*-

# ==============================================================
# Universidad del Valle de Guatemala
# CC2005 semestre 1 2023
# Sección 20
#
# Erick Marroquin
# Número de carné
#
# Cadenas
# 09.03.23
# ==============================================================


cadena = "Esta es mi cadena!!!"

print(cadena)

# imprimir el largo de una cadena
largo = len(cadena)
print(type(largo))
print(largo)
print(len(cadena))

# determinar si una cadena es numerica
cadena2 = "123"
if cadena2.isdigit():
    print("Es numerica")
else:
    print("No es numerica")

# determinar si una cadena es alpha
cadena3 = "holamundo"
if cadena3.isalpha():
    print("La cadena tiene solo letras")
else:
    print("Hay más que letras")

# modificando el case de las cadenas
cadena4 = "HoLa MuNdo"
mayusculas = cadena4.upper()
print(mayusculas)

minusculas = cadena4.lower()
print(minusculas)

titulo = cadena4.title()
print(titulo)

# buscar dentro de cadenas
cadena5 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eget erat ut dolor lobortis sollicitudin non sit amet massa. Nulla bibendum rhoncus risus, ac bibendum orci sodales in. Praesent finibus nibh imperdiet diam feugiat elementum. Nam vitae sem sed mauris aliquam vestibulum. Etiam a convallis ante, vel consequat enim. Nulla viverra luctus quam at pulvinar. Pellentesque tempor nibh id ipsum pulvinar, eu posuere metus condimentum. Donec in erat in quam rhoncus lobortis. Nam eget ligula in ex facilisis finibus et et justo. Quisque accumsan magna ac metus eleifend auctor. Curabitur at magna at mi venenatis sagittis. Fusce sagittis metus et purus ullamcorper rutrum. Aenean ut dolor egestas, dictum mi sed, varius sapien. "
print(len(cadena5))
cantidad_a = cadena5.count('sit')
print(cantidad_a)

# ubicaciones dentro de cadenas
cadena6 = "Hola como que tal"
ubicacion = cadena6.find("l")
ubicacion2 = cadena6.rfind("l")

print(ubicacion, ubicacion2)
print(cadena6[0])

# contar vocales, consonantes y espacios
cadena6 = cadena5.lower()
cant_vocales = 0
cant_consonantes = 0
cant_espacios = 0
for letra in cadena6:
    if letra == " ":
        cant_espacios = cant_espacios + 1
    elif letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        cant_vocales = cant_vocales + 1
    else:
        cant_consonantes = cant_consonantes + 1

print(cant_vocales, cant_consonantes, cant_espacios)
