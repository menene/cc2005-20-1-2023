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
# import matplotlib.pyplot as plt

pokedex = pd.read_csv("pokemon_data.csv")

# print(pokedex)
# print(pokedex.loc[0]['Name'])

# filtrar todos los pokemon legendarios
# print(pokedex['Legendary'])
legendarios = pokedex.loc[pokedex['Legendary'] == True]

# electricos y legendarios
electricos = legendarios.loc[legendarios['Type 1'] == 'Electric']


poderosos_fantasmas = pokedex.loc[(
    pokedex['Attack'] >= 100) & (pokedex['Type 1'] == 'Ghost')]

fantasmas_poderosos = pokedex.query("`Attack` >= 100 and `Type 1` == 'Ghost'")
print(fantasmas_poderosos)
