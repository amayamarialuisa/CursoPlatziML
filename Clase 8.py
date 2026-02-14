import pandas as pd

# Mostrar todas las columnas
pd.set_option('display.max_columns', None)

# Cargar el dataset
df_partidos = pd.read_csv("partidos-cebollitas.csv")

# Ver las primeras filas completas
print(df_partidos.head())

#Nueva característica: diferencia de goles (local - visitante)
df_cebollitas = df_partidos[(df_partidos['equipo_local'] == 'Cebollitas FC') | (df_partidos['equipo_visitante'] == 'Cebollitas FC')].copy()

#Nueva columna con diferencia_goles
df_cebollitas['diferencia_goles'] = 0

#Calcular la diferencia de goles cuando Cebollitas FC es local
cond_local = df_cebollitas['equipo_local'] == 'Cebollitas FC'
df_cebollitas.loc[cond_local, 'diferencia_goles'] = (df_cebollitas.loc[cond_local, 'goles_local'] - df_cebollitas.loc[cond_local, 'goles_visitante'])

#Calcular la diferencia de goles cuando Cebollitas FC es visitante
cond_visitante = df_cebollitas['equipo_visitante'] == 'Cebollitas FC'
df_cebollitas.loc[cond_visitante, 'diferencia_goles'] = (df_cebollitas.loc[cond_visitante, 'goles_visitante'] - df_cebollitas.loc[cond_visitante, 'goles_local'])

pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)

print(df_cebollitas[['fecha_partido', 'equipo_local', 'equipo_visitante',
                     'goles_local', 'goles_visitante', 'diferencia_goles']])

print(df_cebollitas.columns)

#Histograma diferencia de goles

import matplotlib.pyplot as plt
import numpy as np

# Definir rango y bins de tamaño 1
min_gol = df_cebollitas['diferencia_goles'].min()
max_gol = df_cebollitas['diferencia_goles'].max()

bins = np.arange(min_gol - 0.5, max_gol + 1.5, 1)

plt.figure()
plt.hist(df_cebollitas['diferencia_goles'], bins=bins)
plt.xlabel('Diferencia de goles')
plt.ylabel('Cantidad de partidos')
plt.title('Histograma de la diferencia de goles de Cebollitas FC')

# Eje X con escala de 1 en 1
plt.xticks(range(min_gol, max_gol + 1))

plt.show()
