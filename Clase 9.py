import pandas as pd

# =========================
# 1. Cargar datos
# =========================
df_partidos = pd.read_csv("partidos_cebollitas.csv")

# Filtrar solo partidos de Cebollitas FC
df_cebollitas = df_partidos[
    (df_partidos['equipo_local'] == 'Cebollitas FC') |
    (df_partidos['equipo_visitante'] == 'Cebollitas FC')
].copy()

# =========================
# 2. Máscaras lógicas
# =========================
mask_local = df_cebollitas['equipo_local'] == 'Cebollitas FC'
mask_visit = df_cebollitas['equipo_visitante'] == 'Cebollitas FC'

# =========================
# 3. Diferencia de goles (desde perspectiva de Cebollitas)
# =========================
df_cebollitas['diferencia_goles'] = None

df_cebollitas.loc[mask_local, 'diferencia_goles'] = (
    df_cebollitas.loc[mask_local, 'goles_local'] -
    df_cebollitas.loc[mask_local, 'goles_visitante']
)

df_cebollitas.loc[mask_visit, 'diferencia_goles'] = (
    df_cebollitas.loc[mask_visit, 'goles_visitante'] -
    df_cebollitas.loc[mask_visit, 'goles_local']
)

# =========================
# 4. Ratio tiros / posesión (una sola métrica)
# =========================
df_cebollitas['ratio_tiros_posesion'] = None

df_cebollitas.loc[mask_local, 'ratio_tiros_posesion'] = (
    df_cebollitas.loc[mask_local, 'tiros_arco_local'] /
    (df_cebollitas.loc[mask_local, 'posesion_local (%)'] / 100)
)

df_cebollitas.loc[mask_visit, 'ratio_tiros_posesion'] = (
    df_cebollitas.loc[mask_visit, 'tiros_arco_visitante'] /
    (df_cebollitas.loc[mask_visit, 'posesion_visitante (%)'] / 100)
)

# =========================
# 5. Variables finales para modelado
# =========================
df_cebollitas_modelo = df_cebollitas[
    [
        'diferencia_goles',
        'ratio_tiros_posesion'
    ]
].dropna()

# =========================
# 6. Revisión rápida
# =========================
df_cebollitas_modelo.head()

from sklearn.feature_selection import SelectKBest, f_regression


