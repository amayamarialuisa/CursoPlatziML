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

sns.boxplot(x=df_partidos['goles_local'])
plt.title('Boxplot goles equipo local')
plt.show()

#Scatterplot de posesión vs goles marcados local
sns.scatterplot(x='posesion_local (%)', y='goles_local', data=df_partidos)
plt.title('Relacion posesion vs goles marcados (equipo local)')
plt.show()

#Mapa de calor para correlación entre variables clave
plt.figure(figsize=(10, 6))
sns.heatmap(df_partidos[['goles_local','goles_visitante','posesion_local (%)','posesion_visitante (%)','tiros_arco_local','tiros_arco_visitante']].corr(),annot=True, cmap='coolwarm')
plt.title('Mapa de calor - correlación entre variables')
plt.show()