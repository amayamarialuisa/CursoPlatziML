import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Cargar datset partidos
df_partidos = pd.read_csv("partidos-cebollitas.csv")

#Mostrar primeras filas
print(df_partidos.head(6))

#Estadísticas descriptivas generales
print(df_partidos.describe())

# Promedio goles Cebollitas como local y visitante
goles_local_cebo = df_partidos[df_partidos['equipo_local'] == 'Cebollitas FC']['goles_local'].mean()
goles_visitante_cebo = df_partidos[df_partidos['equipo_visitante'] == 'Cebollitas FC']['goles_visitante'].mean()

#Histogramas de goles marcados (local y visitantes)
fig, ax = plt.subplots(1, 2, figsize=(12, 4))

sns.histplot(df_partidos['goles_local'], kde=True, ax=ax[0], bins=10)
ax[0].set_title('Distribución goles equipo local')

sns.histplot(df_partidos['goles_visitante'], kde=True, ax=ax[1], bins=10, color='orange')
ax[1].set_title('Distribución goles equipo visitante')

plt.show()

#Boxplot para goles del equipo local
df_local_cebo = df_partidos[df_partidos['equipo_local']=='Cebollitas FC']

sns.boxplot(x=df_local_cebo['goles_local'])
plt.title('Boxplot goles Cebollitas como equipo local')
plt.show()

#Boxplot para goles de equipo visitante
df_visitante_cebo = df_partidos[df_partidos['equipo_visitante']=='Cebollitas FC']

sns.boxplot(x=df_visitante_cebo['goles_visitante'])
plt.title('Boxplot goles Cebollitas como visitante')
plt.show()

#Scatterplot de posesión vs goles marcados local
sns.scatterplot(x='posesion_local (%)', y='goles_local', data=df_partidos)
plt.title('Relacion posesion vs goles marcados (equipo local)')
plt.show()

#¿Ganamos más de local o de visitante?

