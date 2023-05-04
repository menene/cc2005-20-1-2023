# -*- coding: utf-8 -*-

# ==============================================================
# Universidad del Valle de Guatemala
# CC2005 semestre 1 2023
# Sección 20
#
# Erick Marroquin
# Número de carné
#
# Pandas 1
# 27.04.23
# ==============================================================

import pandas as pd

df = pd.DataFrame({
    'Hoja de trabajo 1': [80, 85, 75, 40, 0],
    'Hoja de trabajo 2': [90, 90, 75, 61, 100],
    'Hoja de trabajo 3': [80, 80, 0, 50, 90],
    'Evaluacion 1': [70, 60, 10, 30, 90],
})

# imprimir todo el data frame
# print(df)

# imprimir la forma
# print(df.shape)

# imprimir estadistica de los datos
# print(df.describe())

# imprimir la media de las columnas
# print(df.mean())

# imprimir la cantidad de registros
# print(df.count())

# imprimir el valor maximo
# print(df.max())

# imprimir el valor menor
# print(df.min())

# imprimir la mediana
# print(df.median())

# imprimir desviacion estandard
# print(df.std())

# imprimir info. por columna
# print(df['Hoja de trabajo 1'][2])

# crear un sub dataframe
# hojas = df[['Hoja de trabajo 1', 'Hoja de trabajo 2', 'Hoja de trabajo 3']]
# print(hojas)

# imprimir la primera fila
# print(df.iloc[0])

# primer valor de la primera fila
# print(df.iloc[0][0])


# print(df.loc[0])
