import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Cargar datset partidos
df_partidos = pd.read_csv("partidos-cebollitas-limpio.csv")

#Mostrar primeras filas
print(df_partidos.head(6))

#Estadísticas descriptivas generales
print(df_partidos.describe())
