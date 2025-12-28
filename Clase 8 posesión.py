import pandas as pd

# Mostrar todas las columnas
pd.set_option('display.max_columns', None)

# Cargar el dataset
df_partidos = pd.read_csv("partidos-cebollitas.csv")

# Ratio tiros / posesión (LOCAL)

df_partidos['ratio_tiros_pose_local'] = None

mask_local = df_partidos['equipo_local'] == 'Cebollitas FC'

df_partidos.loc[mask_local, 'ratio_tiros_pose_local'] = (
    df_partidos.loc[mask_local, 'tiros_arco_local'] /
    (df_partidos.loc[mask_local, 'posesion_local (%)'] / 100)
)

# Ratio tiros / posesión (VISITANTE)

df_partidos['ratio_tiros_pose_visitante'] = None

mask_visitante = df_partidos['equipo_visitante'] == 'Cebollitas FC'

df_partidos.loc[mask_visitante, 'ratio_tiros_pose_visitante'] = (
    df_partidos.loc[mask_visitante, 'tiros_arco_visitante'] /
    (df_partidos.loc[mask_visitante, 'posesion_visitante (%)'] / 100)
)

# MOSTRAR SOLO PARTIDOS DE CEBOLLITAS FC

df_cebollitas = df_partidos.loc[
    mask_local | mask_visitante
]

print(df_cebollitas)

pd.set_option('display.max_columns', None)

# Relación entre tiros al arco y goles local

df_partidos['ratio_tiros_goles_local'] = None

mask_local_goles = df_partidos['equipo_local'] == 'Cebollitas FC'

df_partidos.loc[mask_local_goles, 'ratio_tiros_goles_local'] = (
    df_partidos.loc[mask_local_goles, 'goles_local'] /
    (df_partidos.loc[mask_local_goles, 'tiros_arco_local'] / 100))

#Relación entre tiros al arco y goles visitante

df_partidos['ratio_tiros_goles_visitante'] = None

mask_visitante_goles = df_partidos['equipo_visitante'] == 'Cebollitas FC'

df_partidos.loc[mask_visitante_goles, 'ratio_tiros_goles_visitante'] = (
    df_partidos.loc[mask_visitante_goles, 'goles_visitante'] /
    (df_partidos.loc[mask_visitante_goles, 'tiros_arco_visitante'] / 100))

# MOSTRAR SOLO PARTIDOS DE CEBOLLITAS FC

df_cebollitas_goles = df_partidos.loc[
    mask_local_goles | mask_visitante_goles
]

pd.set_option('display.max_columns', None)

pd.set_option('display.width', None)

print(df_cebollitas_goles)

