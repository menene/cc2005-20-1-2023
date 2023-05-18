# -*- coding: utf-8 -*-

# ==============================================================
# Universidad del Valle de Guatemala
# CC2005 semestre 1 2023
# Sección 20
#
# Erick Marroquin
# Número de carné
#
# Pandas 2
# 02.05.23
# ==============================================================

import pandas as pd
import matplotlib.pyplot as plt

pokedex = pd.read_csv("pokemon_data.csv")

# print(pokedex)
# print(pokedex.loc[0]['Name'])

# filtrar todos los pokemon legendarios
# print(pokedex['Legendary'])
# legendarios = pokedex.loc[pokedex['Legendary'] == True]

# electricos y legendarios
# electricos = legendarios.loc[legendarios['Type 1'] == 'Electric']


# poderosos_fantasmas = pokedex.loc[
#     (pokedex['Speed'] >= 70) & (pokedex['Type 1'] == 'Ghost')
# ]

fantasmas_poderosos = pokedex.query("`Attack` >= 100 and `Type 1` == 'Ghost'")
# print(fantasmas_poderosos)

# imprimir valore faltantes
# print(fantasmas_poderosos.isnull())

# imprimir la cantidad de valores faltantes
# print(fantasmas_poderosos.isnull().sum()

# borrar todos los registros que tienen datos faltantes.
# print(fantasmas_poderosos.dropna())

# borar los registros que tienene datos faltantes en la columna Attack
# print(fantasmas_poderosos.dropna(subset=['Attack']))

# print(fantasmas_poderosos.sort_values(by='Name', ascending=True))
# print(fantasmas_poderosos)

# graficas
# fantasmas_poderosos.plot(
#     kind="bar",
#     x="Name",
#     y=["Attack", "Defense"],
#     title="Poderosos Fantasmas",
#     grid=False,
#     # rot=45,
#     # stacked=True
# )

# mostrar la grafica
# plt.show()

# grafica de pie
# df = pd.DataFrame({'mass': [0.330, 4.87, 5.97],
#                    'radius': [2439.7, 6051.8, 6378.1]},
#                   index=['Mercury', 'Venus', 'Earth'])

# plot = df.plot.pie(y='mass', figsize=(5, 5))
# plt.show()

# valores unicos
# print(fantasmas_poderosos['Attack'].unique())

# cantidad de valores unicos
# print(fantasmas_poderosos['Attack'].nunique())

# limpiar datos
# print(top_fantasmas[["Name", "Speed"]])
# print(fantasmas_poderosos[["Name", "HP", "Attack", "Defense"]])
# print(fantasmas_poderosos.iloc[0:3])
# print(fantasmas_poderosos.iloc[0:3, 1:3])

# top_fantasmas = fantasmas_poderosos.iloc[0:3, 1:10:8]
# print(top_fantasmas)
print("ORIGINAL: ")
print(fantasmas_poderosos[["Name", "HP", "Attack", "Defense"]])
print("================")

# fantasmas_poderosos[["Name", "HP", "Attack", "Defense"]].to_csv(
#     "poderosos_fantasmas.csv")


index = fantasmas_poderosos.index[
    fantasmas_poderosos['Name'] == 'Banette'].tolist()

print("INDICE: ")


print(index)
print("================")


print("EDITADO: ")
fantasmas_poderosos.loc[index, 'Name'] = 'Banette Editado'

# print(fantasmas_poderosos)
