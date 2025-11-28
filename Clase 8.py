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
