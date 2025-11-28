import pandas as pd
#cargar datos del club
datos_cebollitas = pd.read_csv('partidos-cebollitas.csv')
print(datos_cebollitas.head())

#Revisar información general
print(datos_cebollitas.info())

#Encontrar y manejar datos faltantes
print("Valores faltantes por columna:")
print(datos_cebollitas.isnull().sum())

#One-Hot Encoding para equipos
datos_preparados = pd.get_dummies(datos_cebollitas, columns=['equipo_local', 'equipo_visitante'])
print(datos_preparados.head())

print(datos_preparados.dtypes)

#Eliminar filas duplicadas
datos_preparados.drop_duplicates(inplace=True)

print("Filas antes de eliminar duplicados:", len(datos_preparados))
datos_preparados.drop_duplicates(inplace=True)
print("Filas después:", len(datos_preparados))

#Manejar fechas
datos_preparados['fecha_partido'] = pd.to_datetime(datos_preparados['fecha_partido'], errors='coerce')
print("Fechas invalidas (NaT) luego de la conversión:")
print(datos_preparados['fecha_partido'].isnull().sum())

#Resumen de limpieza
print(datos_preparados.info())

print("Shape final del dataset preparado:", datos_preparados.shape)

pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)

print(datos_cebollitas)

datos_cebollitas['diferencia_goles'] = 0

datos_cebollitas['diferencia_goles'] = datos_cebollitas['goles_local'] - datos_cebollitas['goles_visitante']

print(datos_cebollitas)

# Crear columnas de puntos
datos_cebollitas['puntos_local'] = 0
datos_cebollitas['puntos_visitante'] = 0

# Empate
datos_cebollitas.loc[datos_cebollitas['diferencia_goles'] == 0, 'puntos_local'] = 1
datos_cebollitas.loc[datos_cebollitas['diferencia_goles'] == 0, 'puntos_visitante'] = 1

# Gana local
datos_cebollitas.loc[datos_cebollitas['diferencia_goles'] > 0, 'puntos_local'] = 3

# Gana visitante
datos_cebollitas.loc[datos_cebollitas['diferencia_goles'] < 0, 'puntos_visitante'] = 3

df_local = datos_cebollitas[['equipo_local', 'puntos_local']].copy()
df_local = df_local.rename(columns={'equipo_local': 'nombre_equipo',
                                    'puntos_local': 'puntos'})

df_visit = datos_cebollitas[['equipo_visitante', 'puntos_visitante']].copy()
df_visit = df_visit.rename(columns={'equipo_visitante': 'nombre_equipo',
                                    'puntos_visitante': 'puntos'})

df_puntos = pd.concat([df_local, df_visit], ignore_index=True)

df_campeon = df_puntos.groupby('nombre_equipo', as_index=False)['puntos'].sum()

print(df_campeon)


