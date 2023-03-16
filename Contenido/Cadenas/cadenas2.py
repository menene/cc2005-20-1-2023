# -*- coding: utf-8 -*-

# ==============================================================
# Universidad del Valle de Guatemala
# CC2005 semestre 1 2023
# Sección 20
#
# Erick Marroquin
# Número de carné
#
# Cadenas 2
# 14.03.23
# ==============================================================

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eget erat ut dolor lobortis sollicitudin non sit amet massa. Nulla bibendum rhoncus risus, ac bibendum orci sodales in. Praesent finibus nibh imperdiet diam feugiat elementum. Nam vitae sem sed mauris aliquam vestibulum. Etiam a convallis ante, vel consequat enim. Nulla viverra luctus quam at pulvinar. Pellentesque tempor nibh id ipsum pulvinar, eu posuere metus condimentum. Donec in erat in quam rhoncus lobortis. Nam eget ligula in ex facilisis finibus et et justo. Quisque accumsan magna ac metus eleifend auctor. Curabitur at magna at mi venenatis sagittis. Fusce sagittis metus et purus ullamcorper rutrum. Aenean ut dolor egestas, dictum mi sed, varius sapien"

palabras = texto.split(" ")

# imprimir lista de palabras
print(palabras)

# imprimir primera palaba
print(palabras[0])

# imprimir la ultima palabra
print(palabras[len(palabras) - 1])
ultimo_indice = len(palabras) - 1
print(palabras[ultimo_indice])
print(palabras[-1])

# slices
cadena2 = "Hola a todos, como les va?"
print(cadena2)

sub_cadena = cadena2[3:12]
print(sub_cadena)

sub_cadena2 = cadena2[3:12:2]
print(sub_cadena2)
