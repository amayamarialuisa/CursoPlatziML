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

